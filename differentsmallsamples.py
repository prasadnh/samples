st = 'Print only the words that start with s in this sentence'
#Code here
for word in st.split():
    if word[0] == 's':
        print word

#Use range() to print all the even numbers from 0 to 10.
#Code Here
for num in range(0,10):
    if (num % 2 == 0):
        print num

range(0,11,2)


#Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
#Code in this cell
lst = [num for num in range(1,50) if num % 3 == 0]
lst

**Go through the string below and if the length of a word is even print "even!"**
st = 'Print every word in this sentence that has an even number of letters'
#Code in this cell
for word in st.split():
    if len(word) % 2 == 0:
        print 'this word %s has even number' %word


#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".
#Code in this cell
for num in range(1,100):
    if num %3 == 0 and num % 5 == 0:
        print 'FizzBuzz'
    elif num % 5 == 0:
        print 'Buzz'
    elif num % 3 == 0:
        print 'Fizz'

#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
#Code in this cell
for word in st.split():
    print word[0]

print st
[word[0] for word in st.split()]


def is_prime(val):
    """
    INPUT: A number
    OUTPUT: prints prime or not
    This function checks for prime numbers
    """
    lst = []
    for num in range(1,val):
        if num <= 1:
            print str(num) + ' is not a prime number'
        elif num == 2:
            print str(num) + ' is prime number'
            lst.append(num)
        else:
            for n in range(2, num):
                if num % n == 0:
                    print '%s is Not a Prime number' %num
                    break
            else:
                print 'The number %s is prime' %num
                lst.append(num)
                
    print lst


l = [1,1,1,1,2,2,3,3,3,3,4,5]

def unique_list(l):
    #return set(l)
    x = []
    for num in l:
        if num not in x:
            x.append(num)
    return x
unique_list(l)


def palindrome(s):
    return s[::-1]

def palindrome(s):
    #return s[::-1]
    s=s.replace(" ", "")
    return s[::-1]


import string

str1 = "The quick brown fox jumps over the lazy dog"
def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())  