#!/usr/bin/env python3

import csv
import json
import re
import urllib.request
import yaml

from pathlib import Path
from collections import OrderedDict
from common import load_from_path, randomlist, to_text_blocks
from allspells import load_all_spells, long_spells

SOURCE = './sources/spells'
level = 0

spells_loaded = 0

def include(row):
    """
    Use this function to filter the items processed.
    """
    global spells_loaded
    if row['name'] not in load_all_spells():
        return False
    if row['name'] in (
        "Counterspell",
        "Blade Ward",
        "Druidcraft",
        "Poison Spray",  # Prepare this
        "Spare the dying",
        # "True Strike",
        "Vicious Mockery",

        "Armor of Agathys",
        "Banishing Smite",
        "Branding Smite",
        "Chain Lightning"
        "Charm Monster",
        "Commune with Nature",
        "Compulsion",
        "Contact Other Plane",
        "Counterspell",
        "Crown of Stars",
        "Disguise Self",
        "Dominate Monster",
        "Earthbind",
        "Ensnaring Strike",
        "Ensnaring Strike",
        "Etherealness",
        "Find Steed",
        "Glibness",
        "Goodberry",
        "Grasping Vine",
        "Guardian of Nature",
        "Gust",
        "Harm",
        "Magic Circle",
        "Mental Prison",
        "Move Earth",
        "Phantasmal Force",
        "Power Word Heal",
        "Prismatic Wall",
        "Pyrotechnics",
        "Scrying",
        "Shatter",
        "Skill Empowerment",
        "Temple of the Gods",
        "Tidal Wave",
        "Wall of Force",
        "Water Breathing",
    ):
        spells_loaded += 1
        return True
    if row['name'] in long_spells():
        return False
    # if spells_loaded < 18:
    #     spells_loaded += 1
    #     return True
    return False


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
        9: 'indigo',
        8: 'mediumblue',
        7: 'teal',
        6: 'darkgreen',
        5: 'olive',
        4: 'darkgoldenrod',
        3: 'darkorange',
        2: 'orangered',
        1: 'saddlebrown',
        0: 'slategray',
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
    print(row['name'])
    tags = ['spell', 'level_{}'.format(row['level'])]
    subtitle = get_subtitle(row)
    ritual = 'ritual' if row.get('ritual') else ''
    concentration = 'concentration' if row.get('concentration') else ''
    contents = [
        'subtitle | {}'.format(subtitle),
        'rule',
        'property | Casting time | {}<span class="subtitle-right">{}</span>'.format(row['casting_time'], ritual),
        'property | Duration | {}<span class="subtitle-right">{}</span>'.format(row['duration'], concentration),
        'property | Range | {}'.format(row['range']),
        'property | Components | {}'.format(get_components(row)),
        'rule',
    ] + to_text_blocks(row['desc'])

    if row.get('higher_level'):
        contents += [
            'fill',
            'section | Higher levels',
        ] + to_text_blocks(row['higher_level'])

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
    for row in load_from_path(folder):
        row = clean(row)
        if include(row):
            data.append(convert(row))

    write_json(data, outfile)


if __name__ == '__main__':
    # randomlist('./sources/spells', 6, level=0)
    main('./sources/spells', 'spells.json')
