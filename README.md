#Recipe Ingredients
---

###Description 

For CZ4045 Natural Language Processing Project
Nanyang Technological University  
Instructor: [Prof Kim Jung-Jae](http://www.ntu.edu.sg/home/jungjae.kim/Home/Home.html)

The purpose of this project is to build a system that could automatically recognize meaningful entities in cooking tutorial videos (including recipe names, ingredients and amounts and units), as well as the relationship between quantities, units and ingredients; the trained model can be later adopted to build applications to automatically generate recipe summary from videos, and hence to support decision making of rookie home chefs.

The whole system is powered by NLTK, Stanford NLP SDK and Brat.
###Requirements:
* Python 2.7+
* JDK 1.7+
* [NLTK 3.0](http://www.nltk.org/)
* [Stanford Named Entity Recognizer (NER)](http://nlp.stanford.edu/software/CRF-NER.shtml)
* [BRAT](http://brat.nlplab.org/index.html)
####Line encoding
Unix `\n`

###BRAT
Some changes are directly made to the BRAT source code compared to the [original code](https://github.com/nlplab/brat)
Please install the brat first, then use the code inside *brat* folder to overide responding files.

###Usage 
Clone the repo

    $ git clone https://github.com/zhangdanyangg/RecipeIngredients.git

###License##
This project is released under MIT License.