#textparsing.py 
#Elise Meike September 2017
#experiments with nltk


import nltk
from urllib import request


#divides the number of unique words by the total word count of the text (code modified from nltk.org) 
def lexical_diversity(text):
    return len(set(text)) / len(text) 

def percentage(count, total):
    return 100 * count / total

def avg_sentence_length(text):
	sentences = text.count('.') + text.count('!') + text.count('?')
	return len(text) / sentences

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

final_text = get_text("http://www.gutenberg.org/files/1342/1342-0.txt")

print("Examining " + str(final_text))
print("The text is {:,} characters long.".format(len(final_text)))
print("Lexical diversity = {:03.3f}".format(lexical_diversity(final_text)))
print("{:03.3f} % of the text is 'the'".format(percentage(final_text.count('the'), len(final_text))))
print("The average length of a sentence is {:03.2f}".format(avg_sentence_length(final_text)))


#finding the occurences of specific words in the text
words = {"marry", "Elizabeth", "Darcy"}

for word in words:
	print("'{}' occurs {:,} times.".format(word, final_text.count(word)))
