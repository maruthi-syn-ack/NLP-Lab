import nltk 
import re 

# Download nescceary packages 
#nltk.download()

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
output = [w for w in wordlist if re.search('ed$',w)]

#print(wordlist[0],wordlist[1],wordlist[2],wordlist[3],wordlist[4])
for i in range(20):
	print(wordlist[i])
#print((" {} \n\n Found {} words \n\n ").format( output, len(output)))
