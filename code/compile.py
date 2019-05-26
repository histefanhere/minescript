file_name = "example.txt"

file = open(file_name, "r")
code = ""
def interpret_line_for_comments(line):
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
                code += char
            else:
                if char == "#":
                    code += "\n" if i != 0 else ""
                    return
                code += char
        i += 1

for line in file:
    interpret_line_for_comments(line)



file.close()

print(code)
