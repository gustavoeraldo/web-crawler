# Company Analyser



## Data We want

- Ativo (nome da ação)

- Tipo da ação

- Setor

- Cotação ou Valor atual 

- Alta do dia

- Baixa do dia

- P\L

- Lucro nos últimos 12 meses

- Margem líquida > 15%

- ROE > 15%

- ROIC > 10%	

- Div Yield > 5%

- Divida líquida/EBITDA <1,5-3%

- Patrimônio Líquido


## Lib to install 

For crawling data you can use scrapy lib.
Installing using PyPI :<br>
```
pip install Scrapy
```
You can get more information on the [documentation](https://docs.scrapy.org/en/latest/index.html).

 
## Creating a project with scrapy


```
scrapy crawl spider_name - my_data.json
```

## How to run

You can run individually using the command below:
```
scrapy runspider scraper.py
```

Or you will be able to run your current project:
```
scrapy crawl spider_name
```

## How storage data scraped

You can save data into json file :
```
scrapy crawl spider_name -o my_data.json
```
If you run the command above more than once, your json file can have some issues appending new data. So you can save your data into a **Json Line** file following the command :

```
scrapy crawl spider_name -o my_data.jl
```

