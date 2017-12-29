#!/usr/bin/env python

import csv
import json
import re


def load_csv(filename):
    with open(filename, newline='') as fh:
        reader = csv.DictReader(fh, delimiter=';')
        for row in reader:
            yield row


def convert_description(description):
    lines = []
    m = re.match(r'\(([^)]+)\)(.*)', description)
    if m:
        materials = m.group(1)
        lines.append('text | <i>{}</i>'.format(m.group(1)))
        description = m.group(2)

    description = description.replace('\u00e2\u20ac\u00a2', '\u2022')
    for line in description.split('<br>'):
        lines.append('text | {}'.format(line.strip()))

    lines.append('fill | 3')

    return lines


def convert(row):
    tags = ['spell']
    for c in ['Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorcerer', 'Warlock', 'Wizard', 'XGE', 'SCAG']:
        if row[c]:
            tags.append(c.lower())

    contents = [
        'subtitle | {}'.format(row['Type']),
        'rule',
        'property | Casting time | {}'.format(row['Casting time']),
        'property | Range | {}'.format(row['Range']),
        'property | Components |  {}'.format(row['Components'].replace(' ', '')),
        'rule',
        'fill | 2',
    ] + convert_description(row['Description'])
    
    
    # 'section | At higher levels',
            # 'text | +1d6 damage for each slot above 1st'
    return {
        'count': 1,
        'color': 'maroon',
        'title': row['Name'],
        'icon': 'white-book-1',
        'icon_back': 'robe',
        'contents': contents,
        'tags': tags,
    }


def write_json(data, outfile):
    data = sorted(data, key=lambda x: x['title'])
    with open(outfile, 'w') as fh:
        json.dump(data, fh, indent=2)


def main(infile, outfile):
    data = []
    for row in load_csv(infile):
        data.append(convert(row))

    write_json(data, outfile)


if __name__ == '__main__':
    main('spells.csv', 'spells.json')
