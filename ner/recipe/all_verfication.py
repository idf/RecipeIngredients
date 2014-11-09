__author__ = 'Danyang'
from cross_validation import CrossValidator
import os
import re

class TotalVerifier(CrossValidator):
    def verify(self):
        RAW_FOLDER = "data"
        INPUT_FOLDER = "auto"
        OUTPUT_FOLDER = "auto-tagged-model-all"

        os.system("java -cp ../lib/ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop all.prop")
        for non_auto_file in self.file_names:
            auto_file = re.sub(r'%s'%(RAW_FOLDER), INPUT_FOLDER, non_auto_file)
            auto_file = re.sub(r'\.tsv', '.txt', auto_file)

            auto_file_tagged = re.sub(r'%s'%INPUT_FOLDER, OUTPUT_FOLDER, auto_file)
            auto_file_tagged = re.sub(r'\.txt', '-tagged.xml', auto_file_tagged)

            os.system("java -mx500m -cp ../lib/ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier\
             -loadClassifier ner-model-all.ser.gz -textFile %s -outputFormat inlineXML > %s"%(auto_file, auto_file_tagged))

    def do(self):
        self.verify()

if __name__=="__main__":
    TotalVerifier().do()

