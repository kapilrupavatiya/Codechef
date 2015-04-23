import sys
string = sys.stdin.readline()
n = int(sys.stdin.readline())
lenth =  len(string) - 1 
dp = [0]*lenth
dp[lenth-1] = [0] * 16
#12c
#13h
#14e
#15f
c=0
h=0
e=0
f=0

if (string[lenth-1] == 'c'):
	dp[lenth-1][12] = 1
	c = 1
elif (string[lenth-1] == 'h'):
	dp[lenth-1][13] = 1
	h = 1
elif (string[lenth-1] == 'e'):
	dp[lenth-1][14] = 1
	e = 1
else:
	dp[lenth-1][15] = 1
	f = 1

for i in range ( lenth - 2 , -1 , -1 ):
	dp[i] = [0] * 16
	dp[i][0] = dp[ i + 1 ][ 0 ]
	dp[i][1] = dp[ i + 1 ][ 1 ]
	dp[i][2] = dp[ i + 1 ][ 2 ]
	dp[i][3] = dp[ i + 1 ][ 3 ]
	dp[i][4] = dp[ i + 1 ][ 4 ]
	dp[i][5] = dp[ i + 1 ][ 5 ]
	dp[i][6] = dp[ i + 1 ][ 6 ]
	dp[i][7] = dp[ i + 1 ][ 7 ]
	dp[i][8] = dp[ i + 1 ][ 8 ]
	dp[i][9] = dp[ i + 1 ][ 9 ]
	dp[i][10] = dp[ i + 1 ][ 10 ]
	dp[i][11] = dp[ i + 1 ][ 11 ]

	
	if ( string[i] == "c" ):
		dp[i][0] = dp[ i + 1 ][ 0 ] + h 
		dp[i][1] = dp[ i + 1 ][ 1 ] + e
		dp[i][2] = dp[ i + 1 ][ 2 ] + f
		#print "ans -> " + str(dp[i][2])
		c = c + 1
	
	elif ( string[i] == "h" ):
		dp[i][3] = dp[ i + 1 ][ 3 ] + c
		dp[i][4] = dp[ i + 1 ][ 4 ] + e 
		dp[i][5] = dp[ i + 1 ][ 5 ] + f
		h = h + 1
	
	elif ( string[i] == "e" ):
		dp[i][6] = dp[ i + 1 ][ 6 ] + c
		dp[i][7] = dp[ i + 1 ][ 7 ] + f 
		dp[i][8] = dp[ i + 1 ][ 8 ] + h
		e = e + 1
	
	elif( string[i] == "f" ):
		dp[i][9] = dp[ i + 1 ][ 9 ] + e 
		dp[i][10] = dp[ i + 1 ][ 10 ] + c 
		dp[i][11] = dp[ i + 1 ][ 11 ] + h
		f = f + 1
	
	dp[i][12] = c
	dp[i][13] = h
	dp[i][14] = e
	dp[i][15] = f
	
	#ch
	#dp[i][0] = 
	#ce
	#dp[i][1] =
	#cf
	#dp[i][2] =
	#hc
	#dp[i][3] =
	#he
	#dp[i][4] =
	#hf
	#dp[i][5] =
	#ec
	#dp[i][6] =
	#ef
	#dp[i][7] =
	#eh
	#dp[i][8] =
	#fe
	#dp[i][9] =
	#fc
	#dp[i][10] =
	#fh
	#dp[i][11] =
	#print " i-> " + str(i) +" -> "+ str( dp[i][2] )
	#print " f-> " + str(i) +" -> "+ str( dp[i][15] )

