

print('Puta mierda')

#Pedir datos

h=int(input('Dame la duración en h del alquiler (máximo 168 h - 7 dias: '))

if h==1:
    print('5 sentimo')
else:
    if h<=4:
        print('10 peseta')
    else:
        if h<=24:
            print('15 peniques')
        else:
            if h>=24 and h<=72:
                importe_dia=12
                importe_72=h*importe_dia
                print('{0} centavos'.format(importe_72))
            else:
                if h>=72 and h<=168:
                    importe_dia=8
                    importe_168=h*importe_dia
                    print('{0} cabra'.format(importe_168))
