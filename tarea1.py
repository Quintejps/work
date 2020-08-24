chain = "5-6+7+9"

estado = 1

for x in chain:
    if estado == 1:
        if x.isdigit(): estado = 2
        else: estado = 4
    elif estado == 2:
        if x.isdigit(): estado = 2
        elif x == "+" or x == "-": estado = 3
        else: estado = 4
    elif estado == 3:
        if x.isdigit(): estado = 2
        elif x == "+" or x == "-": estado = 4
        else: estado = 4
    elif estado == 4:
        estado = "error"

if estado == 2:
    print ("OK")
else:
    print ("ERROR")



