#Your code here
#You can import some modules or create additional functions

'''
To write a nice song Sophie needs to come up with a perfect rhythm according to the Euclidean algorithm. In order to 
calculate it he will need the greatest common divisor of two numbers. Write a function that will calculate a greatest 
common divisor of two numbers.
Example:
Input: A list of two integers.
Output: The greatest common divisor. A integer.
Example:
?
1
2
3
checkio((12, 8)) == 4
checkio((14, 21)) == 7
checkio((13, 11)) == 1
'''

def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    a, b = data

    while a != b:
    	if a > b:
    		a = a-b
    	else:
    		b = b-a
    return a


  
'''
      while b: 
        a,b = b,a % b 

    return a  
    #replace this for solution
 '''


#These "asserts" using only for self-checking and not necessary for auto-testing

print checkio((12, 8))# == 4 , "First example"
print checkio((14, 21)) #== 7, "Second example"
print checkio((13, 11))# == 1, "Third example"