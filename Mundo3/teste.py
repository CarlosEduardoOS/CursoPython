tempo = int(input())
hora = minuto = segundo = 0
while tempo > 0:
    if tempo >= 3600:
        tempo = tempo - 3600
        hora += 1
    if tempo < 3600 and tempo >= 60:
        tempo = tempo - 60
        minuto += 1
    if tempo < 60 and tempo >= 1:
        tempo = tempo - 1
        segundo += 1
print(f'{hora}:{minuto}:{segundo}') 