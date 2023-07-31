contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3344-1234"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3355-1234"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3366-1234"},
}

"guilherme@gmail.com" in contatos # True
"megui@gmail.com" in contatos # False

"idade" in contatos["guilherme@gmail.com"] # False
"telefone" in contatos["giovanna@gmail.com"] # True