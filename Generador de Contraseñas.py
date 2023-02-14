import secrets
import string
import os
def clear():
    # PARA LIMPIAR LA CONSOLA PARA WINDOWS
    if os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
    # PARA LIMPIAR LA CONSOLA PARA DISTRIBUCIONES LINUX
    elif os.name == "posix":
        os.system("clear")
Letras = string.ascii_letters
Numeros = string.digits
Simbolos = string.punctuation
clear();
print("\n\n\t  GENERADOR DE CONTRASEÑAS EN PYTHON\n\n")
Total = ''
A_Letras = str(input("    01.- AGREGAR LETRAS (Y/N): "))
if (A_Letras == 'y' or A_Letras == 'Y'):
    Total = Letras
A_Numeros = str(input("    02.- AGREGAR NUMEROS (Y/N): "))
if (A_Numeros == 'y' or A_Numeros == 'Y'):
    Total = Total + Numeros
A_Simbolos = str(input("    03.- AGREGAR SIMBOLOS (Y/N): "))
if (A_Simbolos == 'y' or A_Simbolos == 'Y'):
    Total = Total + Simbolos
N_Caracteres = int(input("\n    04.- NUMEROS DE CARACTERES: "))
N_Contrasenas = int(input("    05.- NUMEROS DE CONTRASEÑAS: "))
print("\n")
for j in range(N_Contrasenas):
    F_Contrasenas = ''
    for i in range(N_Caracteres):
        F_Contrasenas += ''.join(secrets.choice(Total))
    print("\n\t",F_Contrasenas)
print("\n")
