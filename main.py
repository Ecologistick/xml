from pprint import pprint
import xml.etree.ElementTree as ET

def open_file(file):
  tree = ET.parse(file)
  return tree

def picking(tree):
  min_word = int(input('Введите минимальный размер слова: '))
  counters = {}
  for description in tree.iterfind('channel/item/description'):
    for word in description.text.lower().split():
      if len(word) < min_word:
        continue
      if word not in counters:
        counters[word] = 1
      else:
        counters[word] += 1
  return counters

def top(counters):
  top_size = int(input('Введите размер топа: '))
  return sorted(counters.items(), key=lambda i: i[1], reverse=True)[:top_size]

pprint(top(picking(open_file('newsafr.xml'))))