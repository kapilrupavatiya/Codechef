#file:///home/kapil/Desktop/Codechef/Codechef%20February/01/Chef%20and%20Chain%20|%20CodeChef.html
#Chef and Chain
T = int(raw_input())
for i in range(0,T):
	line1=raw_input()
	lenth=len(line1)
	minus=0
	plus=0
	for j in range(0,lenth):
		if( j % 2 == 0 ):
			if( line1[j] == '-' ):
				plus = plus + 1
			else:
				minus = minus + 1
		else:
			if( line1[j] == '+' ):
				plus = plus +1
			else:
				minus = minus + 1
	if( plus < minus ): 
		print plus
	else:
		print minus
