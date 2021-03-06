Caution - the command should be executed under this director, `PROJECT/ner/recipe/model_tuning

##Gazettee
###Without Gazette
```bash
java -cp ../../lib/ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop without_Gazette.prop
```

Result

```
CRFClassifier tagged 13988 words in 1 documents at 6247.43 words per second.
         Entity P       R       F1      TP      FP      FN
         Amount 0.8831  0.5271  0.6602  68      9       61
     Ingredient 0.8585  0.5238  0.6506  176     29      160
           Unit 0.9245  0.7903  0.8522  49      4       13
         Totals 0.8746  0.5113  0.6454  293     42      280
```
###With Gazette
```bash
java -cp ../../lib/ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop original.prop
```

Result

```
CRFClassifier tagged 13988 words in 1 documents at 2210.84 words per second.
         Entity P       R       F1      TP      FP      FN
         Amount 0.8765  0.5504  0.6762  71      10      58
     Ingredient 0.8186  0.5774  0.6771  194     43      142
         Recipe 0.0000  0.0000  0.0000  0       2       46
           Unit 0.9245  0.7903  0.8522  49      4       13
         Totals 0.8418  0.5480  0.6638  314     59      259
```


##Word Shape
###Without Disabling Word Shape
```bash
java -cp ../../lib/ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop without_disabling_word_feature.prop
```

Result

```
CRFClassifier tagged 13988 words in 1 documents at 5227.20 words per second.
         Entity P       R       F1      TP      FP      FN
         Amount 0.8571  0.5581  0.6761  72      12      57
     Ingredient 0.8059  0.5685  0.6667  191     46      145
         Recipe 0.0000  0.0000  0.0000  0       1       46
           Unit 0.8889  0.7742  0.8276  48      6       14
         Totals 0.8271  0.5428  0.6554  311     65      262
```
###With Disabling Word Shape
```bash
java -cp ../../lib/ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop original.prop
```

Result

```
CRFClassifier tagged 13988 words in 1 documents at 2210.84 words per second.
         Entity P       R       F1      TP      FP      FN
         Amount 0.8765  0.5504  0.6762  71      10      58
     Ingredient 0.8186  0.5774  0.6771  194     43      142
         Recipe 0.0000  0.0000  0.0000  0       2       46
           Unit 0.9245  0.7903  0.8522  49      4       13
         Totals 0.8418  0.5480  0.6638  314     59      259
```

