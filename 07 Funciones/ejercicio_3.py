import os

def validar_password(password):
    if len(password) < 8:
        return False
    
    numeros = sum(1 for char in password if char.isdigit())
    if numeros < 2:
        return False
    
    if not any(char.isupper() for char in password):
        return False
    
    if not any(char.islower() for char in password):
        return False
    
    return True


# Programa principal
def main():
    os.system('cls')
    password = input("Ingrese la nueva contraseña: ")
    
    if validar_password(password):
        print("La contraseña es valida")
    else:
        print("La contraseña no cumple con los requisitos de seguridad")


main();