from math import expm1


def pairs(open ,close):
    if open == '(' and close == ')':
        return True
    elif open == '[' and close == ']':
        return True
    elif open == '{' and close == '}':
        return True
    else:
        return False

def balanced(exp):
    stack = []
    for i in range(0,len(exp)):
        if exp[i] == '(' or exp[i] == '[' or exp[i] == '{':
            stack.append(exp[i])
        elif exp[i] == ')' or exp[i] == ']' or exp[i] == '}':
            if len(stack) > 0:
                if pairs(stack[-1],exp[i]):
                    stack.pop()
                else:
                    return False
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


exp1 = "[]{}()"
exp2 = "[]{})"

if balanced(exp1):
    print("balanced")
else:
    print('not balanced')