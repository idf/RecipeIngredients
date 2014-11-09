#Recipe Ingredients
---

###Description 

For CZ4045 Natural Language Processing Project
Nanyang Technological University  
Instructor: [Prof Kim Jung-Jae](http://www.ntu.edu.sg/home/jungjae.kim/Home/Home.html)

The purpose of this project is to build a system that could automatically recognize meaningful entities in cooking tutorial videos (including recipe names, ingredients and amounts and units), as well as the relationship between quantities, units and ingredients; the trained model can be later adopted to build applications to automatically generate recipe summary from videos, and hence to support decision making of rookie home chefs.

The whole system is powered by NLTK, Stanford NLP SDK and Brat.
###Requirements:
* Python 2.7+
* JDK 1.7+
* [NLTK 3.0](http://www.nltk.org/)
* [Stanford Named Entity Recognizer (NER)](http://nlp.stanford.edu/software/CRF-NER.shtml)
* [BRAT](http://brat.nlplab.org/index.html)

####Line encoding
Unix `\n`

###BRAT
Some changes are directly made to the BRAT source code compared to the [original code](https://github.com/nlplab/brat)
Please install the brat first, then use the code inside *brat* folder to overide responding files.

###Usage 
Clone the repo

    $ git clone https://github.com/zhangdanyangg/RecipeIngredients.git

###License##
This project is released under MIT License.
#Data Cleaning
---

###Purpose
Remove the time stamps from the downloaded scripts (srt files) and generate xml files according to the format in project manual
Make sure the following folders exist:
Sents_split/non_auto/
Sents_split/auto/

###To Run
Under current directory:
```bash
python removeTime.py
python txt2xml.py
```
#Brat rapid annotation tool (Brat)
---

Source code of brat are changed to facilitate conversion between brat standalone annotation `.ann` format to CoNLL format. 

###Change log
Changed tools/anntoconll.py  
Changed tools/sentencesplit.py  
Please ensure that you have entire local copy of [brat](https://github.com/nlplab/brat)  

###Run
```bash
python .tools/annotconll.py path_to_annotated_txt_file
```
#Cohen's kappa
---

[Cohen's kappa](http://en.wikipedia.org/wiki/Cohen's_kappa) is used to measure the Inter-Annotator Agreement for data subset S2, S3, S4
###Data
Ensure `.txt` and `.ann` are in the folder of G1, G2 under S2, S3, S4 respectively
###To run
```bash
python kappa.py
```
#Named Entity Recognition Model
---

###Run Cross Validation
```bash
python cross_validation.py
```

###Model Evaluation
fold 1:
```
CRFClassifier tagged 13058 words in 1 documents at 9545.32 words per second.
         Entity	P	R	F1	TP	FP	FN
         Amount	0.7662	0.7195	0.7421	59	18	23
     Ingredient	0.7718	0.6370	0.6979	186	55	106
         Recipe	0.0000	0.0000	0.0000	0	1	46
           Unit	0.7826	0.8571	0.8182	36	10	6
         Totals	0.7699	0.6082	0.6796	281	84	181
```
fold 2:
```
CRFClassifier tagged 16499 words in 1 documents at 9797.51 words per second.
         Entity	P	R	F1	TP	FP	FN
         Amount	0.8214	0.6479	0.7244	92	20	50
     Ingredient	0.7103	0.7143	0.7123	255	104	102
         Recipe	0.0000	0.0000	0.0000	0	1	26
           Unit	0.7846	0.6711	0.7234	51	14	25
         Totals	0.7412	0.6622	0.6995	398	139	203
```
fold 3:
```
CRFClassifier tagged 16997 words in 1 documents at 8969.39 words per second.
         Entity	P	R	F1	TP	FP	FN
         Amount	0.7823	0.6258	0.6953	97	27	58
     Ingredient	0.8114	0.5921	0.6847	241	56	166
         Recipe	0.0000	0.0000	0.0000	0	1	23
           Unit	0.9175	0.7542	0.8279	89	8	29
         Totals	0.8227	0.6074	0.6989	427	92	276
```
fold 4:
```
CRFClassifier tagged 13988 words in 1 documents at 9018.70 words per second.
         Entity	P	R	F1	TP	FP	FN
         Amount	0.8765	0.5504	0.6762	71	10	58
     Ingredient	0.8186	0.5774	0.6771	194	43	142
         Recipe	0.0000	0.0000	0.0000	0	2	46
           Unit	0.9245	0.7903	0.8522	49	4	13
         Totals	0.8418	0.5480	0.6638	314	59	259
```


###Tag new files
```bash
java -mx500m -cp ../lib/ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -textFile auto/1.txt -outputFormat inlineXML > auto/1-tagged.xml
```
#Automatic Prediction & Comparison
---

###Purpose
To compare the predicted tags (xml files) and the manually tagged files (ann files).
All files to be compared must be in folder 'auto-tagged'.
Files on the same video must have the same name.

###To Use
```bash
python xml_ann_comparator.py
```
#Entity Relationship Identification Model
---

This model is to identify the relationship among entities. 

After NER system tagged the entity name on the scripts, the relation between the entities could be extracted. For this recipe case, the amount of entities could be extracted from the tagged script.

This model contains three modules:
* ann_to_xml.py : Convert .ann file and responding text file into xml document
* info_extraction.py : Extract relation and entities sets from xml document.
* relation_evaluate.py : Evaluate the relation extractor.
 
There are three data folders:
* non-auto/ : Non-auto transcript tagged by human using brat
* ner-tagged/ : Non-auto tagged by NER system
* auto/ : Auto transcript tagged by NER system

###Usage
To generate evaluation result 
```
$ python relation_evaluate.py [data folder name]
```

###Method
Regular expression is used to extract the amount relation. There are several rules to find a relation: 
####Rules
```
<amount><ingredient>
<amount>[some description words without tag ]<ingredient>
<amount><unit><ingredient>
<amount>[some description words without tag ]<unit><ingredient>
<amount><unit>[some description words without tag ]<ingredient>
<amount>[some description words without tag ]<unit>[some description words without tag ]<ingredient>
<amount>[some other ingredient]<ingredient>
<amount><unit>[some other ingredient ]<ingredient>
```
####Coded Rules
```
<Amount>(?P<amount>[^<]+)</Amount>[^<]{0,70}(<Ingredient>[^<]+</Ingredient>)*<Ingredient>(?P<ingredient>[^<]+)</Ingredient>

<Amount>(?P<amount>[^<]+)</Amount>[^<]{0,70}<Unit>(?P<unit>[^<]+)</Unit>[^<]{0,70}(<Ingredient>[^<]+</Ingredient>)*<Ingredient>(?P<ingredient>[^<]+)</Ingredient>
```
