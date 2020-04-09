# Kaggle exercise for Python - Strings and Dictionaries
# Link: https://www.kaggle.com/akshitgupta29/exercise-strings-and-dictionaries/edit
# @author: Akshit Gupta

def word_search(doc_list, keyword):
    keyword = keyword.lower().strip ('.,')
    result = []
    for i in doc_list:
        print (i)
        sent = i.split()
        sent = [x.lower() for x in sent]
        sent = [x.strip('.') for x in sent]
        sent = [x.strip(',') for x in sent]

        if keyword in sent:
            result.append(doc_list.index(i))

    return (result)

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    result = {}

    for key in keywords:
        result[key] = word_search(doc_list, key)
    print (result)

if __name__ == "__main__":
    doc_list=["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    keywords = ['casino', 'they']
    multi_word_search(doc_list, keywords)

