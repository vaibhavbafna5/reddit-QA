import spacy 

nlp = spacy.load("en")
doc = nlp("The big grey dog ate all of the chocolate, fortunately he wasn't sick!")

dummyDoc = nlp("The latest example deals with the cost of the United States embassy in Jerusalem. The President publicly announced the cost in March: “We’re going to have it built very quickly and inexpensively,” he said. “They put an order in front of my desk last week for $1 billion . . . We’re actually doing it for about $250,000, so check that out.” The actual cost will be almost 100 times higher, as CNN reports. A contract summary file for the embassy from the Office of Acquisitions of the Department of State (available on usaspending.gov) puts the figure at $21.2 million.")

for thing in dummyDoc.ents:
    print(thing, end = " ")
    print(thing.label_, end = " ")
    print(thing.label, end = " ")
    print("\n") 