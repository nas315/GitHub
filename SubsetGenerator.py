#Naomi Staley
#CS 375 Midterm Exam
#Question 1
#Due 10/24/12

#This program takes as input a positive integer n and generates all of the subsets of
#[1,...,n] with no subsets repeated.

import sys

#A class that genrates all the subsets of [1,2,...,n] with no reapeating
#subsets until all 2^n subsets have been seen.
class SubsetGenerator:
	def __init__(self, n):
		self.n = n
		self.previous = []
		#Prints the first subset.
		print self.previous
		
	#Sets the previously returned subset.
	def setPrevious(self, prev):
		self.previous = prev
	
	#Gets the previously returned subset.
	def getPrevious(self):
		return self.previous
	
	#Defines how to get the next subset so that all are generated with no
	#repeating subsets until all 2^n subsets have been seen.
	def next(self):
		#Gets the length of the previous subset generated.
		length = len(self.previous)
		next = self.previous
		#When the length is 0 you want to start with the first subset of
		#length 1, which is just 1 or the empty list appended with 1.
		if ( length == 0):
			next.append(1)
			self.previous = next
		#When you have generated all the subsets aka when the last subset
		#generated is of length n, restart the subsets.
		elif (length == self.n):
			next = []
			self.previous = next
		#When the length is not 0 or n this is how the  subsets are generated.
		else:
			#When the last element in the subarray is the same as the n.
			if (next[length-1]==self.n):
				#Create a list with the same number of elements as the
				#length of the previous subarray.
				B = []
				for i in range(length):	
					B.append( False)
				#Change the length -1 -(B array value) to True if the next
				#element in next array is one more then the one you are
				#looking at.
				for i in range (length-1):
					if (next[i] + 1 == next[i+1]):
						B[(length - 1) - i] = True
				#Sets a variable j to 1 when the subarray has more than 1 element.
				#When it only has one element, you just want to create subset of
				#lenght 2.
				if (length > 1):
					j = 1
				else:
					j= None
				#Finds the elements in the previous subset generated that are
				#not in sequential order. This starts from the end of the previous
				#subset because you want the greatest index where the next
				#element is not one larger. For example if the previous
				#subarray is [1,3,4] you want the next one to be [2,3,4].
				while ( j != None and B[j]== True):
					if (j+1>(length -1)):
						j =None
					else:
						j = j+ 1
				#When all the elements in the previous subarray are in order
				#or the previous subarray is 4 you want the next subarray
				#to have a size one larger than the previous.
				if ( j== None):
					next.append(1)
					for i in range(length+1):
						next[i]=i+1
				#When all of the elements in the previous subarray are not
				#all a sequence, where each term is greater than the previous
				#one, you want to change the (length -1) -index you found above
				#and then change all of the elements after it to be one plus 
				#that value.
				else:
					temp = next[length-1-j] + 1
					next[length-1 - j] = temp
					for k in range (length):
						if (k >( length-1 - j)):
							temp = temp+1
							next[k] = temp
			#When the last element in the subarray is not the same as the n,
			#you just want to increment the last element.
			else:
				temp = next[length-1]
				next[length-1] = temp +1
			
			
		return next

#This has a worst case time complexity of Theta(4*l) = Theta(l) for each
#previous subset of length l that ends in a 4. This is true becasue when
#the subset does not end in 4 there are 3 for loops of range l and a while
#loop that at most goes through l numbers, which gives Theta(4*l).
#When the last element of the previous subset is not 4 you just increment
#the last element in the previous subset by one, giving a time complexity
#of Theta(1).
	
def main(argv):
	#Generates all subsets of [1, 2, ..., n] without repeating and then
	#repeates the first one subset. If the user does not specify an n, 4 is used.
	n = 4
	if (len(argv)> 1):
		n = int(argv[1])
	generator = SubsetGenerator(n)
	for i in range (2**n):
		print(generator.next())

	return

if __name__ == "__main__":
	main(sys.argv)