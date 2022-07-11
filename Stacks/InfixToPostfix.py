from curses.ascii import isalpha
import CPyStack

lStack = []
OElement = CPyStack.CStack(lStack)

def fPriority(l_Operator1):
    if l_Operator1 == '(':
        return 0
    if l_Operator1 == '+' or l_Operator1 == '-':
        return 1
    if l_Operator1 == '/' or l_Operator1 == '*':
        return 2

def fOutputPostfix(l_Array):
    lPostFix = ''
    lPoppedElement = ''

    for i in range(0, len(l_Array)):
        if isalpha(l_Array[i]):
            lPostFix = lPostFix + l_Array[i]
        elif l_Array[i] == ")":
           while True:
                lPoppedElement = OElement.fPop(lStack)
                if lPoppedElement == '(':
                    break
                else:
                    lPostFix = lPostFix + lPoppedElement
        elif l_Array[i] == "(":
            OElement.fPush(lStack,l_Array[i] )
        else:
            if OElement.fPeek(lStack) != 'Underflow':
                 if fPriority(OElement.fPeek(lStack)) >= fPriority(l_Array[i]):
                     lPoppedElement = OElement.fPop(lStack)
                     lPostFix = lPostFix + lPoppedElement
            OElement.fPush(lStack, l_Array[i])

    while not OElement.fIsEmpty(lStack):
        lPostFix = lPostFix + OElement.fPop(lStack)
    return lPostFix


print(fOutputPostfix(list("A*B-(C+D)+E")))
#print(fOutputPostfix(list("A*(B+C)-D")))
print(fOutputPostfix(list("A*(B+C)")))