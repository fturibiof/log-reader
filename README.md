# log-reader

Task

O arquivo de log contém informações de envio de webhooks no format:
level=info response_body="" request_to"url" response_headers=
response_status="code"  

Onde:  
* Url: é a url para onde foi enviado o webhook  
* code: é o status code retornado pelo servidor do cliente  

Foi importado o Regular Expression Engine do python e utilizadas as expressões:</br>
* (request_to=")([\w:/.]*)" para capturar a URL da requisição
* (response_status=")(\d*)" para capturar o status do servidor do cliente

Para o log.txt utilizado como exemplo, o arquivo log-reader.py retorna:

3 URLs mais chamadas:

URL: https://eagerhaystack.com - 750 chamadas

URL: https://surrealostrich.com.br - 734 chamadas

URL: https://grimpottery.net.br - 732 chamadas


Status: 200 - 1417 ocorrências

Status: 201 - 1402 ocorrências

Status: 204 - 1388 ocorrências

Status: 400 - 1440 ocorrências

Status: 404 - 1474 ocorrências

Status: 500 - 1428 ocorrências

Status: 503 - 1451 ocorrências
