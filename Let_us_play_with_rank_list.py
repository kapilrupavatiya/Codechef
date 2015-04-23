#http://www.codechef.com/FEB15/problems/RANKLIST
#Play with Rank List
T = int(raw_input())
for i in range(0,T):
	line1=raw_input()
	list1=line1.split(" ")
	n=int(list1[0])
	s=int(list1[1])
	increment=2
	baki=n-1
	sum=1
	while(True):
		if(baki==1):
			if( sum+increment == s):
				print "0"
				break
		if( sum+increment+baki-1 >= s ):
			print baki
			break
		else:
			sum = sum + increment
			increment = increment +1
			baki = baki - 1
