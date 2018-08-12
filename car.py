import urllib2
import sqlite3
import random
import time
import datetime

random.seed() #uses system time to seed

def CraigsListCars():
	s_site = 'craigslist_cars'
	s_url = 'https://philadelphia.craigslist.org/search/cta?s='
	art = CL_GetArticleList(s_url)
	print('number of articles: '+str(len(art)))
	cars = Get_Articles(art[0:20])
	cl = CL_GetTable(cars)
	tags = cl[0]
	table = cl[1]
	create = CreateStatement(s_site,tags)
	inserts = InsertStatements(s_site,table)
	DatabaseOut(s_site,create, inserts)
	
def CL_GetArticleList(s_url):
	contents = []
	for x in range(3000//120):
		y=x*120
		try:
			contents.append(urllib2.urlopen(s_url+str(y)).read())
			time.sleep(Rnd(3,12))
		except Exception as e:
			print('error with: '+x + '\n' + str(e))
	b=''
	for x in contents:b+=x
	WriteOutArticleList(b)
	c=b.split('<a href="https://philadelphia.craigslist.org/cto/d/')
	d=[]
	for x in c:d.append('https://philadelphia.craigslist.org/cto/d/'+x.split('"')[0])
	return list(set(d))


def Get_Articles(urls):
	contents = []
	for x in urls:
		try:
			contents.append([urllib2.urlopen(x).read(),x])
			time.sleep(Rnd(4,10))
		except Exception as e:
			print('urls - error with: ' + x + '\n' + str(e))
	return contents

def CL_GetTable(cars):
	tags=['url', 'description', 'postingbody']
	table = []
	for car in cars:
		try:
			record = []
			record.append(['url',car[1]])
			metasection = car[0].split('<meta name="description"')[1].split('<meta name="robots"')[0]
			record.append(['description',metasection])
			attrsection = car[0].split('<div class="mapAndAttrs">')[1].split('<section id="postingbody">')[0]
			attrsect = attrsection.split('\n')
			for x in attrsect:
				if('<span>' in x and ':' in x and '</span>' in x):
					y=x.split(':')
					key = y[0].replace('<span>' ,'').replace('<b>','').replace('</b>','').replace(' ','')
					val = y[1].replace('/<span>','').replace('<b>','').replace('</b>','').replace(' ','')
					record.append([key,val])
					if(key not in tags):tags.append(key)
			bodysection = car[0].split('<section id="postingbody">')[1].split('</section>')[0]
			record.append(['postingbody',bodysection])
		except Exception as e:
			print('get table - error with: ' + car[1] + '\n' + str(e))
	return [tags,table]
	

def WriteOutArticleList(b):
	a=open('cars_'+str(datetime.date.today())+'.txt','w')
	a.write(b)
	a.close()
	del a


def Rnd(a=1,b=10):
	return random.randint(a,b)

def CreateStatement(tablename,tags):
	st = 'CREATE TABLE ' + tablename + ' ('
	ct=0
	for x in tags:
		if(ct!=0):st+=', '
		st+=x+' text'
		ct+=1
	st+=')'
	return st

def InsertStatements(tablename,table):
	st = 'INSERT INTO ' + tablename
	col=''
	val=''
	ct=0
	print('------\n'+str(table)+'\n-----')
	for x in table:
		if(ct!=0):col+=', '
		if(ct!=0):val+=', '
		col+=x[0]
		val+='\''+x[1].replace('\'','\'\'')+'\''
		ct+=1
	st+= '(' + col + ') VALUES (' + val + ')'
	return st

def DatabaseOut(website,create,inserts):
	conn = sqlite3.connect(website+'_db_'+str(datetime.date.today())+'.db')
	c = conn.cursor()
	print(str(create))
	c.execute(str(create))
	for x in inserts:
		try:
			print(str(x))
			c.execute(str(x))
		except Exception as e:
			print('did not work for : '+x + '\n' + str(e))
	conn.commit()
	conn.close()

