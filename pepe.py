from os import system
var1 = 2
var2 = 4

name = input("Pon tu nombre: ")
system("cls")
def suma(var1, var2):
    var3 = var1 + var2
    return var3


print("Hola mundo " + str(suma(var1, var2)) + " " +name)