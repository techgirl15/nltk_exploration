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

def common_words(text, depth):
	fdist1 = nltk.FreqDist(text)
	cwords = fdist1.most_common(depth)
	#fdist1.plot(50, cumulative=True)
	#fdist1.plot(50, cumulative=False)
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
	occurences = {}
	for word in words:
		occurences[word] = text.count(word)
	return occurences

def nouns(raw):
	sentences = nltk.sent_tokenize(raw)
	nouns = []
	for sentence in sentences:
		for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
			if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
				nouns.append(word)
	return nouns

def analyze(raw, words, depth):
	text = tokenize_text(raw.lower())
	ret_val = {}
	ret_val["text_name"] = str(text)
	ret_val["lexical_diversity"] = lexical_diversity(text)
	ret_val["len_char"] = len(text)
	ret_val["mean_sent_len"] = avg_sentence_length(raw, text)
	ret_val["mode_word_len"] = word_length(raw, text)[0]
	ret_val["mean_word_len"] = word_length(raw, text)[1]
	ret_val["common_words"] = common_words(text, depth)
	ret_val["word_occurence"] = occurrences(text, words)
	ret_val["noun_count"] = len(nouns(raw))

	for word in words:
		ret_val["percent_"+word] = percentage(text.count(word), len(text))
	
	return ret_val

def print_analysis(analysis):
	print("Examining " + analysis["text_name"])
	print("The text is {:,} characters long.".format(int(analysis["len_char"])))
	print("Lexical diversity (unique words/total) = {:03.3f}".format(analysis["lexical_diversity"]))
	print("The mean length of a sentence is {:03.2f} words.".format(analysis["mean_sent_len"]))
	print("The most common word length is {} characters.".format(analysis["mode_word_len"]))
	print("The mean word length is {:03.2f} characters.".format(analysis["mean_word_len"]))
	print("The most common words and the number of times they occur are {}".format(analysis["common_words"]))
	#occurrences(text, words)
	print("There are {:,} nouns in the text".format(analysis["noun_count"]))
	percent_keys = []
	for key in analysis.keys():
		if key.startswith("percent_"):
			percent_keys.append(key)
	for key in percent_keys:
		word = key[8:]
		print("{:03.3f} % of the text is '{}'".format(analysis[key], word))




#let's do the thing
raw_words = get_text("http://www.gutenberg.org/files/1342/1342-0.txt")
words = {"the","a","be","to","of"}
analysis_depth = 10
analysis= analyze(raw_words, words, analysis_depth)

print_analysis(analysis)
