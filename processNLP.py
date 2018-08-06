import spacy 
import nltk
from nltk.corpus import stopwords
stop = stopwords.words("english")

nlp = spacy.load("en")
doc = nlp("The big grey dog ate all of the chocolate, fortunately he wasn't sick!")

dummyDoc = nlp("The latest example deals with the cost of the United States embassy in Jerusalem. The President publicly announced the cost in March: “We’re going to have it built very quickly and inexpensively,” he said. “They put an order in front of my desk last week for $1 billion . . . We’re actually doing it for about $250,000, so check that out.” The actual cost will be almost 100 times higher, as CNN reports. A contract summary file for the embassy from the Office of Acquisitions of the Department of State (available on usaspending.gov) puts the figure at $21.2 million.")

for thing in dummyDoc.ents:
    print(thing, end = " ")
    print(thing.label_, end = " ")
    print(thing.label, end = " ")
    print("\n") 



dummyComment = "The latest example deals with the cost of the United States embassy in Jerusalem. The President publicly announced the cost in March: “We’re going to have it built very quickly and inexpensively,” he said. “They put an order in front of my desk last week for $1 billion . . . We’re actually doing it for about $250,000, so check that out.” The actual cost will be almost 100 times higher, as CNN reports. A contract summary file for the embassy from the Office of Acquisitions of the Department of State (available on usaspending.gov) puts the figure at $21.2 million."
print("DUMMY COMMENT: ", dummyComment)
dummyComment = ' '.join([word for word in dummyComment.split() if word not in stop])
sentences = nltk.sent_tokenize(dummyComment)

#tokenizes sentences into words --> sentences will become a 2D list [ [blah, blah, blah], [blah, blah, blah] ]
sentences = [nltk.word_tokenize(sent) for sent in sentences]

#tags each word in a sentence with a "part of speech" label --> sentences will become a 2D list with tuples 
# --> [ [ (blah, yuh), (blah, yuh), (blah, yuh) ], [ (blah, yuh), (blah, yuh), (blah, yuh) ] ]
sentences = [nltk.pos_tag(sent) for sent in sentences]
print (sentences, "\n")

#stuff here 
for tagged_sentence in sentences: 

    for chunk in nltk.ne_chunk(tagged_sentence): 
        
#         print (chunk)
        if type(chunk) == nltk.tree.Tree:
            print ("CHUNK: ", type(chunk))

