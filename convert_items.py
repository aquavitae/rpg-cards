#!/usr/bin/env python

import random
import requests
import json
import re
import urllib.request
import yaml

from collections import OrderedDict
from pathlib import Path

printed = [
]

def include(row):
    """
    Use this function to filter the items processed.
    """
    name = row['name'].lower()
    if name in printed:
        return False
    if name in (
        'immovable rod',                # Um
        'sending stones',               # Um
        'slippers of spider climbing',  # UM
        'adamantine breastplate',       # UM
        'portable hole',                # Rm
        'potion of healing',            # Cm
    ):
        return True
    return False


def represent_ordereddict(dumper, data):
    value = []
    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        value.append((node_key, node_value))
    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)


def str_presenter(dumper, data):
  if len(data.splitlines()) > 1:  # check for multiline string
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
  return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(OrderedDict, represent_ordereddict)
yaml.add_representer(str, str_presenter)


def tostring(x):
    if isinstance(x, list):
        return ''.join(x)
    return x.replace('\n\n', '<br>')


def load_from_file(filename):
    with open(filename) as fh:
        return yaml.load(fh)


def get_icon_and_colour(row):
    colour = {
        'common': "saddlebrown",
        'uncommon': "steelblue",
        'rare': "darkgreen",
        'very rare': "darkgoldenrod",
        'legendary': "rebeccapurple",
    }[row['rarity']]
    icon = {
        "Armor": "breastplate",
        "Potion": "magic-potion",
        "Ring": "ring",
        "Rod": "lunar-wand",
        "Scroll": "tied-scroll",
        "Staff": "wizard-staff",
        "Wand": "fairy-wand",
        "Weapon": "war-axe",
        "Wondrous Item": "minerals",
    }[row['category']]
    if row.get('icon'):
        icon = row['icon']

    return icon, colour


def get_caption(row):
    caption = '{} ({})'.format(row['category'], row['rarity'])
    if row.get('attunement'):
        caption += '<span class="subtitle-right">Attunement</span>'
    return caption


def get_contents(row):
    contents = []
    if row.get('description') or row.get('type'):
        line = 'text |'
        if row.get('type'):
            line += ' <b>{}</b>'.format(tostring(row['type']))
        if row.get('description'):
            line += ' <i>{}</i>'.format(tostring(row['description']))
        contents.append(line)
    if len(contents) > 0:
        contents.append('rule')
    if row.get('usage'):
        contents.append('text | {}'.format(tostring(row['usage'])))
    return contents

def convert(row):
    title = row['name']
    tags = row.get('tags', [])
    tags.append(row['level'])
    caption = get_caption(row)
    contents = get_contents(row)
    icon, colour = get_icon_and_colour(row)
    data = {
        'count': 1,
        'color': colour,
        'title': title,
        'icon': icon,
        'contents': contents,
        'tags': tags,
        'title_size': 12,
        'picture': row.get('picture'),
        'caption': caption,
    }
    if row.get('title_size'):
        data['title_size'] = row['title_size']
    if 'picture_ratio' in row:
        data['picture_flex_ratio'] = row['picture_ratio']
    return data


def write_json(data, outfile):
    # data = sorted(data, key=lambda x: x['name'])
    with open(outfile, 'w') as fh:
        json.dump(data, fh, indent=2)


def main(infile, outfile):
    data = []
    for row in load_from_file(infile):
        if include(row):
            data.append(convert(row))

    write_json(data, outfile)


def randomlist(infile, number, **filters):
    items = []
    for row in load_from_file(infile):
        for k, v in filters.items():
            if row.get(k) != v:
                break
        else:
            items.append(row)

    for _ in range(number):
        index = random.randint(0, len(items) - 1)
        item = items[index]
        del items[index]
        print(item['name'])


def fetch_all(infile, outfile):
    items = []
    levels = {}

    levels_raw = load_from_file('sources/items/cats.yml')
    for l in levels_raw['major']:
        levels[l.lower()] = 'major'
    for l in levels_raw['minor']:
        levels[l.lower()] = 'minor'

    for row in load_from_file(infile):
        level = levels.get(row['Name'].lower(), None)
        if level is None:
            print('No level for %s' % row['Name'])
        else:
            del levels[row['Name'].lower()]
        item = OrderedDict([
            ('name', row['Name']),
            ('source', row['Source']),
            ('rarity', row['Rarity'].lower()),
            ('category', row['Type']),
            ('level', level),
            ('attunement', row['Attunement'] == 'yes'),
            ('description', row.get('Description', '')),
        ])
        if 'Limits' in row:
            item['limits'] = row['Limits']
        items.append(item)

    for item in levels:
        items.append(OrderedDict([
            ('name', item),
            ('source', 'xge'),
            ('level', levels[item]),
        ]))
        print('Unused item: ', item)

    stream = yaml.dump(items, default_flow_style=False)
    with open(outfile, 'w') as fh:
        fh.write(stream.replace('\n- ', '\n\n- '))


if __name__ == '__main__':
    randomlist('sources/items/dmg-clean.yml', 6, level="minor", rarity='common')
    # main('sources/items/dmg-clean.yml', 'items.json')
    # fetch_all('sources/items/dmg-complete.yml', 'sources/items/dmg-clean.yml')
