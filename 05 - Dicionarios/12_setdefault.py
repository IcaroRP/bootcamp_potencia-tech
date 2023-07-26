contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"}
}

contatos.setdefault("nome", "giovanna") # "Guilherme"
contatos.setdefault("idade", 28) # {"nome": "Guilherme", "telefone": "3333-1234", "idade": 28}