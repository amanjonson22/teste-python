import json
import getpass as gp
import hashlib as hl
import os

def hash_password(password):
    hashed_pass = hl.sha256(password.encode('utf-8')).hexdigest()
    return hashed_pass

senhas = []
checked = False

while True:
    decisão = input("Quer guardar senha? (Y/N/abrir) ").upper()
    
    if decisão == "ABRIR":

        if os.stat("senhas.json").st_size != 0:
            with open("senhas.json", "r") as json_data:
                senhas = json.load(json_data)

        else:
            print("Nenhuma senha no arquivo")

        senha_escolhida = gp.getpass("Qual a senha? ")
        senha_escolhida_hash = hash_password(senha_escolhida)

        senha_escolhida_certa = False

        for senha in senhas:
            if senha_escolhida_hash == senha["senha"]:
                print("A senha está correta")
                senha_escolhida_certa = True
                break
        
        if senha_escolhida_certa == False:
            print("Senha incorreta ou não existente")

    elif decisão != "N":

        if os.stat("senhas.json").st_size != 0 and checked == False:
            with open("senhas.json", "r") as arquivo:
                senhas = json.load(arquivo)
            
            checked = True

        password = gp.getpass("Digite a senha: ")
        hashed_pass = hash_password(password)

        senha = {f"senha" : hashed_pass}

        senhas.append(senha)

    else:

        with open("senhas.json", "w") as arquivo:
            json.dump(senhas, arquivo)

        break

