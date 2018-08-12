from nltk import Tree


def rec(t):
	if(type(t)==Tree or type(t)==list):
		for x in t: rec(x)
	else: return t


def rec_p(t):
	if(type(t)==Tree or type(t)==list):
		for x in t: rec_p(x)
	else: print(t)
	
