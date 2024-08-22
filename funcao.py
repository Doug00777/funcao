def bom_dia(nome_usuario: str):
    print(f'Bom dia, {nome_usuario}.')

def boa_tarde(nome_usuario: str):
    print(f'Boa tarde, {nome_usuario}.')

def boa_noite(nome_usuario: str):
    print(f'Boa noite, {nome_usuario}.')

nome_usuario = Tanjiro
horario = float(input('digite o horário do dia.'))

if horario > 0 or hora < 12:
    print(f'{bom_dia} {nome_usuario}.')
elif horario > 12 or < 18:
    print(f'{boa_tarde} {nome_usuario}.')
else:
    print(f'{boa_noite} {nome_usuario}.')



