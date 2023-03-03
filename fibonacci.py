def fibonacci(count):
    n1 = 0
    n2 = 1
    c = 0
    while c < count:
        print(n1)
        new = n1 + n2
        n1 = n2
        n2 = new
        c += 1
        

fibonacci(7)


