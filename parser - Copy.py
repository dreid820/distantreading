from lxml import etree as ET
import csv
import os

file = open("E:/masters/master1800tagged.xml", "r", encoding="utf-8")

tree = ET.parse(file)
root = tree.getroot()
iter_ = tree.getiterator()
iter_1 = tree.getiterator()


for elem in iter_1:

	if elem.tag == "title":
		if elem.get('dataset') != None:
			for child in elem:
				if child.tag == "author":
					print(child.text)

				"""if child.tag == "date":
					print(child.text)"""

		
	"""if elem.tag == "term":
		if elem.get('subject') != None:
			if elem.getparent().getparent().getprevious() != None:
				current_year = elem.getparent().getparent().getprevious()
				subject = elem.get('subject')
				f = open(current_year.text + " - subjects.txt", "a", encoding="utf-8")
				f.write(subject + ', ')
				f.close()

	if elem.tag == "term":
		if elem.get('location') != None:
			if elem.getparent().getparent().getprevious() != None:
				current_year = elem.getparent().getparent().getprevious()
				location = elem.get('location')
				f = open(current_year.text + " - locations.txt", "a", encoding="utf-8")
				f.write(location + ', ')
				f.close()"""