#textparsing.py 
#Elise Meike September 2017
#experiments with nltk


import nltk
#nltk.download()
#from nltk.book import text6

#using already downloaded text (code modified from technaverbascripta.wordpress.com)
f = open('PridePrejudice.txt', mode = 'r')
text = f.read()
nltk_text = text.split()
final_text = nltk.Text(nltk_text)


#divides the number of unique words by the total word count of the text (code modified from nltk.org) 
def lexical_diversity(text):
    return len(set(text)) / len(text) 

def percentage(count, total):
    return 100 * count / total

print("Examining " + str(final_text))
print("The text is " + str(len(final_text)) + " characters long.")
print("Lexical diversity = " + str(lexical_diversity(final_text)))
print(str(percentage(final_text.count('the'), len(final_text))) + "% of the text is 'the'")


#finding the occurences of specific words in the text
words = {"marry", "Elizabeth", "Darcy"}

for word in words:
	print("'" + word  + "'" + " occurs " + str(final_text.count(word)) + " times.")


#concord = text6.concordance(word)
#print(word + " occurs " str(len(str(concord))) "in the following passages of \n" + text6)

