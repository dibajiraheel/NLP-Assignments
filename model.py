def TestFunction(pdf):
    
    import PyPDF2
    import os
    import re
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    import string
    import math
    import json
    
    
    data_model = open('model','r')
    counts = json.load(data_model)
    
    data_unique_corpus = open('unique_corpus','r')
    unique_corpus = json.load(data_unique_corpus)
    unique_corpus_set = set(unique_corpus)
    
    # Read pdf file and store in list named content
    content = []
    read = PyPDF2.PdfReader(pdf)
    pages = len(read.pages)
    for i in range(pages):
        content_read = read.pages[i].extract_text()
        content.append(content_read)

    # Join all pages of pdf in single string
    content = ' '.join(content)
    # Replace new line \n
    content = content.replace('\n',' ')
    content = content.replace('  ',' ')

    # Remove any references
    pattern = re.compile(r'\[\d{1,}]')
    b = content.split(' ')
    for word in b:
        if (pattern.search(word)):
            b.remove(word)
        c = ' '.join(b)
    content = c


    # Initialize punctuation list, stop words and lemmatizer
    puncs = list(string.punctuation)
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # Function to remove punctuations
    def RemovePunctuation(text):
        for punc in puncs:
            text = text.replace(punc,'')
        return text

    # Converts all words in string to lowercase
    content = content.lower()

    # Apply Punctuation, Stop Words, Lemmatizer
    content = RemovePunctuation(content)
    content = content.split(' ')
    content = [word for word in content if word not in stop_words]
    content = [lemmatizer.lemmatize(word) for word in content]


    # Create dictionary to store count of words in content and perform this operation
    count = dict()
    for word in unique_corpus:
        count[word] = 0

    for word in content:
        if word is not '' and word in unique_corpus_set:
            count[word] = count[word] + 1


    # Compute L2 Norm to normalize the count and perform this operation
    words = count.keys()

    squared_add = 0
    for word in words:
        squared_add = squared_add + (count[word] * count[word])

    norm = math.sqrt(squared_add)

    words = count.keys()
        
    for word in words:
        count[word] = count[word] / norm

    # Initialize dictionary to store similarity with all subjects and calculate scores
    similarity = {'CV':0, 'DL':0, 'ML':0, 'NIIA':0, 'NLP':0}
    keys = similarity.keys()

    for key in keys:
        subject_count = counts[key]
        score = 0
        for word in unique_corpus:
            a = subject_count[word]
            b = count[word]
            score = score + (a * b)
        similarity[key] = score
        
    keys = list(similarity.keys())
    scores = []
    for key in keys:
        scores.append(similarity[key])

    index = scores.index(max(scores))    

    return (keys[index])