
import func

print('Vamos calcular o seu imc?')

valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite o seu sexo (M ou F): ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo inválido. Digite M ou F.')
    else:
        valid_sexo = True
        print('\n')

valid_peso = False
while valid_peso == False:
    peso = input('Digite o peso (ex. 68.5): ')
    try:
        peso = float(peso)
        if peso <= 0 or peso > 350:
            print('Peso inválido. Número não pode ser zero ou negativo e deve ser inferior a 350.')
        else:
            valid_peso = True
            print('\n')
    except:
        print('Peso inválido. Use apenas números e separe os decimais com ponto.')

valid_altura = False
while valid_altura == False:
    altura = input('Digite a altura em metros (ex. 1.70): ')
    try:
        altura = float(altura)
        if altura <= 0 or altura > 3:
            print('Altura inválida. Número não pode ser zero ou negativo e deve ser inferior a 3 metros.')
        else:
            valid_altura = True
            print('\n')
    except:
        print('Altura inválida. Use apenas números e separe os decimais com ponto.')


v_imc = str(func.imc(peso,altura))
c_imc = func.class_imc(sexo,peso,altura)

print('O seu IMC é:',v_imc[0:5])
print('A sua classificação é:',c_imc)
