
'''
Stack class implements the basic stack operations. It's functions
can be used in various programs. fPush and fPop functions would be
used to insert and delete the stack elements.
'''
class CStack:
    def __init__(self, stk):
        self.top = None
        self.stk = stk

    def fIsEmpty(self,stk):
        if stk == []:
            return True
        else:
            return False

    def fPush(self, stk, item):
        stk.append(item)
        top = len(stk)

    def fPop(self,stk):
        if self.fIsEmpty(stk):
            return 'Underflow'
        else:
            i = stk.pop()
            if len(stk) == 0:
                top = None
            else:
                top = len(stk) - 1
            return i

    def fPeek(self,stk):
        if self.fIsEmpty(stk):
            return 'Underflow'
        else:
            top = len(stk) - 2
            return stk[top]

    def fDisplay(self,stk):
        if self.fIsEmpty(stk):
            print('Stack is Empty')
        else:
            top = len(stk) - 1
            print(stk[top], '<---top')
            for i in range(top - 1, -1, -1):
                print(stk[i])