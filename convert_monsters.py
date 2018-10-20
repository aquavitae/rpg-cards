#!/usr/bin/env python

import csv
import json
import re
import urllib.request

from pathlib import Path

from common import load_from_file, highlight_dice

SKILLS = [
    ('Acrobatics', 'acrobatics'),
    ('Animal Handling', 'animal-handling'),
    ('Arcana', 'arcana'),
    ('Athletics', 'athletics'),
    ('Deception', 'deception'),
    ('History', 'history'),
    ('Insight', 'insight'),
    ('Intimidation', 'intimidation'),
    ('Investigation', 'investigation'),
    ('Medicine', 'medicine'),
    ('Nature', 'nature'),
    ('Perception', 'perception'),
    ('Performance', 'performance'),
    ('Persuasion', 'persuasion'),
    ('Religion', 'religion'),
    ('Sleight of Hand', 'sleight-of-hand'),
    ('Stealth', 'stealth'),
    ('Survival', 'survival'),
]

printed = [
    'cult fanatic',
    'cultist',
    'guard',
    'ogrillon (half-ogre)',
    'outland veteran',
    'scholar',
    'scout',
    'skeleton'
    'sprite',
    'thug',
    'warlock initiate of the fiend',
    'wolf',
    'zombie',
    'gnoll', 'gnoll pack lord', 'harpy', 'commoner',
    'faskar the fallen', 'tomi norelon',
    # smaller font
    'gnoll flesh gnawer', 'gnoll hunter', 'gnoll witherling', 'ghoul',
    'shadow', 'shadow (wolf)',
    'hyena', 'ghast', 'scarecrow', 'cockatrice',
    'green hag', 'ghost',
    'warlock of the archfey', 'master thief', 'scoundrel', 'pixie', 'imp', 'rat', 'spider', 'raven'
    'bandit', 'dire wolf', 'druid', 'giant spider', 'swarm of bats', 'swarm of ravens', "will-o'-wisp",
    'needle blight', 'twig blight', 'vine blight', 'werewolf',
    'assassin', 'beserker', 'bandit captain', 'strahd zombie', 'revenant', 'vampire spawn',
    'gladiator', 'veteran', 'spy', 'wereraven',
    'night hag',
    'dretch',    'nightmare',
    'owl',
    'imp',
    'quasit',
    'young blue dragon',
]

TO_PRINT = [
    'displacer beast',
    'flesh golem',
]

def include(row):
    """
    Use this function to filter the items processed.
    """
    name = row['name'].lower()
    if name in TO_PRINT:
        return True
    return False
    # return True

def get_tags(row):
    tags = [row['size'], row['type']]
    if row.get('legendary_actions'):
        tags.append('legendary')
    if row.get('subtype'):
        tags.append(row['subtype'])
    return tags


def cr_stats(row):
    cr_span = '<span class="subtitle-right">{}, CR: {}</span>'
    cr = row['challenge_rating']
    if 'xp' in row:
        xp = row['xp']
    else:
        xp = {
            0: '10',     14: '11500',
            0.125: '25', 15: '13000',
            0.25: '50',  16: '15000',
            0.5: '100',  17: '18000',
            1: '200',    18: '20000',
            2: '450',    19: '22000',
            3: '700',    20: '25000',
            4: '1100',   21: '33000',
            5: '1800',   22: '41000',
            6: '2300',   23: '50000',
            7: '2900',   24: '62000',
            8: '3900',   25: '75000',
            9: '5000',   26: '90000',
            10: '5900',  27: '105000',
            11: '7200',  28: '120000',
            12: '8400',  29: '135000',
            13: '10000', 30: '155000',
        }[cr]
    if cr == 0.125:
        cr = '1/8'
    if cr == 0.25:
        cr = '1/4'
    if cr == 0.5:
        cr = '1/2'

    alignment = row['alignment']
    if alignment.lower() != "any alignment":
        alignment = re.sub(r'\s*alignment\s*', ' ', alignment, re.I).strip()

    return cr_span.format(alignment, cr)


def stats(row):
    _, colour = get_icon_and_colour(row)
    div_style = 'style="width:33%;float:left"'
    stat_style = 'style="color:{};font-size:180%"'.format(colour)
    template = '<div {div_style}><b>{title}<br><span {stat_style}>{value}</span></b><br>{description}</div>'

    armour = row.get('armor', '')
    hit_dice = row['hit_dice']
    speeds = [re.sub(r'\s*ft\.?', '', x).strip() for x in row['speed'].split(',')]
    speed = 'NA'
    extra_speeds = ''
    if speeds:
        speed = speeds[0]
        if len(speeds) > 1:
            extra_speeds = ', '.join(speeds[1:])

    if not (hit_dice == '' and armour == '' and extra_speeds == ''):
        hit_dice = hit_dice or '&nbsp'
        armour = armour or '&nbsp'
        extra_speeds = extra_speeds or '&nbsp'

    ac_div = template.format(div_style=div_style,
                             title='Armour Class',
                             stat_style=stat_style,
                             value=row['armor_class'],
                             description=armour)

    hp_div = template.format(div_style=div_style,
                             title='Hit Points',
                             stat_style=stat_style,
                             value=row['hit_points'],
                             description=hit_dice)

    cr_div = template.format(div_style=div_style,
                             title='Speed',
                             stat_style=stat_style,
                             value=speed,
                             description=extra_speeds)

    return 'text | <div style="text-align:center">{}{}{}</div>'.format(ac_div, hp_div, cr_div)


