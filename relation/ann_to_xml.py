# -*- coding: utf-8 -*-
# import xml.etree.cElementTree as ET

import os
import operator

class  EntityTag(object):
	"""docstring for  EntityTag"""
	def __init__(self, tag=None, start=None, end=None, content=None):
		super( EntityTag, self).__init__()
		self.tag = tag
		self.start = start
		self.end = end
		self.content = content

	def __repr__(self):
		return str((self.tag, self.start, self.end))
	def __str__(self):
		return str((self.tag, self.start, self.end))


class Relation(object):
	"""docstring for Relation"""
	def __init__(self, unit=None, ingredient=None, amount=None):
		super(Relation, self).__init__()
		self.unit = unit
		self.ingredient = ingredient
		self.amount = amount

	def __repr__(self):
		tmp = ""
		if self.amount:
			tmp = tmp + self.amount+" "
		if self.unit:
			tmp = tmp + self.unit + " of "
		tmp += self.ingredient
		return tmp

	def __str__(self):
		tmp = ""
		if self.amount:
			tmp = tmp + self.amount+" "
		if self.unit:
			tmp = tmp + self.unit + " of "	
		tmp += self.ingredient
		return tmp

	def add(self, type, part1, part2, tag_index_dict):
		ingredient_index = part2.split(":")[-1]
		self.ingredient = tag_index_dict.get(ingredient_index)
		part1_index = part1.split(":")[-1] 
		part1_content = tag_index_dict.get(part1_index)
		if type == "Quantify":
			self.amount = part1_content
		elif type == "Measure":
			self.unit = part1_content
		pass
	
def ann_to_xml(ann_entities, xml_path, txt_path):
	import codecs

	txt_file = codecs.open(txt_path,'r','utf-8')
	txt_raw = txt_file.read()
	txt_file.close()
	xml_file = codecs.open(xml_path, "w+",'utf-8')

	tags = []
	relations_dict = {}
	tag_index_dict = {}
	for ann_entity in ann_entities:
	
		if ann_entity.startswith("T"):
			tag_index, annotation, tagged_text= ann_entity.strip().split("\t")
			tag, tmp = annotation.split(" ", 1)
			tmp = tmp.split(" ")
			start = int(tmp[0])
			end = int(tmp[-1])
			
			try:
				assert tagged_text.strip() == txt_raw[start:end].replace("\n", " ").strip()
			except AssertionError:
				print "Something Wront with entity: " + ann_entity
				print tagged_text.strip() 
				print txt_raw[start:end].replace("\n", " ").strip()

			tag_entity = EntityTag(tag, start, end, tagged_text)
			tags.append(tag_entity)

			tag_index_dict[tag_index] = tagged_text

		elif ann_entity.startswith("R"):

			relation_index, annotation = ann_entity.strip().split("\t")
			rel_type, part1, part2 = annotation.split(" ")
			ingredient_index = part2.split(":")[-1]
			relation = relations_dict.get(ingredient_index, Relation())
			relation.add(rel_type, part1, part2, tag_index_dict)
			relations_dict[ingredient_index] = relation
	tags.sort(key=operator.attrgetter('start'), reverse=True)
	
	ner_tpl = "<entity type=\"%s\">%s</entity>"
	for tag in tags:
		txt_raw = txt_raw[:tag.start]+ ner_tpl % (tag.tag, txt_raw[tag.start:tag.end]) + txt_raw[tag.end:]

	xml_file.write(txt_raw)
	xml_file.close()
	# print "Relations: %s" % str(relations_dict)
	# print "write in "+xml_path+" successfully"

	return relations_dict

def format_directory(top):

	for root, dirs, files in os.walk(top):
		for file_name in files:
			if file_name.endswith(".ann"):
				
				format_file(os.path.join(root, file_name))		

def format_file(file_path):
	
	# print "Converting "+ file_path

	# dir_name = os.path.dirname(file_path)
	# file_name = os.path.basename(file_path)
	import codecs
	ann_file = codecs.open(file_path, 'r',"utf-8")
	ann_entities = [line for line in ann_file]
	ann_file.close()

	xml_path = file_path.replace(".ann", ".xml")
	txt_path = file_path.replace(".ann", ".txt")
	return ann_to_xml(ann_entities, xml_path, txt_path)

def get_relation_set(file_path):
	relation_all = format_file(file_path)
	result_set = set()
	for _, relation in relation_all.items():
		relation_dict = dict()
		if relation.ingredient:
			relation_dict["ingredient"] = relation.ingredient
		if relation.unit:
			relation_dict["unit"] = relation.unit
		if relation.amount:
			relation_dict["amount"] = relation.amount
		result_set.add(str(relation_dict))
	return result_set

if __name__ == '__main__':
	current_directory = os.path.dirname(os.path.realpath(__file__))
	format_directory(current_directory)
	# get_relation_set(os.path.join(current_directory,"non-auto","1.ann"))
