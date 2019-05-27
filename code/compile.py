import utilities as util
import sys
import structure as struct

file_name = "../testfiles/test_structure.txt"

file = open(file_name, "r")
code = ""
def interpret_line(line):
    """get rid of comments (properly) and put the whole thing into one line in code"""
    global code
    mode = "code"
    i = 0
    for char in line:
        if char == "\"":
            util.toggle_var(mode, ["code", "text"])
            code += char
        else:
            if mode == "text":
                if char != "\n":
                    code += char
            else:
                if char == "#":
                    return
                code += char
        i += 1

for line in file:
    interpret_line(line.strip())
file.close()

#TODO: here check if brackets are balanced

objects = []
# Now I'll go through and find the seperate "objects" in the code
mode = "code"
cur_object = ""
operation = ""
children = ""
i = 0
while i < len(code):
    char = code[i]
    if char == "\"":
        mode = util.toggle_var(mode, ["code", "text"])
        continue
    else:
        if mode == "text":
            cur_object += char
        elif mode == "code":

            if char == ";":
                # reached end of command
                objects.append(struct.Object(cur_object, operation, children))
                cur_object, operation, children = "", "", ""
            elif char == "{":
                stack = util.Stack()
                stack.push("{")
                i += 1
                internal_command = ""
                while True:
                    if i == len(code):
                        raise EOFError("Unbalanced \{ and \} brackets, please check syntax")
                        sys.exit()
                    if code[i] == "{":
                        stack.push("{")
                    elif code[i] == "}":
                        stack.pop("Unbalanced \{ and \} brackets, please check syntax")
                    else:
                        internal_command += code[i]
                    if len(stack.stack) == 0:
                        break
                    i += 1

                operation = cur_object
                children = internal_command

            else:
                cur_object += char
                

    i += 1
    if i == len(code):
        objects.append(struct.Object(cur_object, operation, children))
        cur_object, operation, children = "", "", ""

for thing in objects:
    print(f"cur_object: {thing.cur_object}\noperation: {thing.operation}\nchildren: {thing.children}\n")