root=$(cat README.md)
brat=$(cat brat/README.md)
auto_pre=$(cat automatic_prediction/README.md)
cleaning=$(cat data_cleaning/README.md)
kappa=$(cat kappa/README.md)
ner=$(cat ner/recipe/README.md)
relation=$(cat relation/README.md)

rm report.md
echo "${root}" >> report.md
echo "${brat}"  >> report.md
echo "${cleaning}" >> report.md
echo "${kappa}" >> report.md
echo "${ner}" >> report.md
echo "${auto_pre}" >> report.md
echo "${relation}" >> report.md

