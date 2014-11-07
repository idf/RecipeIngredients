# -*- coding: utf-8 -*-
from nltk.metrics.agreement import AnnotationTask
from brat.tools import anntoconll
import os
import io
import codecs
__author__ = 'Danyang'
class KappaRater(object):
    def __init__(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        dir1 = os.path.join(this_dir, "S4", "G1")
        dir2 = os.path.join(this_dir, "S4", "G2")
        self.annotation_task = AnnotationTask(data=self.__readfile(dir1, dir2))

    def __readfile(self, *args):
        data = []

        for i in xrange(len(args)):
            lines = self.__get_lines(args[i])
            coder = "c"+str(i+1)
            for ind, line in enumerate(lines):
                item, label = line
                d = (coder, str(ind)+"_"+item, label)
                # print d
                data.append(d)

        return data

    def __get_lines(self, dir):
        lines = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".txt"):
                    # f = open(os.path.join(root, file), 'r')
                    with io.open(os.path.join(root, file), 'r', newline='', encoding="utf-8") as f:  # keep \r\n for .ann positioning
                        print f
                        lines += anntoconll.text_to_conll_lines(f)
                        f.close()
        return lines

    def kappa(self):
        return self.annotation_task.kappa()


if __name__=="__main__":
    kappa_rater = KappaRater()
    print kappa_rater.kappa()