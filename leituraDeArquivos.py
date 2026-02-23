# Abre o arquivo "poema.txt" em modo de leitura ("r")
arquivo = open("poema.txt", "r")

# Lê e imprime todo o conteúdo do arquivo
print(arquivo.read())

# Fecha o arquivo para liberar os recursos do sistema
arquivo.close()