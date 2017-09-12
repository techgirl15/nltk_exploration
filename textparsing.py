#textparsing.py 
#Elise Meike September 2017
#experiments with nltk


import nltk
#nltk.download()
from nltk.book import text6

#from nltk.org example code: divides the number of unique words by the total word count of the text
def lexical_diversity(text):
    return len(set(text)) / len(text) 


print("Examining " + str(text6))
print("The text is " + str(len(text6)) + " characters long.") #the text is len(text6) chars long
print("Lexical diversity = " + str(lexical_diversity(text6)))


words = {"swallow", "ni", "Arthur"}

for word in words:
	print("'" + word  + "'" + " occurs " + str(text6.count(word)) + " times.")

#concord = text6.concordance(word)
#print(word + " occurs " str(len(str(concord))) "in the following passages of \n" + text6)

