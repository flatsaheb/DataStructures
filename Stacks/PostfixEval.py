'''
This program evaluates Postfix expression. Result of evaluation would be pushed to stack.
Stack class used to perform various stack operations.
'''
# Import Stack Class.
import CPyStack
class PostfixEval:
    def __init__(self):
        self.lStack = []
        self.OElement = CPyStack.CStack(self.lStack)

    def fPostFixProcessing(self, l_Array):
        for i in range(0,len(l_Array)):
            # If operand is numeric value then push it to stack
            if l_Array[i].isnumeric() == True:
                self.OElement.fPush(self.lStack, l_Array[i])
            # If operand is operator then pop last two values from stack and perform the
            # arithmetic operation and push result to stack
            else:
                lItem1 = self.OElement.fPop(self.lStack)
                lItem2 = self.OElement.fPop(self.lStack)
                lOutput = str(lItem2) + str(l_Array[i]) + str(lItem1)
                # eval function takes strings parameters and evaluate the arithmetic operations.
                self.OElement.fPush(self.lStack, eval(lOutput))
        return self.OElement.fPeek(self.lStack)

def main():
    lExpression = "123*+5-"
    lExpressionArray = list(lExpression)
    OPostFix = PostfixEval()
    print('Postfix Evaluation of string {} is  --> {}'.format(lExpression, OPostFix.fPostFixProcessing(lExpressionArray)))

if __name__ == "__main__":
    main()