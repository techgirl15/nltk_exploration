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

	return raw_text

def tokenize_text(text):
	tokens = nltk.word_tokenize(text)
	f_text = nltk.Text(tokens)

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
	#plots a line graph histogram of the most common words in each text. First it plots cumulatively.
	#The cumulative plot shows a very clean function that matches the expected of Zipf's Law.
	#The normal histogram shows a slightly less clean power law graph also indicative of Zipf's Law.
	fdist1.plot(50, cumulative=True)
	fdist1.plot(50, cumulative=False)

	return cwords

def word_length(raw, text):
	fdist2 = nltk.FreqDist(len(w) for w in text)
	#lwords = fdist2.most_common()
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
			if pos in ['NN', 'NNP', 'NNS', 'NNPS']:
				nouns.append(word)

	return nouns

def analyze(raw, words, depth):
	text = tokenize_text(raw.lower())

	ret_val = {}
	ret_val["lexical_diversity"] = lexical_diversity(text)
	ret_val["len_char"] = len(text)
	ret_val["mean_sent_len"] = avg_sentence_length(raw, text)
	ret_val["mode_word_len"] = word_length(raw, text)[0]
	ret_val["mean_word_len"] = word_length(raw, text)[1]
	ret_val["noun_count"] = len(nouns(raw))
	for word in words:
		ret_val["percent_"+word] = percentage(text.count(word), len(text))
	common_words(text, depth)
	#ret_val["common_words"] = common_words(text, depth)
	#ret_val["word_occurence"] = occurrences(text, words)

	return ret_val

def meta_analysis(texts, words, analysis_depth):
	analyses = {}
	#analyses is a dictonary of text names and sets of analysis (ie lexical diversity etc)
	for text, url in texts.items():
		raw_words = get_text(url)
		analysis = analyze(raw_words, words, analysis_depth)
		analyses[text] = analysis

	return analyses


def print_analysis(analyses):
	titles = [" "]
	#iterates over the text names (keys of the analyses dictonary)
	for name in analyses.keys(): 
		titles.append(name)

	#f is a formating placeholder, making columns of 25 characters that can be filled by any text <25 chars
	#the number of columns f makes is based on the number of titles defined (and an extra for the row name)
	f = " ".join(" {:%ds} " % 30 for n in titles)
	print(f.format(*titles))

	#keys is a list of operations done on the texts (ie lexical diversity etc) 
	keys = list(analyses.values())[0].keys()
	#this iterates over and prints the keys and data in the format f (defined above) so it is in columns of data
	for key in keys:
		values = [key]
		for value in analyses.values():
			values.append(value[key])

		#print(f.format(*values))
		if key in ["len_char", "mode_word_len", "noun_count"]:
			f = " {:25s} " + " ".join(" {:>20,d} " for n in range(0, len(titles) - 1))
		else:
			f = " {:25s} " + " ".join(" {:>20.2f} " for n in range(0,len(titles)-1))
		print(f.format(*values))




#let's do the thing
texts = {"Pride and Prejudice":None, "Frankenstein":"https://www.gutenberg.org/files/84/84.txt"}
words = {"the","a","be","to","of"}
analysis_depth = 10


print_analysis(meta_analysis(texts, words, analysis_depth))
