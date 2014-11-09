# -*- coding: utf-8 -*-

import os
import re

class InfoExtraction(object):
	def __init__(self):
		self.p_amount = "<Amount>(?P<amount>[^<]+)</Amount>"
		self.p_ingredient = "<Ingredient>(?P<ingredient>[^<]+)</Ingredient>"
		self.p_unit = "<Unit>(?P<unit>[^<]+)</Unit>"
		self.p_recipe = "<Recipe>(?P<recipe>[^<]+)</Recipe>"

	def extract_directory(self, top, func_name, callback=None):

		for root, dirs, files in os.walk(top):
			for file_name in files:
				if file_name.endswith(".xml"):
					if not callback:
						self.extract_file(os.path.join(root, file_name), func_name)		
					else:
						callback(self.extract_file(os.path.join(root, file_name), func_name))
	def extract_file(self, file_path, func_name):
		# func_name in [set, relation]

		# print "Converting %s for %s" % (file_path, func_name) 

		# dir_name = os.path.dirname(file_path)
		# file_name = os.path.basename(file_path)
		import codecs
		with codecs.open(file_path, 'r') as tagged_file:
			content = tagged_file.read()
		content = self.pre_format(content)
		if func_name=="relation":
			return self.extract_relation(content)
		elif func_name=="set":
			return self.extract_set(content)
		else:
			print "Error: func_name should one from [set, relation"

	def extract_relation(self, content):
		
		# print "asdf", content
		p1 = re.compile("[^<]{0,50}".join([self.p_amount, self.p_ingredient]))
		p2 = re.compile("[^<]{0,50}".join([self.p_amount, self.p_unit, self.p_ingredient]))
		p3 = re.compile("[^<]{0,10}".join([self.p_amount, "<Ingredient>([^<]+)</Ingredient>[^<]", self.p_ingredient]))
		p4 = re.compile("[^<]{0,10}".join([self.p_amount, "<Ingredient>([^<]+)</Ingredient>[^<]","<Ingredient>([^<]+)</Ingredient>[^<]", self.p_ingredient]))
		p5 = re.compile("[^<]{0,10}".join([self.p_amount, "<Ingredient>([^<]+)</Ingredient>[^<]","<Ingredient>([^<]+)</Ingredient>[^<]","<Ingredient>([^<]+)</Ingredient>[^<]", self.p_ingredient]))
		p6 = re.compile("[^<]{0,10}".join([self.p_amount, self.p_unit,"<Ingredient>([^<]+)</Ingredient>[^<]", self.p_ingredient]))
		p7 = re.compile("[^<]{0,10}".join([self.p_amount, self.p_unit,"<Ingredient>([^<]+)</Ingredient>[^<]","<Ingredient>([^<]+)</Ingredient>[^<]", self.p_ingredient]))
		p8 = re.compile("[^<]{0,10}".join([self.p_amount, self.p_unit,"<Ingredient>([^<]+)</Ingredient>[^<]","<Ingredient>([^<]+)</Ingredient>[^<]","<Ingredient>([^<]+)</Ingredient>[^<]", self.p_ingredient]))
		# p3 = re.compile(" ".join([p_amount, p_unit, "of", p_ingredient]))

		patterns = [p1,p2,p3,p4,p5,p6,p7,p8]
		result_set = set()
		
		for p in patterns:
			mg = p.finditer(content.decode("utf-8"))
			for m in mg:
				# print m.string
				# print str(m.groupdict()).decode("utf-8")
				result_set.add(str(m.groupdict()).decode("utf-8"))

		return result_set


	def extract_set(self, content):
		tag_regex = dict()
		tag_regex['recipe']=re.compile(self.p_recipe)
		tag_regex['ingredient']=re.compile(self.p_ingredient)
		tag_regex['unit']=re.compile(self.p_unit)
		tag_regex['amount']=re.compile(self.p_amount)
		set_group = dict()
		
		for tag,tag_re in tag_regex.items():
			result = tag_re.findall(content)
			set_group[tag] = set(result)
		return set_group

	def pre_format(self, content):

		#for non-auto
		content = re.sub("<entity type=\"(\w+)\">([^<]+)</entity>", "<\g<1>>\g<2></\g<1>>", content)
		#for auto 
		content = content.replace("<s>", "")
		content = content.replace("</B-Ingredient> <I-Ingredient>", " ")
		content = content.replace("</I-Ingredient> <I-Ingredient>", " ")
		content = content.replace("</B-Recipe> <I-Recipe>", " ")
		content = content.replace("</I-Recipe> <I-Recipe>", " ")
		content = content.replace("</B-Amount> <I-Amount>", " ")
		content = content.replace("</I-Amount> <I-Amount>", " ")
		content = content.replace("</B-Unit> <I-Unit>", " ")
		content = content.replace("</I-Unit> <I-Unit>", " ")
		content = content.replace("</I-", "</")
		content = content.replace("</B-", "</")
		content = content.replace("<B-", "<")
		content = content.replace("<I-", "<")

		return content


if __name__ == '__main__':
	info_extraction = InfoExtraction()
	current_directory = os.path.dirname(os.path.realpath(__file__))
	current_directory = os.path.join(current_directory)
	info_extraction.extract_directory(current_directory, "relation")