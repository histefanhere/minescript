while i < len(code):
    char = code[i]
    print(char)
    if char == "\"":
        mode = util.toggle_var(mode, ["code", "text"])
        continue
    else:
        if mode == "text":
            cur_object += char
        elif mode == "code":
            # if we still don't know what we're dealing with
            if typ == "":
                # The information we have available up untill the first space must be enough to determine what we have
                # e.g. "execute", "say", "tp" or "if", etc
                if char == " ":
                    if cur_object in ("if"):
                        typ = "minescipt_control_statement"
                        if code[i + 1] != "(":
                            raise SyntaxError(f"Expected \"(\" after control statement, got \"{code[i+1]}\" instead.")
                        else:
                            stack = util.Stack()
                            stack.push("(")
                            i += 2
                            internal_condition = ""
                            while True:
                                print("reading",code[i])
                                if code[i] == "(":
                                    stack.push("(")
                                elif code[i] == ")":
                                    stack.pop()
                                else:
                                    # ignore spaces in the internal condition
                                    if code[i] != " ":
                                        internal_condition += code[i]
                                if len(stack.stack) == 0:
                                    break
                                i += 1
                            print("done the loop!")
                            operation = internal_condition
                            print(operation)

                            while True:
                                i += 1
                                if code[i] == "("

   i += 1
   input("continue: ")

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