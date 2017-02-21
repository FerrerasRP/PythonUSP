
try:
    arquivo_entrada = open('/home/ricardo/Documentos/COURSERA/PythonUSP/arquivo_exemplo.txt','r')
    
    arquivo_saida = open('/home/ricardo/Documentos/COURSERA/PythonUSP/arquivo_saida.txt','w')
    
    
    for linha in arquivo_entrada:
        coluna = linha.split(sep=';')
        
        print(coluna[0],coluna[4],coluna[1],coluna[2], sep='|', file=arquivo_saida)
        
    arquivo_entrada.close()
    arquivo_saida.close()

except IOError:
    print("Erro no arquivo")
