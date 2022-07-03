def fDisplayBinary(n):
    a = ''
    while n>0:
      lQuotient,lRemainder = divmod(n,2)
      n = lQuotient
      a +=str(lRemainder)
    return a[::-1] # reverse the string at the end
n = int(input("Enter the number you want to have binary display \n"))
print(fDisplayBinary(n))
