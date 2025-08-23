# Verificador de senha “forte”

def verificar_senha_forte(senha):
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    if not any(char.isupper() for char in senha):
        return False
    if not any(char.islower() for char in senha):
        return False
    if not any(char in "!@#$%" for char in senha):
        return False
    return True

senha = input("Digite uma senha: ")
if verificar_senha_forte(senha):
    print("Senha forte.")
else:
    print("Senha fraca.")