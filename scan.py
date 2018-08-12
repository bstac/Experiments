"""
#Might be useful
corpus = nltk.corpus.treebank.tagged_sents()
tagger = nltk.data.load('taggers/maxent_treebank_pos_tagger/
english.pickle')
tagger.evaluate(corpus)

http://www.eecis.udel.edu/~trnka/CISC889-11S/lectures/dongqing-chunking.pdf
http://www.comp.leeds.ac.uk/amalgam/tagsets/upenn.html

BIgrms
>>> import nltk
>>> from nltk.collocations import *
>>> bigram_measures = nltk.collocations.BigramAssocMeasures()
>>> trigram_measures = nltk.collocations.TrigramAssocMeasures()
>>> finder = BigramCollocationFinder.from_words(
...     nltk.corpus.genesis.words('english-web.txt'))
>>> finder.nbest(bigram_measures.pmi, 10)  
[(u'Allon', u'Bacuth'), (u'Ashteroth', u'Karnaim'), (u'Ben', u'Ammi'),
 (u'En', u'Mishpat'), (u'Jegar', u'Sahadutha'), (u'Salt', u'Sea'),
 (u'Whoever', u'sheds'), (u'appoint', u'overseers'), (u'aromatic', u'resin'),
 (u'cutting', u'instrument')]

this breaks because of the second line, seperates that which is atomic
NP: }<[\.VI].*>+{       
        <.*>}{<DT>


# NP stage
# chunk determiners, adjectives and nouns
# chunk proper nouns
NP:                   
      {<DT>?<JJ>*<NN>}    
      {<NNP>+}

# start by chunking everything
# chink any verbs, prepositions or periods
# separate on determiners
# PP = preposition + noun phrase
# VP = verb words + NPs and PPs
NP: {<.*>*}
        }<[\.VI].*>+{       
        <.*>}{<DT>          
    PP: {<IN><NP>}          
    VP: {<VB.*><NP|PP>*}

# start by chunking each tag
# unchunk any verbs, prepositions or periods
# merge det/adj with nouns
NP:
      {<.*>}              
      }<[\.VI].*>+{       
      <DT|JJ>{}<NN.*> 

"""
import nltk
college = nltk.collocations
#twoToucksTookTooManyTokes
took = nltk.word_tokenize
bilbo = nltk.pos_tag

patterns = """
NP: {<DT|PP\$>?<JJ>*<NN>}
{<NNP>+}
{<NN>+}
"""

# chunk determiners, adjectives and nouns
# VP = verb words
grammar = r"""
    NP: {<DT>?<JJ>*<NN>}    
    VP: {<TO>?<VB.*>}       
"""   


chunk = nltk.RegexpParser(patterns)
def chunky(s):
    return chunk.parse(bilbo(took(s)))

gram = nltk.RegexpParser(grammar)
def grammy(s):
    return gram.parse(bilbo(took(s)))

def lastLet(word):
    return word[len(word)-1]

def genPerms(s):
    return perms('',s)

def noDups(s):
    wDups = genPermList(s)
    wOutDups = remDups(wDups)
    wOutDups.sort()
    return wOutDups
    
def perms(buildPerm,togoString):
    togoLen = len(togoString)
    if togoLen == 0:
        print(buildPerm)
    else:
        for i in range(togoLen):
            perms(buildPerm + togoString[i],togoString[:i] + togoString[i+1:])
 
def genPermList(s):
    L =[]
    return permLis('',s,L)
 
def permLis(buildPerm,togoString,L):
    togoLen = len(togoString)
    if togoLen == 0:
        L.append(buildPerm)
    else:
        for i in range(togoLen):
            permLis(buildPerm + togoString[i],togoString[:i] + togoString[i+1:],L)
    return L

def remDups(L):
    newL = []
    for item in L:
        if not(item in newL):
            newL.append(item)
    return newL

def readAfile(fName):
    f = open(fName,'r')
    return f.read()

def rwAfile(fNameIn,fNameOut):
    f_in = open(fNameIn,'r')
    f_out = open(fNameOut,'w')
    contents = f_in.read()
    f_out.write(contents)
    return 'Done!'

