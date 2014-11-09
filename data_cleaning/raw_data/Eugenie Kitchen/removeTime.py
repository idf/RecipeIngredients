import re
import os

texts = []

directory = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(directory):
	for file in files:
		if file.endswith(".srt"):
			f=open(os.path.join(root,file), 'r')
			texts.append((file,f.read()))
			f.close()

p1 = re.compile(('^\d+$'))
p2 = re.compile(('\d\d:\d\d:\d\d'))

for videoName, videoTexts in texts:
	transcripts = ''
	lines = videoTexts.splitlines()
	for line in lines:
		if not (p1.search(line) or p2.search(line) or len(line) < 1):
			transcripts += (line+'\n')
	f = open(videoName[:len(videoName)-4]+'_cleaned.txt','w')
	f.write(transcripts)
	print(videoName + ' has been cleaned.')
	f.close()

#fileName = 'Jelly Roll Ice Cream Bombe Recipe - Laura Vitale - Laura in the Kitchen Episode 790 [English]-4.txt'

# # f = open(fileName,'r')

# p1 = re.compile(('^\d+$'))
# p2 = re.compile(('\d\d:\d\d:\d\d'))

# transcripts = ''

# # text = f.read().splitlines()
# # f.close()

# for line in text:
# 	if not(p1.search(line) or p2.search(line) or len(line) < 1):
# 		transcripts+=(line+'\n')

# f2 = open(fileName+'-cleaned.txt','a')
# f2.write(transcripts)
# f2.close()