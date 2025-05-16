print('===== Formando Triângulo Pt2=====')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Os segmentos acima formam um triângulo equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Os segmentos acima formam um triângulo isósceles!')
    else:
        print('Os segmentos acima formam um triângulo escaleno!')
else:
    print('Os segmentos acima não podem formar um triângulo!') 