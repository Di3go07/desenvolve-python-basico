from datetime import date
from datetime import datetime


data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
data_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
hora_em_texto = data_e_hora_atuais.strftime('%H:%M')


print(f'Data: {data_em_texto}')
print(f'Hora: {hora_em_texto}')