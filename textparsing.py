#textparsing.py 
#Elise Meike September 2017
#experiments with nltk


import nltk
#nltk.download()
#from nltk.book import text6


#divides the number of unique words by the total word count of the text (code modified from nltk.org) 
def lexical_diversity(text):
    return len(set(text)) / len(text) 

def percentage(count, total):
    return 100 * count / total

#using already downloaded text (code modified from technaverbascripta.wordpress.com)
f = open('PridePrejudice.txt', mode = 'r')
text = f.read()
nltk_text = text.split()
final_text = nltk.Text(nltk_text)

print("Examining " + str(final_text))
print("The text is {:,} characters long.".format(len(final_text)))
print("Lexical diversity = {:,}".format(lexical_diversity(final_text)))
print("{:03.2f} % of the text is 'the'".format(percentage(final_text.count('the'), len(final_text))))


#finding the occurences of specific words in the text
words = {"marry", "Elizabeth", "Darcy"}

for word in words:
	print("'" + word  + "'" + " occurs " + str(final_text.count(word)) + " times.")


#concord = text6.concordance(word)
#print(word + " occurs " str(len(str(concord))) "in the following passages of \n" + text6)
