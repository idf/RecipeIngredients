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
directory = os.path.dirname(os.path.realpath(__file__)) + '/raw_data/cleaned'
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

if not os.path.exists('Sents_split/non_auto/'):
    os.makedirs('Sents_split/non_auto/')
if not os.path.exists('Sents_split/auto/'):
    os.makedirs('Sents_split/auto/')   

for ind, (video, text) in enumerate(text_nonauto):
	xml_nonauto = '[non-automatic.xml]\n<transcripts>\n'
	video = video[:(video.find('[English]'))]
	url = text[:text.strip().find('\n')]
	text = text[text.strip().find('\n'):]
	sents = sent_detector.tokenize(text.strip())
	cleaned = '<transcript'+' id=\"'+ str(ind+1)+ '\" title=\"'+video+'\" url=\"'+ url + '\" mode=\"non-automatic\">\n'
	for s in sents:
		s = s.replace('\n',' ') +'\n'
		s = s.replace('.',' ')
		s = s.lower()
		cleaned += s
		temp = PunktWordTokenizer().tokenize(s)		
	cleaned += '</transcript>\n'
	xml_nonauto+= cleaned+'</transcripts>'
	f = open('Sents_split/non_auto/'+str(ind+1)+'.txt','w')
	f.write(xml_nonauto)
	f.close()

for ind, (video, text) in enumerate(text_auto):
	xml_auto = '[automatic.xml]\n<transcripts>\n'
	video = video[:(video.find('[English]'))]
	url = text[:text.strip().find('\n')]
	text = text[text.strip().find('\n'):]
	sents = sent_detector.tokenize(text.strip())
	cleaned = '<transcript'+' id=\"'+ str(ind+1) + '\" title=\"'+video+'\" url=\"'+ url + '\" mode=\"automatic\">\n'
	for s in sents:
		s = s.replace('\n',' ') +'\n'
		s = s.replace('.',' ')
		s = s.lower()
		cleaned += s
	cleaned += '</transcript>\n'
	xml_auto+= cleaned+'</transcripts>'
	f = open('Sents_split/auto/'+str(ind+1)+'.txt','w')
	f.write(xml_auto)
	f.close()