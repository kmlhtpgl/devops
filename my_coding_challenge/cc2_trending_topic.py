with open ("tweets_Jerusalem_small.txt", "r") as myfile:
    wordlist=myfile.readlines()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))
    
final_list = list(zip(wordlist, wordfreq))
print(final_list[5])
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))





