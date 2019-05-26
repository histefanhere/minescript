file_name = "example.txt"

file = open(file_name, "r")
code = ""
def interpret_line_for_comments(line):
    global code
    for char in line:
        if char == "#":
            return
        else:
            code += char

for line in file:
    interpret_line_for_comments(line)



file.close()

print(code)