#first 100 triangle numblers
#rule: n(n+1) / 2 
#n is the number of dots in triangle

count = 1

while count < 101:
    tri = count * (count + 1) / 2
    print(tri)
    count += 1