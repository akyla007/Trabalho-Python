import datetime
from Veiculos import veiculos
def cls(): #Limpar tela
    print('\n'*50)
def main():
    # ç = input() é somente para o sistema dar um pause para melhorar a visualização
    Dados = [] #Lista onde serão guardados os carros
    repet = 1   #repetidor de laço
    hj = datetime.date.today() #pega a data atual
    avanc = 0
    aux = 1 #auxiliador que guarda o tamanho da lista
    reservados = 0
    alugados = 0
    hj2 = 0
    Nomes = []
    Datas = []
    while(repet == 1):
        i = 0
        repetop = 1
        print("========"+str(hj)+"========") #A data mostra ano/mês/dia
        print("Quantidade de veiculos cadastrados -->"+"["+str(len(Dados))+']')
        for carro in Dados:
            if ((str(Dados[i].status) == 'alugado')):
                alugados = alugados + 1
            if ((str(Dados[i].status) == 'atraso')):
                reservados = reservados + 1
            i = i+1
        print("Quandidade de veículos alugados-->"+'['+str(alugados)+']')
        print('Quantidade de veículos atrasados-->'+'['+str(reservados)+']')
        print("Escolha dentre as opcoes:\n")
        print("1-Consultar veiculos")
        print("2-Adicionar veiculos")
        print("3-Alugar/reservar veiculos")
        print("4-Devolver/liberar veiculos")
        print("5-Excluir veiculos")
        print("6-Avancar data atual")
        print("7-Sair\n")
        a = int(input("Digite a opcao -->"))

        while(repetop == 1):
            if a==1:
                i=0
                print("Consulta de veiculos\n")
                for carro in Dados:
                    if ((str(Dados[i].status)) == 'liberado'):
                        print('Código:'+str(Dados[i].codigo)+'||Modelo:'+str(Dados[i].modelo)+str('||')+str(Dados[i].status))
                    if str(Dados[i].status) == 'alugado':
                        print('Código:' + str(Dados[i].codigo) + '||Modelo:' + str(Dados[i].modelo) + str('||') + str(Dados[i].status)+'||'+str(Dados[i].data)+'||'+str(Dados[i].nome)+'||')
                    if str(Dados[i].status) == 'atrasado':
                        print('Código:' + str(Dados[i].codigo) + '||Modelo:' + str(Dados[i].modelo) + str('||') + str(Dados[i].status) + '||' + str(Dados[i].data))
                    i=i+1
                print('Deseja ver mais informações sobre um carro?[1-sim/0-não]')
                r = int(input())
                if r == 1:
                    i=0
                    escolha = str(input('Digite o código:'))
                    for carro in Dados:
                        if str(escolha) != str(Dados[i].codigo):
                            i=i+1
                        else:
                            print('marca:\n'+Dados[i].marca)
                            print('valor:\n'+Dados[i].valor)
                            print('ano:\n'+Dados[i].ano)
                            ç = input()
                else:
                    repetop = 0
                repetop = 0
            if a==2:
                cod = '00' + str(aux) #Criação do codigo (001,002,003...) que será atribuido a cada carro registrado

                if aux >= 10:
                    cod = '0'+str(aux)

                if aux>=100 :
                    cod = aux
                print("Digite as informacoes do carro:\n")
                m = input('Digite a marca:')
                mo = input('Digite o modelo:')
                an = input('Digite o ano:')
                va = input('Digite o valor:')
                Datas.append(1)
                carro = veiculos(m,mo,an,va,'liberado',cod,hj2,0)
                aux = aux+1
                Dados.append(carro)
                repetop = 0

            if a==3:
                print("Alugar/reservar\n")
                i = 0
                for carro in Dados:
                    print('Código:' + str(Dados[i].codigo)+str('||')+'Status:'+str(Dados[i].status))
                    i = i + 1
                reservar = input('Qual carro deseja alugar:')
                i=0
                for carro in Dados:
                    if (str(Dados[int(i)].codigo) == str(reservar)) & (str(Dados[int(i)].status) == 'liberado'):
                        hj2 = datetime.date.today()#Data auxiliar que pega a data do dia em que o carro foi alugado
                        hj3 = datetime.date.today()
                        Dados[int(i)].nome = input("Digite seu nome")
                        dias=input(str('Daqui a quanto(s) dia(s) deseja alugar? [')+str(hj2)+str(']' + '\nSó permitido no máximo 30 dias\n'))
                        if int(dias) <=30:
                            hj2 = hj2 + datetime.timedelta(days=int(dias))
                            Datas[i]=hj2
                            Dados[int(i)].status = 'alugado'
                            Dados[int(i)].data = Datas[i]
                            print('Digite seu nome:\n')
                            #NÃO DIGITAR MAIS DE 30 DIAS!!
                else:
                    print('Esse carro já está alugado')
                repetop = 0

            if a==4: #Esta parte do programa(escolha 4) está incompleta!!
                print("Devolucao/liberacao\n")
                i=0
                print(str(hj2))
                for carro in Dados:
                    if str(Dados[i].status) == 'atraso':
                        print('O valor a pagar é'+str(int(Dados[i].valor)*2))
                        ç = input()
                ç=input()
                repetop = 0

            if a==5:
                i = 0
                print("Exclusao\n")
                print('Qual deseja excluir:\n')
                for carro in Dados:
                    print('Codigo:' + str(Dados[int(i)].codigo))
                    i=i+1
                i=0
                remover = str(input())
                for carro in Dados: #Analisa o codigo e o status[reservado/liberado...]
                    if (str(Dados[int(i)].codigo) == str(remover)) & (str(Dados[int(i)].status) == 'liberado') | (str(Dados[int(i)].status)=='atraso'):
                        print('Exclusão feita com sucesso')
                        Dados.remove(Dados[i]) #Quando um carro de ordem anterior é excluido, o carro de ordem posterior assume o posto do excluído
                    else:
                        print('Veículo Alugado/Atraso')
                        ç=input()
                    i=i+1
                repetop = 0

            if a==6:
                print("Avancar data,digite quantos dias pretende avancar:\n")
                avanc = int(input())
                hj = hj + datetime.timedelta(days=avanc)
                repetop = 0

            if a==7:
                print("Sair\n")
                repetop = 0
                repet = 0
                exit
            if a>7:
                print('Opção inválida!!')
                cls()
                repetop=0

main()
