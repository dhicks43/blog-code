#from stop_words import stop_words
from start_words import start_words
import string

word_dict = {}
with open("indeed_data_python.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        line = ''.join(c for c in line if c not in string.punctuation)
        line = line.lower()

        word_list = line.split(" ")

        for word in word_list:
            #if word and word not in stop_words:
            if word and word in start_words:
                if word not in word_dict:
                    word_dict[word] = 1

                word_dict[word] += 1


top_100_list = [ (word, word_dict[word]) for word in sorted(word_dict, key=word_dict.get , reverse=True) ]
print(top_100_list[:100])
