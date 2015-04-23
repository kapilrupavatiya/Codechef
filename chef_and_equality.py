#http://www.codechef.com/FEB15/problems/CHEFEQ
#Chef and equality
T = int(raw_input())
for i in range(0,T):
	number = int (raw_input())
	line1=raw_input()
	list1=line1.split(" ")
	lenth=len(list1)
	hashmap = {}
	for j in range(0,lenth):
		no = int (list1[j])
		if(hashmap.has_key(no)):
			val = hashmap[no]
			hashmap[no]=val+1
		else:
			hashmap[no]=1
	maxval=0
	for key,value in hashmap.items():
		if( value > maxval ):
			maxval = value
	print number-maxval
