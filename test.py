import pandas as pd
import json_lines
import numpy as np

if __name__ == "__main__":
	
	path = '/home/gustavo/Documentos/ShowOff/WebCrawler/quotesproject/datamoney.jl'

	a = []
	with open(path,'rb') as f:
		for i in json_lines.reader(f):
			a.append(i['data'])
			#print(i['data'])

	labels = ['Papel', 'Cotação', 'Tipo', 'Setor', 'P/L', 'Marg. Líquida', 'ROIC', 'Div. Yield', 'ROE', 'Dív. Líquida', 'Patrim. Líq'] 
	data = []
	
	for i in labels:
		x = a.index(i)+1
		if '\n' in a[x]:         			
			aux = a[x].split("\n          ", 1)
			data.append(aux[1])
		else:
			data.append(a[x])
		
	b = np.array(data)	
	b = np.reshape(b, (1,len(b)))
	
	df = pd.DataFrame(b, columns=labels)
	df.to_csv('novo.csv',index=False)
	print(df)
	