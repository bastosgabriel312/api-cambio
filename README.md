# api-cambio

## Tecnologias utilizadas (Docs)
  * Python 3 (https://docs.python.org/3.8/)
  * API Awesome (https://docs.awesomeapi.com.br/api-de-moedas)
  * Flask (https://flask.palletsprojects.com/)
  
## Awesome API
### API de cotações de moedas.

### Foi criada uma classe para realizar consultas e retornar os resultados da API.
``` 
# Disponível no arquivo cambio.py
class Cambio():
    def __init__(self):
        self.url = "https://economia.awesomeapi.com.br/json"
```

### É possível utilizar tambem em (https://cambio.pythonanywhere.com/)
