#Entity Relationship Model 
This model is to identify the relationship among entities. 

After NER system tagged the entity name on the scripts, the relation between the entities could be extracted. For this recipe case, the amount of entities could be extracted from the tagged script.

This model contains three modules:
* ann_to_xml.py : Convert .ann file and responding text file into xml document
* info_extraction.py : Extract relation and entities sets from xml document.
* relation_evaluate.py : Evaluate the relation extractor.
 
There are three data folders:
* non-auto/ : Non-auto transcript tagged by human using brat
* ner-tagged/ : Non-auto tagged by NER system
* auto/ : Auto transcript tagged by NER system

##Usage
To generate evaluation result 
```
$ python relation_evaluate.py [data folder name]
```

##Method
Regular expression is used to extract the amount relation. There are several rules to find a relation: 
###Rules
```
<amount><ingredient>
<amount>[some description words without tag ]<ingredient>
<amount><unit><ingredient>
<amount>[some description words without tag ]<unit><ingredient>
<amount><unit>[some description words without tag ]<ingredient>
<amount>[some description words without tag ]<unit>[some description words without tag ]<ingredient>
<amount>[some other ingredient]<ingredient>
<amount><unit>[some other ingredient ]<ingredient>
```
###Coded Rules 
```
<Amount>(?P<amount>[^<]+)</Amount>[^<]{0,70}(<Ingredient>[^<]+</Ingredient>)*<Ingredient>(?P<ingredient>[^<]+)</Ingredient>

<Amount>(?P<amount>[^<]+)</Amount>[^<]{0,70}<Unit>(?P<unit>[^<]+)</Unit>[^<]{0,70}(<Ingredient>[^<]+</Ingredient>)*<Ingredient>(?P<ingredient>[^<]+)</Ingredient>
```
