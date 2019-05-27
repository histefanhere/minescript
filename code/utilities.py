import sys
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, i):
        self.stack.append(i)

    def pop(self, error=None):
        try:
            self.stack.pop()
        except:
            raise SyntaxError(error)
            sys.exit()


def toggle_var(var, states):
    i = states.index(var) + 1
    if i >= len(states):
        i = 0
    return states[i]
