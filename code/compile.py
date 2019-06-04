import utilities as util
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

keywords = ["var", "=", "if"]
after_keywords = {"var":"label", "label":"operator", "=":"value", "if":"condition", "condition":"innercode", "operator":"value"}
minecraft_commands = ["tellraw", "say", "execute"]
brackets = {"condition":"(", "innercode":"{"}
end_brackets = {"(":")", "{":"}"}

def lexerize(code_):
    print("started new loop")
    print(f"the data I have to deal with is \"{code_}\"")
    tokens = []
    mode = ""
    data = ""
    typ = ""
    stack = util.Stack()
    i = 0
    while i < len(code_):
        char = code_[i]
        # we're looking at a something that needs to be in a stack!
        if typ in brackets:
            if len(stack.s) == 0 and char != " ":
                # beginning of stack
                if char == brackets[typ]:
                    # impossible for there to be an error here because we know it's the start of the stack
                    stack.push(char, "")
                    i += 1
                    isdisastring = False
                    while len(stack.s) != 0:
                        if code_[i] == "\"":
                            if isdisastring:
                                isdisastring = False
                            else:
                                isdisastring = True
                        data += code_[i]
                        i += 1
                        if code_[i] in ("(", "{", "}", ")", "[", "]") and not isdisastring:
                            stack.push(code_[i], "Unbalanced brackets")

                    sub_data = data.strip() if data.strip()[-1] == ";" else data.strip() + ";"
                    tokens.append({"type":typ, "value":lexerize(sub_data)})
                    # typ = after_keywords[typ]
                    stack = util.Stack()
                    if typ in after_keywords:
                        typ = after_keywords[typ]
                    else:
                        typ = ""
                    data = ""

                else:
                    raise SyntaxError("Unpropper starting bracket")

        elif char == ";" and typ == "minecraft_command":
            tokens.append({"type":typ, "value":data})
            typ = ""
            data = ""

        elif typ == "minecraft_command":
            data += char

        elif char == "\"":
            if typ != "string":
                typ = "string"
            else:
                typ = "code"
                tokens.append({"type":"char", "value":data})
                data = ""

        elif typ == "string":
            data += char

        elif char == " " and typ == "":
            if data in keywords:
                tokens.append({"type":"keyword", "value":data})
                typ = after_keywords[data]
                data = ""

            elif data in minecraft_commands:
                typ = "minecraft_command"
                data += char

            else:
                # data is a user defined label
                tokens.append({"type":"label", "value":data})
                typ = after_keywords["label"]
                data = ""

        elif char == " " or char == ";":
            tokens.append({"type":typ, "value":data})
            data = ""
            typ = ""


        else:
            data += char

        # debugging
        #print(tokens, data, typ)
        #input("continue:")
        i += 1
    return tokens

objects = lexerize(code)
print(objects)
