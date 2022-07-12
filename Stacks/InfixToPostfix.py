'''
Infix to Postfix Conversion. Stack class CStack would be used for stack operations. isalpha function would
be used to check whether the processing character is operand.
'''
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

    # Scan the string using for loop. String would pass as an array.
    for i in range(0, len(l_Array)):
        # If it is an operand output it to expression.
        if isalpha(l_Array[i]):
            lPostFix = lPostFix + l_Array[i]
        # Else If it is a left opening bracket then Pop all the elements and add them to expression
        elif l_Array[i] == ")":
           while True:
                lPoppedElement = OElement.fPop(lStack)
                if lPoppedElement == '(':
                    break
                else:
                    lPostFix = lPostFix + lPoppedElement
        # Else If it is a right opening bracket then simply push to stack.
        elif l_Array[i] == "(":
            OElement.fPush(lStack,l_Array[i])

        # Else  Compare the priorities of operands, if priority of operand on top of the stack is higher
        # than one being processed then pop the item from stack and add to expression.
        # Lastly push the processed operand.
        else:
            if OElement.fPeek(lStack) != 'Underflow':
                 if fPriority(OElement.fPeek(lStack)) >= fPriority(l_Array[i]):
                     lPoppedElement = OElement.fPop(lStack)
                     lPostFix = lPostFix + lPoppedElement
            OElement.fPush(lStack, l_Array[i])
    # When entire infix string processed then pop the items from stack and add to the
    # expression.
    while not OElement.fIsEmpty(lStack):
        lPostFix = lPostFix + OElement.fPop(lStack)
    return lPostFix


print(fOutputPostfix(list("A*B-(C+D)+E")))
print(fOutputPostfix(list("A*(B+C)")))