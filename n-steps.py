#n step stairs - a man can jump either 1 or 2 at a time
#find the number of ways the stairs can be climbed

import math

n = input('Enter number of steps: ')

#max steps - if all steps are single steps
maxSteps = n

#min steps - if all steps are double
minSteps = int(math.ceil(float(n)/2))

numSteps = maxSteps
numWays = 0
#iterate through number of possible steps to climb the stairs
for i in range(maxSteps-minSteps+1):
	#calculate the number of ways in which stairs of n steps can be climbed in 'numSteps' steps
	diff = n - numSteps #these many number of 2 steps need to be present
	#find the number of ways these 2 steps can be arranged in 'numSteps'
	ways = math.factorial(numSteps) / (math.factorial(numSteps-diff) * math.factorial(diff))
	#add to total number of ways
	numWays += ways
	#bump numSteps
	numSteps -= 1

print('Number of ways: '+str(numWays))

#side note - the output is coincidentally the fibonacci sequence
#if input is 0, 1, 2, 3, 4, 5, 6, 7 -> out will be 1, 1, 2, 3, 5, 8, 13, 21