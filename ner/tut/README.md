#Stanford NER
The Stanford Natural Language Processing Group [official link](http://nlp.stanford.edu/software/CRF-NER.shtml)
###Training
java -cp ../lib/ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop austen.prop

###Testing
java -cp ../lib/ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -testFile jane-austen-emma-ch2.tsv

####Sample Result
```
slice   O       O
of      O       O
Mrs.    PERS    PERS
Weston  PERS    PERS
's      O       O
wedding-cake    O       O
in      O       O
their   O       O
hands   O       O
:       O       O
but     O       O
Mr.     PERS    PERS
Woodhouse       PERS    PERS
would   O       O
never   O       O
believe O       O
it      O       O
.       O       O

CRFClassifier tagged 1999 words in 1 documents at 2705.01 words per second.
         Entity P       R       F1      TP      FP      FN
           PERS 0.8205  0.7273  0.7711  32      7       12
         Totals 0.8205  0.7273  0.7711  32      7       12
```