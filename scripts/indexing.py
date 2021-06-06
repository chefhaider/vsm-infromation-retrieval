#!/usr/bin/env python
# coding: utf-8



from nltk.stem import WordNetLemmatizer
import numpy as np
import pickle




lem = WordNetLemmatizer()




dictionary = {}
idf = {}



stop_words = {'a','is','the','of','all','and','to','can','be','as','once','for','at','am','are','has','have','had','up','his','her','in','on','no','we','do','s'}


for file_no in range(1,51):
    with  open(f"./ShortStories/{file_no}.txt", "r", encoding="utf8") as my_file:
        
        #document prepocessing
        words = my_file.read()
        for inv in "#'.,!?;:‘“”*&)(":
            words = words.replace(inv,'')
        
        words = words.replace('-',' ').replace('—',' ').replace('’',' ')
        words = words.lower()
        
        words = words.split() #tokenization


        
        for word in words:

            if word in stop_words: #neglection stop words
                continue

            word = lem.lemmatize(word)#stemming


            try:
                try:
                    dictionary[word][file_no]+=1 # updating document frequency
                except:
                    dictionary[word][file_no] = 1 #indexing documents
            except:
                dictionary[word] = {file_no:1} # indexing terms
        
        
#forming idf list
for key in dictionary.keys():
    idf[key] = np.log10(len(dictionary[key].keys()))/50
 

with open("dictionary.pkl", "wb") as file: #file for dictionarty
    pickle.dump(dictionary, file)


with open("idf.pkl", "wb") as file: #file for idf
    pickle.dump(idf, file)

print('files created!')

