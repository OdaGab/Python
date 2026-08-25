
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valorFixo = float(input("Salário Fixo: "))
totalVendido = float(input("Total Vendido: "))

comissao = totalVendido * 0.4
print(locale.currency(comissao, grouping=True, international=False))

salarioAtual = comissao + valorFixo
print(locale.currency(salarioAtual, grouping=True, international=False))