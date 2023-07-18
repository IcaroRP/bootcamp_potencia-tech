#Também serve para ordenar

linguagens = ['python', 'js', 'c', 'java', 'csharp']

sorted(linguagens, key=lambda x: len(x)) # ['c', 'js', 'java', 'python', 'csharp']

sorted(linguagens, key=lambda x: len(x), reverse=True) # ['python', 'csharp', 'java', 'js', 'c']