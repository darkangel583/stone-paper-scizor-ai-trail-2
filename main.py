import random
from collections import Counter
def bot(i,j):
	d={"stone":0,"paper":0,"scizor":0}
	l=[]
	if i =="stone":
		d["stone"]=d["stone"]+1
		l.append(1)
	elif i == "paper":
		d["paper"]=d["paper"]+1
		l.append(2)
	elif i=="scizor":
		d["scizor"]=d["scizor"]+1
		l.append(3)
	if j>5:
		bag=[]
		x=[]
		for i in range(0,len(l)):
			if l[i] == 2:
				x.append(i)	
		for i in range(0,len(x)-1):		
			bag.append(l[x[i]:x[i+1]])
		d=Counter(bag)
		q=d.keys()
		b=0
		while b<(len(q)-1):
			if d[q[b]]>d[q[b+1]]:
				d[q[b]],d[q[b+1]]=d[q[b+1]],d[q[b]]
			b+=1
		if d[len(d)-1]>3:
			p=d[len(d)-1]
		else:		
			if d["stone"]>d["paper"] and d["stone"]>d["scizor"]:
				print("stone")
				p="stone"
			elif d["paper"]>d["stone"] and d["paper"]>d["scizor"]:
				print("paper")
				p="paper"
			elif d["scizor"]>d["paper"] and d["scizor"]>d["stone"]:
				print("scizor")
				p="scizor"
			else:
				l=["stone","paper","scizor"]
				o=random.choice(l)
				print(o)
				p=o
	if j<=5:
		l=["stone","paper","scizor"]
		o=random.choice(l)
		p=o
	return p	
j=0	
t=True	
while t == True:
	j+=1
	i=input()
	p=bot(i,j)
	if p=="stone":
		print("paper")
		if i == "stone":
			t=False
	if p=="paper":
		print("scizor")
		if i=="paper":
			t=False
	if p=="scizor":
		print("stone")
		if i=="scizor":
			t="False"				
print("You have played:",j,"rounds")	