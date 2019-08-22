


def gen(p,q):
	n=p*q
	phi=(p-1)*(q-1)
	return [p,q,n,phi]


def prime_e(l,e):
	l.append(e)
	d=1
	for x in range(l[3]):
		if( (e*x)%l[3]==1):
			d = x
			break
	l.append(d)
	return l

def encrypt(l,m):
	return pow(m,l[4])%l[2]

def decrypt(l,m):
	return pow(m,l[5])%l[2]

#example
#python -c "import simple_rsa as rsa; l=rsa.gen(61,53); l=rsa.prime_e(l,17); print(rsa.decrypt(l,rsa.encrypt(l,345)) ); print(l)"
#345
#[61, 53, 3233, 3120, 17, 2753]
