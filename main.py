import mysyn

data = ""
while True:
    x = input()
    if x.endswith(';'):
        data += "\n"+x
        break
    else:
        data += "\n"+x
print(data)
mysyn.parser.parse(data)
