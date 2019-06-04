import sys

open_brackets = ["(", "{", "["]
closed_brackets = [")", "}", "]"]

class Stack:
    def __init__(self):
        self.s = []

    def push(self, i, error):
        self.s.append(i)
        if self.s[-1] in closed_brackets:
            if len(self.s) >= 2:
                if self.s[-2] in open_brackets:
                    if closed_brackets.index(self.s[-1]) == open_brackets.index(self.s[-2]):
                        self.s.pop()
                        self.s.pop()
                    else:
                        raise SyntaxError(error)
                else:
                    raise SyntaxError(error)
            else:
                raise SyntaxError(error)

    # def pop(self, error=None):
    #     if len(self.s) == 0:
    #         raise SyntaxError(error)
    #         sys.exit()
    #     else:



def toggle_var(var, states):
    i = states.index(var) + 1
    if i >= len(states):
        i = 0
    return states[i]
