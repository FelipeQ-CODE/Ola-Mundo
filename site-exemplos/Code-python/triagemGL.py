#Cadastro em Triagem para Aferição de GLICEMIA CAPILAR
while (1):
    print(53*('-'))
    print('CADASTRO EM TRIAGEM PARA AFERIÇÃO DE GICEMIA CAPILAR ')
    print(53*('-'))
    print()

    dados = dict()
    dados ['nome']=input('Nome: ')
    dados ['sobrenome']= input('Sobrenome: ')
    dados ['idade'] = int(input('Idade: '))

    #PACIENTES DIABETICOS , EM USO DE INSULINA HUMANA REGULAR , SEGUE OS CONTROLES DAS APLICAÇOES CONFORME O DEXTRO.

    gl=int(input('Digite seu Dxt: '))
    print()
    if gl >= 80 and gl <= 180 :
        print('Voce nao ira ser suplementado')
    if gl > 181 and gl <= 229 :
        print('Voce sera suplementado com 2UI de Insulina Regular ')
    if gl > 230 and gl <= 250 :
         print('Voce sera suplementado com 4UI de Insulina Regular ')
    if gl > 251 and gl <= 270 :
        print('Voce sera suplementado com 6UI de Insulina Regular ')
    if gl > 271 and gl <= 290 :
        print('Voce sera suplementado com 8UI de Insulina Regular ')
    if gl > 291 and gl < 300:
        print('Voce sera suplementado com 10UI de Insulina Regular e comunicar o Medico plantonista ')
    if gl >= 301 :
        print('Suplementar com 10ui e Comunicar o médico, com urgência!!')

        print(' ')

    print(f'{dados} Voce foi suplementado conforme Prescrição medica da UNIDADE !')
    print(' ')
    stop = int(input('Deseja parar a TRIAGEM ? digite  (1 -Sim ou  2-Não):'))
    if stop == 1:
        break
        