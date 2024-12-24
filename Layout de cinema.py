import os
os.system ('cls')
import colorama
from colorama import Fore,Back,Style
import rich
from rich.console import Console
from rich.table import Table

print('='*45)
print(Fore.LIGHTWHITE_EX+'🌟 Seja Bem vindo ao cinema Boulevard 🌟')
print('='*45)


print('='*45)
print(Fore.LIGHTWHITE_EX+'   🍿 Filmes em exibição 🍿' )
print('='*45)




console=Console()

table=Table(show_header=True, header_style='white')
table=Table(header_style='Red')
table.add_column('Data',style='white',width=12)
table.add_column('Titulo',style='white')                              # <===== Essas são as configurações da tabela!
table.add_column('Preço do ingresso',justify='right',style='white')
table.add_column('Preço do ingresso area Vip',justify='right',style='red')
table.add_row('Dezembro 20, 2024','Moana 2','R$ 45,00','R$ 65,00',style='cyan')
table.add_row('Janeiro 14, 2025' ,'Mario VS Wario','R$ 45,00','R$ 65,00',style='white')
table.add_row('Janeiro 23, 2025','Um completo desconhecido','R$ 45,00','R$ 65,00',style='magenta')
table.add_row('fevereiro 14, 2025','Num Beco sangrento','R$ 45,00','R$ 65,00',style='yellow')
console.print(table)


opção_de_ingresso=input(Fore.LIGHTGREEN_EX+'Digite o nome do filme que você deseja ver: ')

print(Fore.LIGHTCYAN_EX+'='*50)
opção_de_pagamento=input(Fore.LIGHTCYAN_EX+'''
                         (1) Pix
                         (2) Dinheiro
                         (3) Cartão de Credito
                            ===> ''')
if opção_de_pagamento not in ['1', '2', '3']:
    print(Fore.RED+'Opção não valida')
elif opção_de_pagamento == '1':
    print(Fore.LIGHTWHITE_EX+'Você pagou o seu ingresso com a forma de pagamento PIX!')
elif opção_de_pagamento == '2':
    print(Fore.LIGHTWHITE_EX+'Você pagou o seu ingresso com a forma de pagamento Dinheiro!')
elif opção_de_pagamento == '3':
    print(Fore.LIGHTWHITE_EX+'Você pagou o seu ingresso com a forma de pagamento Cartão de crédito!')

console=Console()
table=Table(show_header=True, header_style='red')
table.add_column('Feliz Natal ',style='red',width=12,)
console.print(table)