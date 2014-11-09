import ann_to_xml
import info_extraction 

import os
import sys

def relation_evaluate(file_path):
	global tp, fp, fn
	set_original = ann_to_xml.get_relation_set(file_path+".ann")
	extract_engine = info_extraction.InfoExtraction()
	set_extracted = extract_engine.extract_file(file_path+"-tagged.xml", "relation")
	# print "****** Precessing %s *******" % file_path
	# print "Number of relations in source file: %d" % len(set_original)
	# print "Number of relations extracted: %d" % len(set_extracted)
	# print "Number of correct relation: %d" % len(set_original.intersection(set_original, set_extracted))

	# # print set_original
	# # print set_extracted
	# print set_original- set_extracted
	# print set_extracted - set_original

	tp += len(set_original.intersection(set_original, set_extracted))
	fp += len(set_extracted - set_original)
	fn += len(set_original - set_extracted)

if __name__ == '__main__':
	if len(sys.argv)==1:
		print "usage: python relation_evaluate.py [data_folder relative name]"
		print "example: python relative_evaluate.py non-auto"
		sys.exit(0)
	else:
		folder_name = sys.argv[1]
	tp = fp = fn = 0

	current_directory = os.path.dirname(os.path.realpath(__file__))
	# format_directory(current_directory)
	for i in range(1,33):
		# relation_evaluate(os.path.join(current_directory,"ner-tagged",str(i)))
		relation_evaluate(os.path.join(current_directory, folder_name, str(i)))

	print "******summary*********"
	print "tp: %d\nfp: %d\nfn: %d" % (tp, fp, fn)
	print "f1: %f" % (float(2*tp)/(2*tp+fp+fn))
	print "recall: %f" % (float(tp)/(tp+fn))