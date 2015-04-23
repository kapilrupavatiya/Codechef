#file:///home/kapil/Desktop/Codechef/Codechef%20February/01/Chef%20and%20Chain%20|%20CodeChef.html
#Chef and Strange Formula
import sys
facto = [0]*1000000
def getfacto(x):
	if (x < 1000000):
		return facto[x]
	if (x >= mod):
		return 0
	return (x*getfacto(x+1)) % mod
	

line1 = sys.stdin.readline().split()
n=int(line1[0])
mod=int(line1[1])

ans = 0
facto [0] = facto [1] = 1
for i in range(2,1000000):
	facto [i] = ( facto[i-1] * i ) % mod

line2 = raw_input().split()
	
for i in range(0,n):
	lastint = int (line2[i])
	sum = (( lastint * ( lastint + 1) / 2 ) * lastint ) % mod 
	ans = ((ans + sum + getfacto(lastint+1) - 1) ) % mod
sys.stdout.write(str(ans))
