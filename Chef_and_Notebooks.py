#www.codechef.com/MARCH15/problems/CNOTE
#Chef and Notebooks
T = int (raw_input())
for i in range (0,T):
	line1 = raw_input()
	array = line1.split(" ")
	x = int (array[0])
	y = int (array[1])
	k = int (array[2])
	n = int (array[3])
	flag = 1
	bakipage = x - y
	
	for j in range (0,n):
		line2 = raw_input()
		array1 = line2.split(" ")
		a = int (array1[0])
		b = int (array1[1])
		
		if( bakipage - a <= 0 and k - b >= 0 ):
			flag=0
	
	if flag == 1:
		print ("UnluckyChef")
	else:
		print ("LuckyChef")
