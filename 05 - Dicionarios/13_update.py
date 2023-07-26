contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos # {"guilherme@gmail.com": {"nome": "Gui"}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
contatos # {"guilherme@gmail.com": {"nome": "Gui"}, {"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}}}