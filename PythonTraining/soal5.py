a = 2

for i in range (1,6):
    b = i 
    for j in range (5):
        print(b, end=" ")
        b += a
    a += 1
    print( )