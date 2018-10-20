import re
import yaml
import json
import random

from collections import OrderedDict
from pathlib import Path


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


def highlight_dice(x):
    return re.sub(r'(\d+d\d+( ?[+-] ?\d+)?)', r'<b>\1</b>', x)


def tostring(x):
    if isinstance(x, list):
        x = '<br>'.join(x)
    x = x.replace('\n\n', '<br>')
    return highlight_dice(x)


def to_text_blocks(x):
    if not isinstance(x, list):
        x = [x]

    lines = []
    for line in x:
        lines += line.split('\n\n')

    output = []
    for line in lines:
        line = highlight_dice(line)
        if re.match(r'^[a-z]+ \| ', line):
            output.append(line)
        else:
            output.append('text | {}'.format(line))

    return output


def load_from_file(filename):
    with open(filename, encoding='utf-8') as fh:
        return yaml.load(fh)


def load_from_path(folder):
    for infile in Path(folder).iterdir():
        for row in load_from_file(infile):
            yield row


def write_json(data, outfile):
    # data = sorted(data, key=lambda x: x['name'])
    with open(outfile, 'w') as fh:
        json.dump(data, fh, indent=2)


def randomlist(folder, number, callable_filter=None, **filters):
    items = []
    for row in load_from_path(folder):
        if callable_filter and not callable_filter(row):
            continue
        for k, v in filters.items():
            if row.get(k) != v:
                break
        else:
            items.append(row)

    results = []
    for _ in range(number):
        index = random.randint(0, len(items) - 1)
        item = items[index]
        del items[index]
        print(item['name'])
        results.append(item['name'])
    return results
