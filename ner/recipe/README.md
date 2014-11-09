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