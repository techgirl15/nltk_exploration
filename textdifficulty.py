#textdifficulty.py 
#Elise Meike September 2017
#experiments with nltk to determine different levels of difficulty of a text

import nltk
#from nltk import word_tokenize
#from urllib import request
from nltk.corpus import inaugural


cfd = nltk.ConditionalFreqDist(
	(target, fileids[:4])
	for fileids in inaugural.fileids()
	for w in inaugural.words(fileids)
	for target in ['america', 'citizen']
	if w.lower().startswith(target))

cfd.plot()

#from nltk.corpus import udhr
#languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']

#cfd = nltk.ConditionalFreqDist(
#	(lang, len(word))
#	for lang in languages
#	for word in udhr.words(lang + '-Latin1'))

#cfd.plot(cumulative=True)

#url = "http://www.gutenberg.org/files/1342/1342-0.txt"

#response = request.urlopen(url)
#raw = response.read().decode('utf8')
#print(type(raw))
#tokens = nltk.word_tokenize(raw)
#print(type(tokens))
#text = nltk.Text(tokens)
#print(type(text))

#def lexical_diversity(text):
#    return len(set(text)) / len(text)

#def sentences(text):
#	return len(text.sents())



#using already downloaded text (code modified from technaverbascripta.wordpress.com)
#f = open('PridePrejudice.txt', mode = 'r')
#text = f.read()
#nltk_text = text.split()
#final_text = nltk.Text(nltk_text)
#print(len(text.words())
#print(len(text) / len(st(raw)))
#print(text.count('a'))
#print(text.count('.'))