for i in range(0,n):
	inlist = sys.stdin.readline().split()
	startchar = inlist[0]
	endchar = inlist[1]
	startindex = int ( inlist[2] )
	endindex = int ( inlist[3] )
	ans=0
	mul=0
	if(startchar == 'c' and endchar == 'h' ):
		if (endindex == lenth):
			print dp[startindex-1][0]
		else:
			no = dp[endindex][13]   # end index
			start = dp[startindex-1][12] - dp[endindex][12] # start index
			print (dp[startindex-1][0] - dp[endindex][0] - (no*start))
			
	if(startchar == 'c' and endchar == 'e' ):
		if (endindex == lenth):
			print dp[startindex-1][1]
		else:
			no = dp[endindex][14]   # end index
			start = dp[startindex-1][12] - dp[endindex][12] # start index
			print (dp[startindex-1][1] - dp[endindex][1] - (no*start))
			
	if(startchar == 'c' and endchar == 'f' ):
		if (endindex == lenth):
			print dp[startindex-1][2]
		else:
			no = dp[endindex][15]   # end index
			start = dp[startindex-1][12] - dp[endindex][12] # start index
			print (dp[startindex-1][2] - dp[endindex][2] - (no*start))
			
	if(startchar == 'h' and endchar == 'c' ):
		if (endindex == lenth):
			print dp[startindex-1][3]
		else:
			no = dp[endindex][12]   # end index
			start = dp[startindex-1][13] - dp[endindex][13] # start index
			print (dp[startindex-1][3] - dp[endindex][3] - (no*start))
			
	if(startchar == 'h' and endchar == 'e' ):
		if (endindex == lenth):
			print dp[startindex-1][4]
		else:
			no = dp[endindex][14]   # end index
			start = dp[startindex-1][13] - dp[endindex][13] # start index
			print (dp[startindex-1][4] - dp[endindex][4] - (no*start))
			
	if(startchar == 'h' and endchar == 'f' ):
		if (endindex == lenth):
			print dp[startindex-1][5]
		else:
			no = dp[endindex][15]   # end index
			start = dp[startindex-1][13] - dp[endindex][13] # start index
			print (dp[startindex-1][5] - dp[endindex][5] - (no*start))
			
	if(startchar == 'e' and endchar == 'c' ):
		if (endindex == lenth):
			print dp[startindex-1][6]
		else:
			no = dp[endindex][12]   # end index
			start = dp[startindex-1][14] - dp[endindex][14] # start index
			print (dp[startindex-1][6] - dp[endindex][6] - (no*start))
			
	if(startchar == 'e' and endchar == 'f' ):
		if (endindex == lenth):
			print dp[startindex-1][7]
		else:
			no = dp[endindex][15]   # end index
			start = dp[startindex-1][14] - dp[endindex][14] # start index
			print (dp[startindex-1][7] - dp[endindex][7] - (no*start))
			
	if(startchar == 'e' and endchar == 'h' ):
		if (endindex == lenth):
			print dp[startindex-1][8]
		else:
			no = dp[endindex][13]   # end index
			start = dp[startindex-1][14] - dp[endindex][14] # start index
			print (dp[startindex-1][8] - dp[endindex][8] - (no*start))
			
	if(startchar == 'f' and endchar == 'e' ):
		if (endindex == lenth):
			print dp[startindex-1][9]
		else:
			no = dp[endindex][14]   # end index
			start = dp[startindex-1][15] - dp[endindex][15] # start index
			print (dp[startindex-1][9] - dp[endindex][9] - (no*start))
			
	if(startchar == 'f' and endchar == 'c' ):
		if (endindex == lenth):
			print dp[startindex-1][10]
		else:
			no = dp[endindex][12]   # end index
			start = dp[startindex-1][15] - dp[endindex][15] # start index
			print (dp[startindex-1][10] - dp[endindex][10] - (no*start))
			
	if(startchar == 'f' and endchar == 'h' ):
		if (endindex == lenth):
			print dp[startindex-1][11]
		else:
			no = dp[endindex][13]   # end index
			start = dp[startindex-1][15] - dp[endindex][15] # start index
			print (dp[startindex-1][11] - dp[endindex][11] - (no*start))
