#!/usr/bin/env python3

import random
import requests
import json
import re
import urllib.request
import yaml

from common import load_from_file, randomlist, write_json, tostring
from collections import OrderedDict
from pathlib import Path

def include(row):
    """
    Use this function to filter the items processed.
    """
    name = row['name'].lower()
    if name in (
        'rapier of wounding',
        'cloak of the manta ray',
        'bead of force',
    ):
        return True
    return False


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
    caption = '{} ({} {})'.format(row['category'], row['level'], row['rarity'])
    if row.get('attunement'):
        caption += '<span class="subtitle-right">Attunement</span>'
    return caption


def get_properties(row):
    properties = []
    for prop in row.get('properties', []):
        for name, desc in prop:
            name = name[0].upper() + name[1:]
            properties.append('property | {} | {}'.format(name, desc))
    return properties


def get_contents(row):
    properties = get_properties(row)
    contents = []
    if properties:
        contents = properties + ['rule']

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
    if 'picture_flex_ratio' in row:
        data['picture_flex_ratio'] = row['picture_flex_ratio']
    elif 'picture_ratio' in row:
        data['picture_flex_ratio'] = row['picture_ratio']

    return data


def main(folder, outfile):
    data = []
    for infile in Path(folder).iterdir():
        print(infile)
        for row in load_from_file(infile):
            if include(row):
                data.append(convert(row))

    write_json(data, outfile)

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
    # randomlist('sources/items', 6, level="minor", rarity='rare')
    main('sources/items', 'items.json')
    # fetch_all('sources/items/dmg-complete.yml', 'sources/items/dmg-clean.yml')
