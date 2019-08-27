import glob
import os
import random
import re
import nltk
from lxml import etree as ET
from itertools import chain

#Establish the xml tree for the master_list
xml_root_compiled = ET.Element('master_list')
xml_tree_compiled = ET.ElementTree(xml_root_compiled)

#Set-up a flag to give each transformed book a number. This is unnecessary, but might prove useful someday.
title_flag = 0

#Open every metadata file in the source directory. Metadata files are housed up one level from the book files, so I had to specifically target those subdirectories.
for filename in glob.iglob(os.path.join(r'E:/randomized_files_1850-59', '*', '*')):
	if filename.endswith('.xml'):
		
		#Establish the xml tree for each book.
		xml_root = ET.Element('book')
		xml_tree = ET.ElementTree(xml_root)

		#Create a list that will hold all words from each page file.
		page = []

		#Define the three variables that will be used as metadata.
		title = None
		author = None
		date = None

		#Open and parse through each metadata xml file using ElementTree.
		alto = os.path.dirname(filename)
		tree = ET.parse(filename)
		root = tree.getroot()
		iter_ = tree.getiterator()

		#Look through every element in the xml files to find the title, author, and publication date, and create subelements of them in the book xml tree.
		for elem in iter_:
			if elem.tag == "{http://www.loc.gov/mods/v3}title":
				title_flag += 1
				title = elem.text
				book_title = ET.SubElement(xml_root, "title", number=str(title_flag))
				book_title.text = title
				break
		for elem in iter_:
			if elem.tag == "{http://www.loc.gov/mods/v3}namePart":
				dirty_author = elem.text
				#The author is being use to name the document, so I had to strip all characters that cannout be used in a Windows file name.
				PATTERN = r'[<|>|:|/|\\|?\|*\|"|#|$|%|&|+|]'
				author = re.sub(PATTERN, r'', dirty_author)
				book_author = ET.SubElement(xml_root, "author")
				book_author.text = author
				break
		for elem in iter_:
			if elem.tag == "{http://www.loc.gov/mods/v3}dateIssued":
				date = elem.text
				book_date = ET.SubElement(xml_root, "date")
				book_date.text = date
				break

		#Now that the metadata has been collected, go one level deeper to open the book files.	
		for other_filename in glob.iglob(os.path.join(alto, '*', '*.xml')):
				#Open and parse through the book files using Elementree.
				tree = ET.parse(other_filename)
				root = tree.getroot()
				
				#The text of the book files is located in a child element labeled "CONTENT". So search through the child elements until "CONTENT" is located, and append the text in that element to the page list. At the end of this loop, the page list will contain all the words in the book.
				for child in root:
					if child.tag == "Layout":
						for child_1 in child:
		
		
							if "ID" in child_1.attrib:
								print(child_1.attrib["ID"])
					
								for child_2 in child_1:
									for child_3 in child_2:
										for child_4 in child_3:
											for child_5 in child_4:
				
												if "CONTENT" in child_5.attrib:
											

													page.append(child_5.attrib["CONTENT"] + " ")
														
		#Since this is only a digitally-assisted project and I will be reading through the data myself, I decided not to do a full clean of the data. I also had a difficult time with regex. However, I tried to clean up characters that were causing me issues.	
		book_pages = ET.SubElement(xml_root, 'book_pages')
		dirty_content = ("".join(list(chain.from_iterable(page))))
			
		dirty_content = dirty_content.replace(" - ", "")
		dirty_content = dirty_content.replace("- ", "")
		dirty_content = dirty_content.replace(" -", " ")
		dirty_content = dirty_content.replace(",", ";")
		dirty_content = dirty_content.replace("Av", "w")
		dirty_content = dirty_content.replace("&quot;", '')
		dirty_content = dirty_content.replace("&amp;", "and")
		dirty_content = dirty_content.replace("&#8212;", "-")
		dirty_content = dirty_content.replace("&#187;", "-")
		dirty_content = dirty_content.replace("&#171;", "-")

		PATTERN = r'[<|>|/|\\|*|#|$|%|+|]'
		content = re.sub(PATTERN, r'', dirty_content)


	


		#Use the Natural Language Tool Kit to tokenize the books into sentences.
		default_st = nltk.sent_tokenize
		corpus_sentences = default_st(text=content)
		corpus = iter(corpus_sentences)

		#Create a flag to number each line in a book, so that, when taken out of context, a line can easily be relocated.
		line_number = 1
		
		#Create a list to hold all the tokenized lines. This is how was able to pull the line before and the line after any line with my keywords in it. By appending all lines to a list, I could retreive the previous line (lines[-2]) and the next line (next(corpus)).
		lines = []

		#For every tokenized line in each book:
		for line in corpus:
			#Increase line_number flag.
			line_number += 1
			#Create a subelement in the book xml file.
			book_lines = ET.SubElement(book_pages, 'tokenized_line-' + str(line_number))
			book_lines.text = line
			lines.append(line)

			#If one of the keywords is in the line, create a subelement in the master xml file with the title, author, date, and the line plus the preceding and proceding lines.
			if "civilizing" in line: 
				book_title_compiled = ET.SubElement(xml_root_compiled, "title")
				book_title_compiled.text = title
				book_author_compiled = ET.SubElement(book_title_compiled, "author")
				book_author_compiled.text = author
				book_date_compiled = ET.SubElement(book_title_compiled, "date")
				book_date_compiled.text = date
				book_pages_compiled = ET.SubElement(book_title_compiled, 'book_pages')
				book_lines_compiled = ET.SubElement(book_pages_compiled, 'tokenized_line-' + str(line_number))
				book_lines_compiled.text = lines[-2] + line + next(corpus)
			elif "civilization" in line: 
				book_title_compiled = ET.SubElement(xml_root_compiled, "title")
				book_title_compiled.text = title
				book_author_compiled = ET.SubElement(book_title_compiled, "author")
				book_author_compiled.text = author
				book_date_compiled = ET.SubElement(book_title_compiled, "date")
				book_date_compiled.text = date
				book_pages_compiled = ET.SubElement(book_title_compiled, 'book_pages')
				book_lines_compiled = ET.SubElement(book_pages_compiled, 'tokenized_line-' + str(line_number))
				book_lines_compiled.text = lines[-2] + line + next(corpus)
			elif "civilized" in line: 
				book_title_compiled = ET.SubElement(xml_root_compiled, "title")
				book_title_compiled.text = title
				book_author_compiled = ET.SubElement(book_title_compiled, "author")
				book_author_compiled.text = author
				book_date_compiled = ET.SubElement(book_title_compiled, "date")
				book_date_compiled.text = date
				book_pages_compiled = ET.SubElement(book_title_compiled, 'book_pages')
				book_lines_compiled = ET.SubElement(book_pages_compiled, 'tokenized_line-' + str(line_number))
				book_lines_compiled.text = lines[-2] + line + next(corpus)
				


		#Write the book xml file.	 
		xml_tree.write(str(author) + '.xml', encoding="utf-8", xml_declaration=True, pretty_print=True)

#Write the master xml file.
xml_tree_compiled.write('master1850.xml', encoding="utf-8", xml_declaration=True, pretty_print=True)
