#factorial(7) = 7*6*5*4*3*2*1
#factorial(6) = 6*5*4*3*2*1
#factorial(5) = 5*4*3*2*1
#factorial(4) = 4*3*2*1
#factorial(0) = 1

#factorial(n) = n * factorial(n-1)

#n(n-1)(n-2)(n-3)......(2)(1)

#5(4)(3)(2)(1)
#5(4)(3)(2!)

#n(n-1)!

#n!
#n(n-1)!

# factorial (n-1)

# (n-1)(n-2)!

# factorial (n-2)

# factorial(1)


def factorial(n):
    #terminating condition
    if n==1 or n==0:
       return 1 
    #function body
    return n*factorial(n-1)
     

#Created instances of Factorial function
# factorial(5) return 120
# factorial(4) return 24
# factorial(3) return 6
# factorial(2) return 2
# factorial(1) returns 1 based on terminating condition

def determinant(n):
    pass
if __name__ == "__main__":
 print(factorial(5))