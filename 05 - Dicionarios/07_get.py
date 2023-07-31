# Segunda forma de acessar valores em um dicionario

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"}
}

contatos["chave"] # KeyError proposital

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("guilherme@gmail.com", {}) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"}}