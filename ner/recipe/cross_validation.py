import os
import io
import re
__author__ = 'Danyang'
class CrossValidator(object):
    def __init__(self):
        self.directory = os.path.dirname(os.path.realpath(__file__))
        self.file_names = self.read_file_names_from_dir(os.path.join(self.directory, "data"))

    def cross_validate(self, k=4):
        """
        divide by file name
        """
        file_names = self.group_files(False, k)

        # test
        for fold in range(k): # [0, 1, 2, 3]
            print "fold=%d"%(fold+1)
            train = []
            for files in file_names[0:fold]+file_names[fold+1:]:
                for file in files:
                    train.append(file)
            test = []
            for files in file_names[fold:fold+1]:
                for file in files:
                    test.append(file)

            print "training ",
            print train
            print "testing ",
            print test

            self.combine_files(train, os.path.join(self.directory, "train.tsv"))
            self.combine_files(test, os.path.join(self.directory, "test.tsv"))
            # training & evaluation
            os.system("java -cp ../lib/ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier \
            -prop recipe.prop > fold-%d.log 2>&1"%fold)

            self.tag_files(test, 'non-auto')
            self.tag_files(test, 'auto')

    def tag_files(self, raw_tsv, input_folder_name):
        for f_input in raw_tsv:
            f_input = re.sub(r'\.tsv', '.txt', f_input)
            f_input = re.sub(r'data', input_folder_name, f_input)
            f_tagged = re.sub(r'\.txt', '-tagged.xml', f_input)
            os.system("java -mx500m -cp ../lib/ner/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier\
             -loadClassifier ner-model.ser.gz -textFile %s -outputFormat inlineXML > %s"%(f_input, f_tagged))

    def group_files(self, default=True, k=4):
        file_names = [[] for _ in xrange(k)]
        if default:
            part = len(self.file_names)/k
            for i in xrange(k):
                file_names[i] = self.file_names[i*part:(i+1)*part]
            return file_names
        else:
            # 1, 7, 15, 24
            starts = [1, 7, 15, 24, 34]
            for i in xrange(len(starts)-1):
                file_names[i] = ["data/%d.tsv"%(j) for j in xrange(starts[i], starts[i+1])]
            return file_names

    def read_file_names_from_dir(self, path):
        names = []
        print path
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".tsv"):
                    names.append(os.path.join(root, file))
        return names

    def combine_files(self, files, output_path):
        output = []
        for file in files:
            with io.open(file, 'r', newline='', encoding="utf-8") as f:
                output.append(f.read())
                f.close()

        with io.open(output_path, 'w', newline='', encoding="utf-8") as o:
            o.write("\n".join(output))
            o.close()


    def do(self):
        self.cross_validate()

if __name__=="__main__":
    v = CrossValidator()
    v.do()



