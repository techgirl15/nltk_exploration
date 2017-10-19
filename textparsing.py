#textparsing.py 
#Elise Meike October 2017
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
	return raw_text

def tokenize_text(text):
	tokens = nltk.word_tokenize(text)
	#print(type(tokens))
	f_text = nltk.Text(tokens)
	#print(type(text))
	return f_text

def lexical_diversity(text):
	#divides the number of unique words by the total word count of the text (code modified from nltk.org) 
    return len(set(text)) / len(text) 

def percentage(count, total):
    return 100 * count / total

def avg_sentence_length(raw, text):
	st = nltk.sent_tokenize
	sentences = len(st(raw))
	return len(text) / sentences

def common_words(text):
	fdist1 = nltk.FreqDist(text)
	cwords = fdist1.most_common(50)
	fdist1.plot(50, cumulative=True)
	fdist1.plot(50, cumulative=False)
	return cwords

def word_length(raw, text):
	fdist2 = nltk.FreqDist(len(w) for w in text)
	#lwords = fdist2.most_common()
	#print(lwords)
	num_chars = len(raw)
	num_words = len(text)
	modelength = fdist2.max()
	avelength = num_chars/num_words
	#fdist2.plot(20, cumulative=False)
	return modelength, avelength

def occurrences(text, words):
	#finding the occurences of specific words in the text
	#lower_tokens = nltk.word_tokenize(raw.lower())
	for word in words:
		print("'{}' occurs {:,} times.".format(word, text.count(word)))

def analyze(raw, text, words):
	print("Examining " + str(text))
	print("The text is {:,} characters long.".format(len(text)))
	print("Lexical diversity (unique words/total) = {:03.3f}".format(lexical_diversity(text)))
	print("{:03.3f} % of the text is 'the'".format(percentage(text.count('the'), len(text))))
	print("The average length of a sentence is {:03.2f} words.".format(avg_sentence_length(raw, text)))
	print("The most common word length is {} characters.".format(word_length(raw, text)[0]))
	print("The average word length is {:03.2f} characters.".format(word_length(raw, text)[1]))
	#occurrences(text, words)



#let's do the thing
raw_words = get_text("http://www.gutenberg.org/files/1342/1342-0.txt")
final_text = tokenize_text(raw_words.lower())
words = {"the","a","be","to","of"}

analyze(raw_words, final_text, words)
