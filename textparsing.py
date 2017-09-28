#textparsing.py 
#Elise Meike September 2017
#experiments with nltk


import nltk
from urllib import request

def get_text(url = None):
	if url is None:
		#using already downloaded text (code modified from technaverbascripta.wordpress.com)
		f = open('PridePrejudice.txt', mode = 'r')
		raw_text = f.read()
	else:
		#getting and tokenizing text from a URL (code modified from nltk.org)
		response = request.urlopen(url)
		raw_text = response.read().decode('utf8')
		#print(type(raw))
	tokens = nltk.word_tokenize(raw_text)
	#print(type(tokens))
	text = nltk.Text(tokens)
	#print(type(text))
	return text

def lexical_diversity(text):
	#divides the number of unique words by the total word count of the text (code modified from nltk.org) 
    return len(set(text)) / len(text) 

def percentage(count, total):
    return 100 * count / total

def avg_sentence_length(text):
	sentences = text.count('.') + text.count('!') + text.count('?')
	return len(text) / sentences

def occurrences(text, words):
	#finding the occurences of specific words in the text
	for word in words:
		print("'{}' occurs {:,} times.".format(word, text.count(word)))

def analyze(text, words):
	print("Examining " + str(text))
	print("The text is {:,} characters long.".format(len(text)))
	print("Lexical diversity = {:03.3f}".format(lexical_diversity(text)))
	print("{:03.3f} % of the text is 'the'".format(percentage(text.count('the'), len(text))))
	print("The average length of a sentence is {:03.2f}".format(avg_sentence_length(text)))
	occurrences(text, words)


#let's do the thing
final_text = get_text("http://www.gutenberg.org/files/1342/1342-0.txt")
words = {"marry", "Elizabeth", "Darcy"}

analyze(final_text, words)
