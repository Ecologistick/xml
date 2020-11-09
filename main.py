from pprint import pprint
import xml.etree.ElementTree as ET

def open_file(file):
  tree = ET.parse(file)
  return tree

def picking(tree):
  counters = {}
  for description in tree.iterfind('channel/item/description'):
    for word in description.text.lower().split():
      if len(word) < 6:
        continue
      if word not in counters:
        counters[word] = 1
      else:
        counters[word] += 1
  return counters

def top(counters):
  return sorted(counters.items(), key=lambda i: i[1], reverse=True)[:10]

pprint(top(picking(open_file('newsafr.xml'))))