file_name = "../testfiles/test_structure.txt"

def toggle_var(var, states):
    i = states.index(var) + 1
    if i >= len(states):
        i = 0
    return states[i]

file = open(file_name, "r")
code = ""
def interpret_line(line):
    """get rid of comments (properly) and put the whole thing into one line in code"""
    global code
    mode = "code"
    i = 0
    for char in line:
        if char == "\"":
            if mode == "code":
                mode = "text"
            else:
                mode = "code"
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

objects = []
# Now I'll go through and find the seperate "objects" in the code
mode = "code"
cur_object = ""
for char in code:
    if char == "\"":
        mode = toggle_var(mode, ["code", "text"])
        continue
    else:
        if mode == "text":
            cur_object += char
        elif mode == "code":

            if char != ";":
                cur_object += char
            else:
                
