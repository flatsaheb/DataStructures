'''
Expression Validation program would check the validity of expression
by checking the corresponding opening brace has closing brace. Stack data-structure
has been used to process the validation. Class CStack containing
basic stack operations has been used.
'''

import CPyStack

lStack = []
element = CPyStack.CStack(lStack)

# Class to implement validation function.
class CExprTest:
    def __init__(self,l_ExprArray):
        self.lExpr = l_ExprArray


    def fMatchChar(self,l_InitalChar,l_TerminalChar):
        if (l_InitalChar == '(' and l_TerminalChar == ')'):
            return 1
        elif (l_InitalChar == '{'and l_TerminalChar == '}'):
            return 1
        elif (l_InitalChar == '[' and l_TerminalChar == ']'):
         return 1
        else :
         return 0


    def fCheckExpression(self,l_ExprArray):
        for i in range(0,len(l_ExprArray)):
            if (l_ExprArray[i] == '(' or l_ExprArray[i] == '{' or l_ExprArray[i] == '['):
                element.fPush(lStack,l_ExprArray[i])
            if (l_ExprArray[i] == ')' or l_ExprArray[i] == '}' or l_ExprArray[i] == ']'):
                if element.fIsEmpty(lStack):
                    print('Error: Right symbols are more than Left')
                    return 0
                else:
                    lTempChar = element.fPop(lStack)
                    if (not self.fMatchChar(lTempChar,l_ExprArray[i])):
                        print('Error: Unmatched symbol found')
                        return 0

        if(element.fIsEmpty(lStack)):
            print('Stack is empty all open and close parenthesis match')
            return 1
        else:
            print('Stack is not empty open and close parenthesis not matching')
            return 0

def main():
    lExpression = list("(a+b)*(c-d)")
    lExprObj = CExprTest(lExpression)
    lValidity = lExprObj.fCheckExpression(lExpression)

    if (lValidity == 1):
        print("Expression is Valid")
    if (lValidity == 0):
        print("Expression is invalid")

if __name__ == "__main__":
    main()