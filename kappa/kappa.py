from nltk.metrics.agreement import AnnotationTask
import re
import os
class KappaRater(object):
    def __init__(self):
        dir1 = ""
        dir2 = ""
        self.annotation_task = AnnotationTask(data=self.__readfile(dir1, dir2))

    def __readfile(self, *args):
        data = []

        for i in xrange(len(args)):
            lines = self.__get_lines(args[i])
            coder = "c"+str(i+1)
            for ind, line in enumerate(lines):
                item, label = line.split(" ")
                data.append((coder, str(ind), label))

        return data

    def __get_lines(self, dir):
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".txt"):
                    f = open(os.path.join(root, file), 'r')

                    f.close()

    def kappa(self):
        return self.annotation_task.kappa()