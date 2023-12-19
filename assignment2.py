def ExtractDrugNames(text):
    
    import pandas as pd
    import numpy as np
    import string
    import json
    import nltk
    import re
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    
    regular_punc = list(string.punctuation) # python punctuations 
    special_punc = ['©', '^', '®','¾', '¡','!','≥','±','→∞'] # user defined special characters to remove 
    punc_list = regular_punc + special_punc


    drugs_data = open('drugs_final','r')
    drugs = json.load(drugs_data)
    drugs = set(drugs)
    
    words_data = open('words_without_drugs','r')
    words = json.load(words_data)
    for i in range(0,5000):
        words.append(str(i))
    words = set(words)

    # Load the English dictionary
    dictionary = Dict("en_US")
    
    
    def remove_punctuation(text,punc_list):
        for punc in punc_list:
            if punc == '-' or punc == '~' :
                text = text.replace(punc,' ')
            else:
                text = text.replace(punc, '')
        return text.strip()

    def SeperateWord(word):
        i = 0
        new_words = []
        for char in word:
            if i == 0:
                i = i + 1
                continue
            else:
                if bool(char.isupper()):
                    new_words.append(word[0:i])
                    new_words.append(word[i:])

                    seperated_word = ''
                    for j in range(len(new_words)):
                        if j == 0:
                            seperated_word = new_words[j]
                        else:
                            seperated_word = seperated_word + ' ' + new_words[j]

                    return seperated_word
            i = i + 1

            return word 


    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()


    
    if type(text) == float:
        return  ''

    splitted_text = text.split(' ')
    text = []
    for word in splitted_text:
        text.append(SeperateWord(word))
    
    combined_text = ''
    for i in range(len(text)):
        if text[i] is None:
            continue
        elif i == 0:
            combined_text = text[i]
        else:
            combined_text = combined_text + ' ' + text[i]
    
    text = combined_text
    
    text = text.lower()
    text = remove_punctuation(text,punc_list)
    text = text.split(' ')
    
    text = [word for word in text if word not in stop_words]
    text = [lemmatizer.lemmatize(word) for word in text]
    
    drugs_found = []

    
    for word in text:
        if (word in drugs):
            drugs_found.append(word)
            

    drugs_found = set(drugs_found)
    drugs_found = list(drugs_found)
    
    

    extracted_drugs = drugs_found #+ remaining_words
    extracted_drugs = set(extracted_drugs)
    extracted_drugs = list(extracted_drugs)
    

    
    pattern = re.compile(r'^\d|^\D\d{1,2}\D$|^\D{1,2}\d+$|^\D{1,2}$|^\D{1,4}$|^\D\d{1,4}\D$|^\w+[^\w]$|^\w+[^\w]+\w$')
    
    drugs_extracted = []
    
    for drug in extracted_drugs:
        if drug == '':
            continue
            
        elif bool(pattern.search(drug)):
            continue
        
        elif drug in words:
            continue
        
        elif drug == 'mg':
            continue
        
        else:
            drugs_extracted.append(drug)
    
    final_drugs = ''
    for k in range(len(drugs_extracted)):
        if k == 0:
            final_drugs = str(k+1) + '. ' + drugs_extracted[k]
        else:
            final_drugs = final_drugs + '  ' + str(k+1) + ('. ') + drugs_extracted[k]
        
    
    return final_drugs

    
