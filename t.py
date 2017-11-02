import nltk

File = open('PridePrejudice.txt', mode = 'r') #open file
lines = File.read() #read all lines
sentences = nltk.sent_tokenize(lines) #tokenize sentences
nouns = [] #empty to array to hold all nouns

for sentence in sentences:
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
            nouns.append(word)

print(nouns)