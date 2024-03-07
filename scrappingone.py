import requests
from bs4 import BeautifulSoup
import pandas

url = "https://www25.senado.leg.br/web/senadores/em-exercicio"
pag = requests.get(url)


soup = BeautifulSoup(pag.text,'html.parser')

data_senator = []
di_senator = []

table = soup.find_all("table", {"id" : "senadoresemexercicio-tabela-senadores"})

for element in table:
    rows = element.find_all("tr")

    for row in rows:
        cols = row.find_all("td", {"colspan" : ""})
        for col in cols:
            data_senator.append(col.text)    

for i in range(0, len(data_senator), 6):
    di_senator.append({})

    di_senator[-1]["Nome"] =      data_senator[i+0]
    di_senator[-1]["Partido"] =   data_senator[i+1]
    di_senator[-1]["UF"] =        data_senator[i+2]
    di_senator[-1]["Periodo"] =   data_senator[i+3]
    di_senator[-1]["Telefones"] = data_senator[i+4]
    di_senator[-1]["Email"] =     data_senator[i+5]

df = pandas.DataFrame(di_senator)
df.to_excel("planilha.xlsx", index=False)
