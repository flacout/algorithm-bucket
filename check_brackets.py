# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def IsBalanced(text):
    stack = []
    index_stack =[]
    index_close_bracket = 0
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            stack.append(next)
            index_stack.append(i+1)
        elif next == ')' or next ==']' or next=='}' :
            index_close_bracket = i+1
            if len(stack)==0 : 
                return index_close_bracket
            top = stack.pop()
            _ = index_stack.pop()
            if ( (top=='[' and next!=']') or 
                 (top=='(' and next!=')') or 
                 (top=='{' and next!='}') ) :
                return index_close_bracket
    if len(stack)==0 : return "Success"
    else : return index_stack.pop()


if __name__ == "__main__":
    text = sys.stdin.read()
    print (IsBalanced(text))
