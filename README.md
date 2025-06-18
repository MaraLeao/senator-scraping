# senator-scraping

## Introdução
Script em Python para realizar web scraping de informações de senadores brasileiros, estruturando os dados em uma planilha .xlsx com os seguintes campos: Nome, Partido, UF, Período, Telefones e E-mail. Ideal para análises, integrações com dashboards ou estudos acadêmicos.

## Tecnologias usadas
- ``Python 3``
- ``Requests``
- ``BeautifulSoup (bs4)``
- ``Pandas``

Caso ainda não tenha essas bibliotecas instaladas, você pode instalar com:

``` bash 
pip install requests beautifulsoup4 openpyxl
```

## Como usar
1. Clone o repositório
``` bash
git clone https://github.com/MaraLeao/senator-scraping.git
```

``` bash
cd senator-scraping
```

2. Execute o script
``` bash
python main.py
```

3. A planilha ``planilha.xlsx`` será gerada na mesma pasta.

## Exemplo de saída

| Nome            | Partido |  UF    | Periodo     | Telefone       | Email                                               |
| --------------- | ------- | ------ | ----------- | -------------- | --------------------------------------------------- |
| Fulano da Silva | ABC     | SP     | 2023 - 2031 | (61) 3210-1234 | [fulano@senado.leg.br](mailto:fulano@senado.leg.br) |
