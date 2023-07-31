# Sort é para ordenar a lista

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort() # ['c', 'csharp', 'java', 'js', 'python'] ALFABETICAMENTE PADRÃO

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(reverse=True) # ['python', 'js', 'java', 'csharp', 'c'] ALFABETICAMENTE INVERSO

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(key=lambda x: len(x)) # ['c', 'js', 'java', 'python', 'csharp'] Ordenando pelo tamanho da palavra, do menor ao maior (lambda é uma função anonima)

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(key=lambda x: len(x), reverse=True) # ['python', 'csharp', 'java', 'js', 'c'] O mesmo de cima, porém espelhado