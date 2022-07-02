def f_Fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        print ("Factorial value is {}".format(n))
        return(n*f_Fact(n-1))

print (f_Fact(0))

