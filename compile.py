file_name = "example.txt"

file = open(file_name, "r")
code = ""
def interpret_line_for_comments(line):
    global code
    mode = "code"
    for char in line:
        if char == "\"":
            if mode == "code":
                mode == "text"
            else:
                mode = "code"
            code += char
        else:
            if mode == "text":
                code += char
            else:
                if char == "#" or char == " ":
                    return
                code += char

for line in file:
    interpret_line_for_comments(line)



file.close()

print(code)