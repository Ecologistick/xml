from pprint import pprint
import xml.etree.ElementTree as ET
def top(file):
  tree = ET.parse(file)
  counters = {}
  for description in tree.iterfind('channel/item/description'):
    for word in description.text.lower().split():
      if len(word) < 6:
        continue
      if word not in counters:
        counters[word] = 1
      else:
        counters[word] += 1
  return sorted(counters.items(), key=lambda i: i[1], reverse=True)[:10]

pprint(top('newsafr.xml'))