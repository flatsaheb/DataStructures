lStack = []
top = None

def fIsEmpty(stk):
    if (stk==[]):
        return True
    else:
        return False

def fPush(stk,item):
    stk.append(item)
    top = len(stk)

def fPop(stk):
    if (fIsEmpty(stk)):
        return ('Underflow')
    else:
        i = stk.pop()
        if (len(stk) == 0):
            top = None
        else:
            top = len(stk) -1
        return i

def fPeek(stk):
    if (fIsEmpty(stk)):
        return 'Underfow'
    else:
        top = len(stk) - 2
        return(stk[top])

def fDisplay(stk):
    if (fIsEmpty(stk)):
        print ('Stack is Empty')
    else:
        top = len(stk)-1
        print(stk[top],'<---top')
        for i in range(top-1,-1,-1):
            print(stk[i])

def fMatchChar(l_InitalChar,l_TerminalChar):
    if (l_InitalChar == '(' and l_TerminalChar == ')'):
        return 1
    elif (l_InitalChar == '{'and l_TerminalChar == '}'):
        return 1
    elif (l_InitalChar == '[' and l_TerminalChar == ']'):
        return 1
    else :
        return 0
def fCheckExpression(l_ExprArray):
    for i in range(0,len(l_ExprArray)):
        if (l_ExprArray[i] == '(' or l_ExprArray[i] == '{' or l_ExprArray[i] == '['):
            fPush(lStack,l_ExprArray[i])
        if (l_ExprArray[i] == ')' or l_ExprArray[i] == '}' or l_ExprArray[i] == ']'):
            if fIsEmpty(lStack):
                print('Error: Right symbols are more than Left')
                return 0
            else:
                lTempChar = fPop(lStack)
                if (not fMatchChar(lTempChar,l_ExprArray[i])):
                    print('Error: Unmatched symbol found')
                    return 0
    if(fIsEmpty(lStack)):
        print('Stack is empty all open and close paranthesis match')
        return 1
    else:
        print('Stack is not empty open and close paranthesis not matching')
        return 0


lExprArray = list("(a+b)*({c-d})")
lValidity = fCheckExpression(lExprArray)
if (lValidity == 1):
    print("Expression is Valid")
if (lValidity == 0):
    print("Expression is invalid")












