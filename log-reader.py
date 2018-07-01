import re
import numpy as np

#Abrir arquivo com o log
file = open('log.txt','r')

#Leitura do arquivo
log = file.read()

#Criação da regex para o request
regexp = r'(request_to=")([\w:/.]*)"'
regex_status = r'(response_status=")(\d*)"'
lista_request = []
lista_status = []

resultados_request = re.finditer(regexp, log)
resultados_status = re.finditer(regex_status, log)

# Coloca todos os requests em uma lista
for resultado in resultados_request:
    lista_request.append(resultado.group(2))

# Coloca todos os status em outra lista
for resultado in resultados_status:
    lista_status.append(resultado.group(2))

#Retira duplicatas
requests = np.unique(lista_request).tolist()
status = np.unique(lista_status).tolist()

#Inicializa contadores
contador_request = [None] * len(requests)
contador_status = [None] * len(status)

#Contagem de cada valor único
for index in range(len(requests)):
    contador_request[index] = lista_request.count(requests[index])
for index in range(len(status)):
    contador_status[index] = lista_status.count(status[index])


# Verificar mais chamadas
top = 3
mais_chamadas_url = top*[None]
mais_chamadas_freq = top*[None]

i = 0
while(i < top):
    maximo = max(contador_request)
    max_index = contador_request.index(maximo)
    mais_chamadas_url[i] = requests[max_index]
    mais_chamadas_freq[i] = contador_request[max_index]
    contador_request.remove(maximo)
    requests.remove(requests[max_index])
    i += 1

print("\n{} URLs mais chamadas:\n".format(top))
for x in range(len(mais_chamadas_url)):
    print("URL: {} - {} chamadas".format(mais_chamadas_url[x], mais_chamadas_freq[x]))

print("\n")
for x in range(len(status)):
    print("Status: {} - {} ocorrências".format(status[x], contador_status[x]))
