#Naomi Staley
#Tile Puzzle
#This program determines if an n by m tile puzzle is solvable.
#Any matrix with one spot the blank tile (labeled as none in the matrix)
#can be taken as input.

import sys

def solvable(W):
	row = len(W)		#number of rows or n
	col = len(W[0])		#number of columns or m
	swaps = 0			#set the total swaps or inversions initially to zero
	#this is looking at each value, a, in the matrix
	for k in range(row):
		for l in range(col):
			#this looks at all the values appearing after, a, in the matrix
			#to see how many of those are less than a
			for i in range(row-k):
				for j in range(col):
					#if you are not looking at the null element
					if(W[i+k][j]!=None):
						#if the row of the value you are looking at is the
						#same as the row of a only look at the values in this
						#row whose column comes after the column a is in
						if(k==i+k):
							#if any of those values are less than a then
							#add one to the total number of swaps
							if (l<j and W[k][l]> W[i+k][j] and W[i+k][j]!=None):
								swaps= swaps + 1
						#if not just look at all the values in that row
						#and see if a is less than any of them
						else:
							if (W[k][l]> W[i+k][j] and W[i+k][j]!=None):
								swaps = swaps + 1
					#when you are looking at the empty element
					#record the row the empty tile is in
					else:
						empty = i+k
	#when there is an even number of columns and the empty square is
	#an even row counting from the bottom then add one to the total sum
	if( col % 2 == 0 and (row-(empty)) % 2 == 0 ):
		swaps = swaps + 1
	#If the total number of swaps is even the puzzle is solvable.
	if( swaps % 2 == 0):
		solvable = True
	#If the total number of swaps is odd the puzzle is not solvable.
	else:
		print swaps % 2
		solvable = False
	return solvable
				
def main(argv):
	
	#input matrix/array
	W = ([[1,2,3,4],
			[5,6,7,None],
			[9,10,11, 8]])
	swaps = solvable(W)
	print"solvable? ", swaps
	return 0

if __name__ == "__main__":
	main(sys.argv)