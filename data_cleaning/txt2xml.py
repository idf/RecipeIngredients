import nltk.data
import os
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.stem.porter import *
import math

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
stemmer = PorterStemmer()

text_auto = []
text_nonauto = []

print 'Processing datat in'
directory = os.path.dirname(os.path.realpath(__file__)) + '/raw_data'
print 'dir:'+directory

for root, dirs, files in os.walk(directory):
	for file in files:	
		if file.endswith(".txt") and (not ('(1)' in file)) and (not ('-2' in file)):
			f=open(os.path.join(root,file), 'r')
			text_nonauto.append((file,f.read()))
			f.close()
		elif file.endswith(".txt"):
			f=open(os.path.join(root,file), 'r')
			text_auto.append((file,f.read()))
			f.close()

token_counters = [0,0]
type_counters = [0,0]
token_all_auto = []
token_all_nonauto = []

for ind, (video, text) in enumerate(text_nonauto):
	xml_nonauto = '[non-automatic.xml]\n<transcripts>\n'
	video = video[:(video.find('[English]'))]
	url = text[:text.strip().find('\n')]
	text = text[text.strip().find('\n'):]
	sents = sent_detector.tokenize(text.strip())
	cleaned = '<transcript'+' id=\"'+ str(ind+1)+ '\" title=\"'+video+'\" url=\"'+ url + '\" mode=\"non-automatic\">\n'
	token_count = 0
	sents_counter += len(sents)
	for s in sents:
		s = s.replace('\n',' ') +'\n'
		s = s.replace('.',' ')
		s = s.lower()
		cleaned += s
		token_count += len(PunktWordTokenizer().tokenize(s))
		temp = PunktWordTokenizer().tokenize(s)
		for t in temp:
			t = stemmer.stem(t)
			token_all_nonauto.append(t)			
	cleaned += '</transcript>\n'
	xml_nonauto+= cleaned+'</transcripts>'
	f = open('Sents_split/non_auto/'+str(ind+1)+'.txt','w')
	f.write(xml_nonauto)
	f.close()
	token_counters.append((ind+1,token_count))
	token_counters[0] += token_count
	token_all_nonauto = set(token_all_nonauto)
	type_counters[0] += len(token_all_auto)

for ind, (video, text) in enumerate(text_auto):
	xml_auto = '[automatic.xml]\n<transcripts>\n'
	video = video[:(video.find('[English]'))]
	url = text[:text.strip().find('\n')]
	text = text[text.strip().find('\n'):]
	sents = sent_detector.tokenize(text.strip())
	token_count = 0
	cleaned = '<transcript'+' id=\"'+ str(ind+1) + '\" title=\"'+video+'\" url=\"'+ url + '\" mode=\"automatic\">\n'
	for s in sents:
		s = s.replace('\n',' ') +'\n'
		s = s.replace('.',' ')
		s = s.lower()
		cleaned += s
		temp = PunktWordTokenizer().tokenize(s)
		for t in temp:
			t = stemmer.stem(t)
			token_all_auto.append(t)	
	cleaned += '</transcript>\n'
	xml_auto+= cleaned+'</transcripts>'
	f = open('Sents_split/auto/'+str(ind+1)+'.txt','w')
	f.write(xml_auto)
	f.close()
	token_counters[1] += token_count
	token_all_auto = set(token_all_auto)
	type_counters[1] += len(token_all_auto)

print token_counters