def dnd_stats(row):
    return 'dndstats | {} | {} | {} | {} | {} | {}'.format(row['strength'],
                                                           row['dexterity'],
                                                           row['constitution'],
                                                           row['intelligence'],
                                                           row['wisdom'],
                                                           row['charisma'])


def attributes(row):
    lines = []

    # Saving throws
    saving = []
    for key in ('strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma'):
        if key + '_save' in row:
            name = key[0].upper() + key[1:]
            value = row[key + '_save']
            saving.append('{} +{}'.format(name, value))
    if saving:
        lines.append('property | Saves | ' + ', '.join(saving))

    # Skills
    skills = []
    for name, key in SKILLS:
        if key in row:
            skills.append('{} +{}'.format(name, row[key]))
    if skills:
        lines.append('property | Skills | ' + ', '.join(skills))

    # Others
    for name, key in [
        ('Damage vulnerabilities', 'damage_vulnerabilities'),
        ('Damage resistances', 'damage_resistances'),
        ('Damage immunities', 'damage_immunities'),
        ('Condition immunities', 'condition_immunities'),
        ('Senses', 'senses'),
        ('Languages', 'languages'),
    ]:
        if row.get(key):
            lines.append('property | {} | {}'.format(name, row[key]))

    if len(lines) > 0:
        lines.append('rule')
    return lines


def description(row):
    if 'description' in row:
        return [
            # 'fill | 2',
            'rule',
            'text | <i>{}</i>'.format(row['description']),
        ]
    return []


def abilities(row):
    lines = []
    for key, title in [
        ('special_abilities', ''),
        ('actions', 'Actions'),
        ('reactions', 'Reactions'),
        ('legendary_actions', 'Legendary Actions'),
    ]:
        if key in row:
            if title:
                lines.append('section | ' + title)
            for x in row[key]:
                desc = x['desc'] if isinstance(x['desc'], str) else ''.join(x['desc'])
                desc = re.sub('(<br>|\n)+', '<br>', desc)
                desc = highlight_dice(desc)
                lines.append('property | {} | {}'.format(x['name'], desc))

    return lines


def get_icon_and_colour(row):
    icon, colour = {
        'aberration':           ('suckered-tentacle', 'rebeccapurple'),
        'beast':                ('lion',              'saddlebrown'),
        'celestial':            ('angel-outfit',      'darkgoldenrod'),
        'construct':            ('robot-golem',       'slategray'),
        'dragon':               ('dragon-head',       'darkred'),
        'elemental':            ('unfriendly-fire',   'teal'),
        'fey':                  ('unicorn',           'olive'),
        'fiend':                ('imp',               'orangered'),
        'giant':                ('giant',             'steelblue'),
        'humanoid':             ('person',            'indianred'),
        'monstrosity':          ('hydra',             'darkmagenta'),
        'ooze':                 ('slime ',            'darkslategray'),
        'plant':                ('carnivorous-plant', 'darkgreen'),
        'swarm of Tiny beasts': ('hydra-shot',        'darksalmon'),
        'undead':               ('shambling-zombie',  'black'),
    }.get(row['type'], (None, None))

    if row.get('icon'):
        icon = row['icon']
    else:
        print("Using default icon for {}".format(row['name']))

    if icon is None:
        print("Can't find icon or colour for '{}'".format(row['type']))
        return 'imp-laugh', 'red'

    return icon, colour


def convert(row):
    title = row['name']
    tags = get_tags(row)

    classification = '{size} {type}'.format(**row)
    if row.get('subtype') not in (None, "", "any race"):
        classification += ' ({})'.format(row['subtype'])

    classification += cr_stats(row)

    caption = ''
    if row.get('picture'):
        caption = classification
        contents = []
    else:
        contents = ['subtitle | {}'.format(classification), 'rule']

    contents += [
        stats(row),
        'rule',
        dnd_stats(row),
        'rule',
    ] + attributes(row) + abilities(row) + [
        'fill | 2'
    ] + description(row)

    icon, colour = get_icon_and_colour(row)
    data = {
        'count': 1,
        'color': colour,
        'title': title,
        'icon': icon,
        'picture': row.get('picture', ''),
        'picture_flex_ratio': row.get('picture_flex_ratio'),
        'caption': caption,
        'contents': contents,
        'tags': tags,
    }
    if row.get('title_size'):
        data['title_size'] = row['title_size']
    return data


def write_json(data, outfile):
    # data = sorted(data, key=lambda x: x['name'])
    with open(outfile, 'w') as fh:
        json.dump(data, fh, indent=2)


def main(folder, outfile):
    data = []
    for infile in Path(folder).iterdir():
        print(infile)
        for row in load_from_file(infile):
            if include(row):
                data.append(convert(row))

    write_json(data, outfile)


if __name__ == '__main__':
    main('sources/monsters', 'monsters.json')
