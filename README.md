#Recipe Ingredients
---
Report: http://git.io/p9Tl  
Repository: https://github.com/idf/RecipeIngredients

##Description

For CZ4045 Natural Language Processing Project
Nanyang Technological University  
Instructor: [Prof Kim Jung-Jae](http://www.ntu.edu.sg/home/jungjae.kim/Home/Home.html)

The purpose of our project is to build a system that could automatically recognize meaningful entities in cooking tutorial videos (including recipe names, ingredients and amounts and units), as well as the relationship between quantities, units and ingredients. In the future the trained model can be adopted to build applications to automatically generate recipe summary from videos, and hence to support decision making of rookie home chefs.

In this project, the meaningful entities and their relations in cooking video transcripts were tagged. A CRF model was trained with the tags, to predict the entities and relations in both non-automatic and automatic transcripts. The model achieved satisfactory F-measure on non-automatic transcripts and high Precision on automatic transcripts.

The whole system is powered by NLTK, Stanford NLP and Brat.
###Requirements:
* Python 2.7
* Java JDK 1.8+
* [NLTK 3.0](http://www.nltk.org/)
* [Stanford Named Entity Recognizer (NER)](http://nlp.stanford.edu/software/CRF-NER.shtml)
* [Brat](http://Brat.nlplab.org/index.html)
* Unix line ending `\n`

###Brat
Some changes are directly made to the Brat source code compared to the [original code](https://github.com/nlplab/Brat)
Please install the Brat first, then use the code inside *Brat* folder to override responding files.

###Usage 
Clone the repo

```bash
git clone https://github.com/idf/RecipeIngredients.git
```

###License##
This project is released under MIT License.
