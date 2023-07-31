contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"] # {"nome": "Guilherme", "telefone": "3333-1234"}
copia["guilherme@gmail.com"] # {"nome": "Gui"}