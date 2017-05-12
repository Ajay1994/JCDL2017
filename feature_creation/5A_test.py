from collections import defaultdict

def mean(l):
	s=0
	sz=len(l)
	if sz==0:
		return 0
	return float(sum(l)/sz)
################### Preprocess ###############################
def preprocess(x,y):
	d=defaultdict(list)
	s=len(x)
	for i in range(s):
		d[x[i]].append(y[i])
	t={}
	for i in range(s):
		t[x[i]]=mean(d[x[i]])
	return t


x=[1,1,1,2,3,1]
y=[2,3,4,5,6,7]
t=preprocess(x,y)
print t