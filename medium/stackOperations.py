# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.8.10
    stack = []

    for op in S.split(' '):
        if op.isnumeric():
            stack.append(int(op))
        elif op == "DUP":
            try:
                dup = stack.pop()
                stack.append(dup)
                stack.append(dup)
            except:
                return -1
        elif op == "POP":
            try:
                stack.pop()
            except:
                return -1
        elif op == "+":
            try:
                f = stack.pop()
                s = stack.pop()
                if abs(f + s) > (2**20 - 1):
                    return -1
                else:
                    stack.append(f+s)
            except:
                return -1
        elif op == "-":
            try:
                f = stack.pop()
                s = stack.pop()
                if abs(f - s) > (2**20 - 1):
                    return -1
                else:
                    stack.append(f - s)
            except:
                return -1
    
    return stack.pop()

solution(' ')