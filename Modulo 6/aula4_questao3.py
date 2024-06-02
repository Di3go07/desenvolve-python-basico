horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25

pagamentos = [(n - 44) * hora_extra + (n) * ganho_por_hora if n > 44 else (n) * ganho_por_hora for n in horas_trabalhadas]

print(pagamentos)