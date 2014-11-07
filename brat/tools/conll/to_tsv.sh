cd ..
n=$((1))
while [ $(($n < 34)) == 1 ]; do
  python anntoconll.py -o .tsv conll/$n.txt
  n=$(($n + 1))
done