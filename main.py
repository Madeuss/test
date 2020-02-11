import CRUD as c

print("*******MENU*******\n")
print("1-Select")
print("2-Insert")
print("3-Update")
print("4-Delete")
print("5-Exit")

opc = int(input("Select the desired option: "))

if opc == 1:
    print("\n--Select--")
    fields = input("Fields(* for all): ")
    tables = input("Table: ")
    where = input("Where: ")
    see = c.select(fields, tables, where)
    print(see)
elif opc == 2:
    print("\n--Insert Into--")
    table = input("Table: ")
    fields = input("Field: ")
    values = input("Values: ")
    put = c.insert(values, table, fields)
elif opc == 3:
    print("\n--Update--")
    table = input("Table: ")
    sets = input("Sets: ")
    where = input("Where: ")
    up = c.update(sets, table, where)
elif opc == 4:
    print("\n--Delete--")
    table = input("Table: ")
    where = input("Where: ")
    delete = c.delete(table, where)
elif opc == 5:
    exit(0)
else:
    print("Invalid Option")