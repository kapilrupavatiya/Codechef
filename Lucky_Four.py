#http://www.codechef.com/LTIME21/problems/LUCKFOUR
#Lucky Four
T = int (raw_input())
for i in range (0,T):
	num = raw_input()
	ans = 0
	for j in range (0,len(num)):
		if ( num[j] == '4' ):
			ans = ans + 1
	print ans
