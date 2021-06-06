from flask import Flask, jsonify, request
from flask_cors import CORS

from scipy.spatial.distance import cosine
from nltk.stem import WordNetLemmatizer
import pickle

lem = WordNetLemmatizer()

app = Flask(__name__)
CORS(app)

dictionary = {}
idf = {}

#api to process query and return results
@app.route('/search',methods = ['GET'])
def search():

    global dictionary,idf

    query = str(request.args['Query'])
    query = query.lower()
    query = query.split()
    query = [lem.lemmatize(term) for term in query]
    
    #fetching relevant docs
    docs = set()
    for term in query:
        if term in list(dictionary.keys()):
            docs = docs.union(set(dictionary[term].keys()))


    #formation of the tf-idf matrix for docs
    tfidf_mat = {}
    for doc in docs:
        
        tfidf_mat[doc] = []
        for word in dictionary:
            
            if doc in dictionary[word].keys():
                tfidf_mat[doc].append(dictionary[word][doc]*idf[word])
            else:
                tfidf_mat[doc].append(0)


    #formation of the query matrix
    query_mat = [0 for _ in range(len(dictionary))]
    for term in query:
        try:
            pos = list(dictionary.keys()).index(term)
            query_mat[pos]+=1
        except:
            continue
    
    
    #computing the cosine similarity
    sim = {}
    for doc in docs:
        sim[doc]  = 1 - cosine(query_mat,tfidf_mat[doc])


    #sorting the results and filtering wrt to alpha 
    results = sorted(sim.items(),key=lambda kv:kv[1],reverse=True)
    doc = []
    score = []
    alpha = 0.005
    for elem in results:
        if float(elem[1])>=alpha:
            doc.append(elem[0])
            score.append(elem[1])




    #returning the doc+score
    results = {}
    results['doc'] = doc
    results['score'] = score

    return jsonify(results)



if __name__ == '__main__':


    with open('dictionary.pkl', "rb" ) as file:
        dictionary = pickle.load(file)

    with open('idf.pkl', "rb" ) as file:
        idf = pickle.load(file)
    
    app.run(debug = True)