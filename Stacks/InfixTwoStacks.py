'''
Infix expression evaluation using two stacks viz. Operand Stack and Operator Stack. Operand stack holds operands and
Operator stack holds operators.
Until the end of the expression is reached, get one character and perform only one of the steps (1) through (5):
1. If the character is an operand, push it onto the operand stack.
2. If the character is “(“, then push it onto the operator stack.
3. If the character is “)”, then “process” as explained above until the corresponding “(” is encountered in the operator
   stack. At this stage POP the operator stack and ignore “(.”
4. If we encounter an operator
    4.1 If the operator stack is empty then push the operator onto the operator stack.
    4.2 If the operator stack is not empty and the operator’s precedence is greater than the precedence of the stack top
        of the operator stack, then push the character onto the operator stack.
    4.3 If the operator stack is not empty and the character’s precedence is lower than the precedence of the stack top
        of operator stack then we pop the operator with high precedence, and two values from the value stack, apply the
        operator to the values and store the result in the value stack. And, push the current iterated operator in the
        operator stack.
5.  Once we have iterated the entire expression, we pop one operator from the operator stack and two values from the
    value operator and apply the operator to the values, store the result in the value stack, and keep on repeating
    this, until we have just a single value left in the value stack.
The last value in the value stack will be the result.
'''

import CPyStack

lOperatorStack = []
lOperandStack = []
OOperator = CPyStack.CStack(lOperatorStack)
OOperand = CPyStack.CStack(lOperandStack)


class InfixEvaluation:
    def __init__(self):
        pass

    @staticmethod
    # Function to evaluate operator precedence.
    def fOperatorPrecedence(l_Operator):
        if l_Operator == '*' or l_Operator == '/':
            return 2
        elif l_Operator == '-' or l_Operator == '+':
            return 1
        elif l_Operator == '(':
            return 0

    @staticmethod
    # Function to evaluate the expressions based on two operands and operator and also push the second operator.
    # Function overloaded to evaluate when there is only one operator is present.
    def fOperateOnItems(l_Operand1, l_Operand2, l_Operator1, l_Operator2 = None):
        lTotal = str(l_Operand1) + str(l_Operator1) + str(l_Operand2)
        if l_Operator2:
            OOperator.fPush(lOperatorStack, l_Operator2)
        OOperand.fPush(lOperandStack, eval(lTotal))

    # Function to scan the input expression and push the operands and operators accordingly.
    #
    def fInfixEval(self, l_Array):
        for i in range(0,len(l_Array)):
            if l_Array[i].isnumeric():
                OOperand.fPush(lOperandStack, l_Array[i])
            else:
                if OOperator.fIsEmpty(lOperatorStack) or l_Array[i] == '(':
                    OOperator.fPush(lOperatorStack,l_Array[i])
                elif l_Array[i] == ')':
                    while True:
                        if OOperator.fPeek(lOperatorStack) != '(':
                            self.fOperateOnItems(OOperand.fPop(lOperandStack), OOperand.fPop(lOperandStack),
                                                 OOperator.fPop(lOperatorStack), None)
                        else:
                            OOperator.fPop(lOperatorStack)
                            break
                elif self.fOperatorPrecedence(OOperator.fPeek(lOperatorStack)) < self.fOperatorPrecedence(l_Array[i]):
                    OOperator.fPush(lOperatorStack,l_Array[i])
                else:
                    self.fOperateOnItems(OOperand.fPop(lOperandStack),OOperand.fPop(lOperandStack),
                                         OOperator.fPop(lOperatorStack), l_Array[i])

        lOutput = None
        while True:
            if not OOperator.fIsEmpty(lOperatorStack):
                lOutput = str(OOperand.fPop(lOperandStack)) + str(OOperator.fPop(lOperatorStack)) \
                          + str(OOperand.fPop(lOperandStack))
                OOperand.fPush(lOperandStack,eval(lOutput))
            else:
                break
        if not lOutput:
            lOutput = str(OOperand.fPeek(lOperandStack)) + ''

        return eval(lOutput)

def main():
    lExpression = list("(1+1)*(5+2)")
    OInfixEval = InfixEvaluation()
    print('Output is {}'.format(int(OInfixEval.fInfixEval(lExpression))))
    print('Final value on stack {} '.format(OOperand.fPeek(lOperandStack)))

    lExpression2 = list("3+4*2")
    OInfixEval2 = InfixEvaluation()
    print('Output without round braces {}'.format(int(OInfixEval2.fInfixEval(lExpression2))))
    print('Final value on stack without round braces {} '.format(OOperand.fPeek(lOperandStack)))

if __name__ == "__main__":
    main()