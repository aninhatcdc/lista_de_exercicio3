lista_convidados=['neymar','virginia','anitta','bruna','marquezine']
for convite in lista_convidados:
 print('Estou lhe convidando para jantar',convite)
nome_removido='bruna'   
if nome_removido in lista_convidados:
 lista_convidados.remove(nome_removido)

print(f'A {nome_removido}','não pode comparecer')

lista_convidados2=['neymar','virginia','anitta','messi', 'cr7']
for convite2 in lista_convidados2:
 print('venha para aqui em casa comemorar,',convite2)