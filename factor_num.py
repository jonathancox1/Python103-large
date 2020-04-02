#given a number print its factor

num = int(input("Give me a number:  "))

factors = []
neg_factors = []

#loop through 1 and the input number
for i in range(1, num):
    #determin if the iteration divided by the input number is divisiable cleanly ex. no remainder
    if num % i == 0:
        #if so, append the factor array
        factors.append(i)
        #the negative version of the number is also a factor, so append that array
        neg_factors.append(-i)
#the original number is a factor of itself
factors.append(num)
#the negative version is also a factor of itself
neg_factors.append(-num)


print(factors)
print(neg_factors)
