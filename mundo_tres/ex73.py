times =('Palmeiras','Flamengo','Internacional','São Paulo','Grêmio',
        'Atlético-MG', 'Santos','Atlético-PR','Fluminense','Cruzeiro',
        'Bahia','Corinthians','Botafogo','Vasco','América-MG','Vitória','Ceará',
        'Chapecoense','Sport','Paraná')

print('Primeiros colocados:', times[0:3])
print('Ultimos colocados:', times[17:20])
print('Ordem alfabética:', sorted(times))
print(f'O Chapecoense está na : {times.index("Chapecoense")+1}ª posição')