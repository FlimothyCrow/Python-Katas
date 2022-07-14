def mockCase(string):
    new_quote = ""
    i = False
    for char in string:
        if i:
            new_quote += char.upper()
        else:
            new_quote += char.lower()
        if char != ' ':
            i = not i
    return new_quote
# call mockcase from a front end and autoclipboard for faster mockery
print(mockCase("sorry i know i'm a bad friend"))