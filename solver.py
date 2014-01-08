valcom=['k']
class node:
	def __init__(self,(x,y),value):
		self.value=value
		self.x=x
		self.y=y
		self.corner=False
		
		self.right=(x,y+1)
		self.left=(x,y-1)
		self.up=(x-1,y)
		self.down=(x+1,y)
		self.upleft=(x-1,y-1)
		self.downleft=(x+1,y-1)

		self.upright=(x-1,y+1)
		self.downright=(x+1,y+1)
		c=True
		if (self.left[0]==-1 or self.left[1] ==-1) :
			self.corner=True
			self.left=None

		if (self.right[0]==4 or self.right[1] ==4):
			self.corner=True
			self.right=None
		if (self.up[0]==-1 or self.up[1]==-1) :
			self.corner=True
			self.up=None
		if (self.down[0]==4 or self.down[1]==4):
			self.corner=True
			self.down=None
		if ((self.upleft[0]==-1 or self.upleft[1] ==-1)) or ((self.upleft[0]==4 or self.upleft[1]==4)):
			self.corner=True
			self.upleft=None
		if ((self.downleft[0]==-1 or self.downleft[1] ==-1)) or ((self.downleft[0]==4 or self.downleft[1]==4)):
			self.corner=True
			self.downleft=None
		if ((self.upright[0] ==4 or self.upright[1] ==4)) or ((self.upright[0]==-1 or self.upright[1] ==-1)):
			self.corner=True
			self.upright=None
		if ((self.downright[0]==4 or self.downright[1] ==4)) or ((self.downright[0]==-1 or self.downright[1] ==-1)):
			self.corner=True
			self.downright=None
	def getNeighbours(self,x):
		y=[]
		
		if self.left !=None:
			y=y+[x[self.left[0]*4+self.left[1]]]
		
				
		if self.right !=None:
			y=y+[x[self.right[0]*4+self.right[1]]]
		
					
		if self.up !=None:
			y=y+[x[self.up[0]*4+self.up[1]]]
		
					
		if self.down !=None:
			y=y+[x[self.down[0]*4+self.down[1]]]
		
			
		if self.upleft !=None:
			y=y+[x[self.upleft[0]*4+self.upleft[1]]]
				
		if self.downleft !=None:
			y=y+[x[self.downleft[0]*4+self.downleft[1]]]
		
			
		if self.upright !=None:
			y=y+[x[self.upright[0]*4+self.upright[1]]]
		
				
		if self.downright !=None:
			y=y+[x[self.downright[0]*4+self.downright[1]]]
		
		return y
	def getNeighbourValue(self,x):
		return map(self.findValue,self.getNeighbours(x))
	def findValue(self,y):
		if y==None:
			return None
		return y.value
	def getValue(self):
		return self.value

def wordamentSolver():
	x=raw_input("Input array. For combinations, enter block enclosed by quotes.\nFor indicating beginning or \neg. emakdhrgiricetan or emakdhrg'ig'ricetan\n")
	t=[]
	x=x.upper()
	for i in range(4):
		for j in range(4):
			if x[4*i+j]=='\'':
				m=4*i+j
				p=0
				for m in range(4*i+j,len(x)):
					if x[m]=='\'':
						p=p+1
					if p==2:
						
						t=t+[node((i,j),x[(4*i+j)+1:m])]
						break
				if p!=2:
					print "invalid input"
					exit()
				x=x[:4*i+j]+x[m:]
				
			else: 
				t=t+[node((i,j),x[4*i+j])]
	for i in range(4):
		l=""
		for j in range(4):
			l=l+t[4*i+j].getValue()
		
	
	s=[]
	for i in range(16):
		s=s+list(flatten(getposcom(t[i],wordList,[t[i].getValue()],t[i].getValue(),t,[])))
	s=set(list(flatten(s)))
	vw=[]
	
	vw=list(s.intersection(wordList))
	vw=map(str.lower,vw)
	vw.sort(key=len)
	print (vw)
	print ("%s words" %len(vw))
import itertools as IT
import collections

def flatten(iterable, ltypes=collections.Iterable):
    iterable = iter(iterable)
    remainder = iterable
    while True:
        first = next(remainder)
        if isinstance(first, ltypes) and not isinstance(first, basestring):
            remainder = IT.chain(first, remainder)
            first = next(iter(first))
        else:
            yield first
def getposcom(x,wordList,valcom,trail,t,prevnodes):
	if not notPartOfWord(trail):
		return trail[-1]
	

	
	valcom=valcom+[trail]
	y=x.getNeighbours(t)
	for j in prevnodes :
		
		if j in y:
			y.remove(j)
	
	prevnodes+=[x]
	if y==[] :
		
		return trail
	z=[]
	k=[]
	for i in prevnodes:
		k=k+[i]
	for i in y:
		prevnodes=[]
		for j in k:
			prevnodes=prevnodes+[j]
		
		z=z+[getposcom(i,wordList,valcom,trail+i.getValue(),t,prevnodes)]
		

	
	return z+[trail]

		
import string	


WORDLIST_FILENAME = "words.txt"
def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList
def ht():
	
	y={}
	z=string.ascii_uppercase
	for i in z:
		for j in range(len(wordList)):
			if (wordList[j])[0]==i:
				y[i]=j
				break
	return y
def notPartOfWord(x):
	x=x.upper()
	y=[]
	if x[0]=='z':
		y=wordList[hashTable[x[0]]:]
	else:
		y=wordList[hashTable[x[0]]:hashTable[chr(ord(x[0])+1)]]
	for i in y:
		if x in i:
			return True
	return False

wordList=loadWords()	
hashTable=ht()

wordamentSolver()
