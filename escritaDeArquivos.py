# Estudo sobre escrita em arquivos

# Abre o arquivo "novo_poema.txt" em modo de escrita ("w")
# Se o arquivo não existir, ele será criado.
# Se já existir, seu conteúdo será apagado.
arquivo = open("novo_poema.txt", "w")

# Escreve linhas no arquivo
arquivo.write("No meio do caminho tinha uma pedra\n")
arquivo.write("tinha uma pedra no meio do caminho\n")

# Fecha o arquivo
arquivo.close()

print("Arquivo 'novo_poema.txt' criado e escrito com sucesso!")
