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
while True:
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display')
    print('5. Exit')
    print('\n \n')

    ch = int(input('Enter the choice 1-5'))
    if (ch == 1):
        item = int(input("Enter the item you want to push"))
        fPush(lStack,item)
        print('%d added sucessfully'%item)
        input('Press any key to continue')

    elif(ch == 2):
        item = fPop(lStack)
        if (item == 'Underflow'):
            print ('Stack is empty')
        else:
            print ('%d is popped'%item)
        print ('Press any key to continue')

    elif(ch == 3):
        item = fPeek(lStack)
        if (item == 'Underflow'):
            print ('Stack is empty')
        else:
            print('%d is at the top'%item)

    elif(ch == 4):
        fDisplay(lStack)
        input('Press any key to continue')

    elif(ch == 5):
        break

    else:
         print('Wrong Input. \n')
         print ('Please give input between 1 to 5 \n')















