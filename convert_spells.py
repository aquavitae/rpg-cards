#!/usr/bin/env python3

import csv
import json
import re
import urllib.request
import yaml

from pathlib import Path
from collections import OrderedDict

printed = [
]

def include(row):
    """
    Use this function to filter the items processed.
    """
    name = row['name'].lower()
    if name in printed:
        return False

    # classes = [c['name'] for c in row['classes']]
    if row['level'] <= 1 and 'Paladin' in row['classes']:
        return True
    if row['name'] in ["Hunter's Mark", 'Hail of Thorns', 'Ensnaring Strike']:
        return True
    if row['level'] == 0 :
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
        return '\n'.join(x)
    return x


def load_from_file(path):
    with path.open(encoding='utf-8') as fh:
        return yaml.load(fh)

def get_icon_and_colour(row):
    # icon = {
    #     'Abjuration': 'bolt-shield',
    #     'Conjuration': 'teleport',
    #     'Divination': 'meditation',
    #     'Enchantment': 'coma',
    #     'Evocation': 'bubbling-beam',
    #     'Illusion': 'relationship-bounds',
    #     'Necromancy': 'death-zone',
    #     'Transmutation': 'embrassed-energy',
    # }.get(row['school']['name'])
    icon = 'tied-scroll'
    colour = {
        9: 'rebeccapurple', # '#670000',
        8: 'steelblue', # '#811A1A',
        7: 'teal', # '#9A3333',
        6: 'darkgreen', # '#B33D3D',
        5: 'olive', # '#CD6666',
        4: 'darkgoldenrod', # '#E67F7F',
        3: 'darkorange', # '#FF9999',
        2: 'darkred', # '#FFB3B3',
        1: 'saddlebrown', # '#FFCCCC',
        0: 'slategray', # '#FFE5E5',
    }[row['level']]
    return icon, colour


def get_subtitle(row):
    name = row['school']['name']
    level = row['level']
    if level == 0:
        level = 'cantrip'
    else:
        level = 'level {}'.format(level)
    return '{}<span class="subtitle-right">{}</span>'.format(name, level)


def get_components(row):
    icons = []
    text = ''
    if 'M' in row['components']:
        icons.append('oak-leaf')
    if 'S' in row['components']:
        icons.append('slap')
    if 'V' in row['components']:
        icons.append('shouting')
    if len(icons) == 0:
        return 'None'
    right = 2
    for icon in icons:
        text += '<span class="card-inlineicon icon-{}" style="position:absolute;right:{}mm"></span>'.format(icon, right)
        right += 4
    if row.get('material'):
        text += '<br><i>{}</i>'.format(row['material'])
    return text


def clean(row):
    classes = [c if isinstance(c, str) else c['name'] for c in row['classes']]
    classes = [c for c in classes if ' ' not in c]
    row['classes'] = sorted(set(classes))
    if isinstance(row['components'], str):
        row['components'] = list(row['components'])
    return row


def convert(row):
    tags = ['spell', 'level_{}'.format(row['level'])]
    subtitle = get_subtitle(row)
    ritual = 'ritual' if row.get('ritual') else ''
    concentration = 'concentration' if row['concentration'] else ''
    contents = [
        'subtitle | {}'.format(subtitle),
        'rule',
        'property | Casting time | {}<span class="subtitle-right">{}</span>'.format(row['casting_time'], ritual),
        'property | Duration | {}<span class="subtitle-right">{}</span>'.format(row['duration'], concentration),
        'property | Range | {}'.format(row['range']),
        'property | Components | {}'.format(get_components(row)),
        'rule',
        'text | {}'.format(tostring(row['desc']))
    ]

    if row.get('higher_level'):
        contents += [
            'fill',
            'section | Higher levels',
            'text | {}'.format(tostring(row['higher_level']))
        ]

    classes = ', '.join(row['classes'])
    contents.append('text | <span class="right-footer">{}</span>'.format(classes))

    icon, colour = get_icon_and_colour(row)

    data = {
        'count': 1,
        'color': colour,
        'title': row['name'],
        'icon': icon,
        'contents': contents,
        'tags': tags,
    }
    if row.get('title_size'):
        data['title_size'] = row['title_size']
    return data

def write_json(data, outfile):
    data = sorted(data, key=lambda x: x['title'])
    with open(outfile, 'w') as fh:
        json.dump(data, fh, indent=2)


def main(folder, outfile):
    data = []
    for infile in Path(folder).iterdir():
        for row in load_from_file(infile):
            row = clean(row)
            if include(row):
                data.append(convert(row))

    write_json(data, outfile)


if __name__ == '__main__':
    main('./sources/spells', 'spells.json')
