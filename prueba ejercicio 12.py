

print('Programa para calcular el importe del alquiler de una bicicleta')

#Pedir datos

horas=int(input('Dame la duración en horas del alquiler (máximo 168 horas - 7 dias: '))

if horas==1:
    print('5 Euros')
else:
    if horas<=4:
        print('10 Euros')
    else:
        if horas<=24:
            print('15 Euros')
        else:
            if horas>=24 and horas<=72:
                importe_dia=12
                importe_72=horas*importe_dia
                print('{0} Euros'.format(importe_72))
            else:
                if horas>=72 and horas<=168:
                    importe_dia=8
                    importe_168=horas*importe_dia
                    print('{0} Euros'.format(importe_168))
