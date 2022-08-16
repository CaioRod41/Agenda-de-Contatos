# Atividade avaliativa - Lógica - Algorítimos e Programação de computadores 
# Aluno: Caio Rodrigues Lino Mesquita
# Matrícula: 2272190016

AgendaTelefonica = [] #Declaração do arranjo Agenda Telefonica (para armazenar os contatos)


def digite_nome():  #Fução para inserir o nome do contato
    return(input("Digite o nome: "))

def digite_telefone():   #Fução para inserir o telefone do contato
    return(input("Digite o telefone: "))
 
def digite_twitter():    #Fução para inserir o twitter do contato
    return(input("Digite o twitter: "))

def digite_instagram():    #Fução para inserir o instagram do contato
    return(input("Digite o instagram: "))

def digite_facebook():       #Fução para inserir o facebook do contato
    return(input("Digite o facebook: "))

def digite_email():       #Fução para inserir o e-mail do contato
    return(input("Digite o e-mail: "))


def saida_dados(nome, telefone, twitter, instagram, facebook,email):    #Fução de saída de dados (impressão dos dados do contato)
    print("\n Nome: %s \n Telefone: %s \n Twitter: %s \n Instagram: %s \n Facebook: %s \n E-mail: %s \n" % (nome, telefone, twitter, instagram, facebook, email))
    
def Criar_Contato():   #Função para criação de um novo contato
    global AgendaTelefonica   #chamando a variável AgendaTelefonica 
    
    nome = digite_nome()  #Armazenando o nome do contato 
    telefone = digite_telefone()  #Armazenando o telefone do contato 
    twitter = digite_twitter()  #Armazenando o twitter do contato 
    instagram = digite_instagram()  #Armazenando o instagram do contato 
    facebook = digite_facebook()    #Armazenando o facebook do contato 
    email = digite_email()
    AgendaTelefonica.append([nome, telefone, twitter, instagram, facebook, email]) #Insere no vetor AgendaTelefonica todos os dados armazenados nas variáveis
    
def Imprimir_Agenda(): #Função para impressão da agenda
    cont = 0 #inciando um contador auxiliar para dizer quantos contatos tem na agenda
    print("\n\n------------------Agenda-------------------") #formatação da agenda
        
    for impressão in AgendaTelefonica: #loop for para impressão de todos os contatos da AgendaTelefonica
        cont +=1 #toda vez que o loop se repete o contador soma +1
        print("Contato: %s" % (cont)) #numero do contato dentro da agenda
        saida_dados(impressão[0], impressão[1], impressão[2], impressão[3], impressão[4], impressão[5]) #saida de dados tem como parametro a impressão de todas as informações
    print("\n----------------------------------------") #formatação da agenda

def Pesquisar_contato(nome): #Função para pesquisar o contato (tem como paramêtro o nome pois a pesquisa é feita pelo nome)
    nome_auxiliar = nome.lower() #criação da variavel nome auxiliar (.lower ajuda a transferir a string)
    for aux, achou in enumerate(AgendaTelefonica): #loop for com índice enumerate (retornando primeiramento o índice)
        if achou[0].lower() == nome_auxiliar: #condicional para retornar caso a condição seja atendida
            return aux
    return None
    
def Consultar_Contato(): #Função para consultar o contato através do nome 
    
    consult_aux = Pesquisar_contato(digite_nome()) #usuário insere o nome na variável, ele vai para a função de pesquisar e o resultado para a variável auxiliar
    if consult_aux != None: #Se a variável auxiliar atender a condição o if vai prosseguir
        nome = AgendaTelefonica[consult_aux][0] #Pesquisa dentro da agenda telefonica o nome do contato
        telefone = AgendaTelefonica[consult_aux][1] #Pesquisa dentro da agenda telefonica o telefone do contato
        twitter = AgendaTelefonica[consult_aux][2] #Pesquisa dentro da agenda telefonica o twitter do contato
        instagram = AgendaTelefonica[consult_aux][3] #Pesquisa dentro da agenda telefonica o instagram do contato
        facebook = AgendaTelefonica[consult_aux][4] #Pesquisa dentro da agenda telefonica o facebook do contato
        email = AgendaTelefonica[consult_aux][4] #Pesquisa dentro da agenda telefonica o e-mail do contato
        print("Nome encontrado!") #caso as informações coincidirem, irá aparecer na tela que o nome foi encontrado
        saida_dados(nome, telefone, twitter, instagram, facebook, email) #imprime na tela as informações do contato         
    else:
        print("Contato não encontrado!") #imprime na tela caso o contato não seja encontrado
            
def Alterar_Contato(): #Função de altera o contato
    
    consult_aux = Pesquisar_contato(digite_nome()) #usuário insere o nome na variável, ele vai para a função de pesquisar e o resultado para a variável auxiliar
    if consult_aux != None: #Se a variável auxiliar atender a condição o if vai prosseguir
        nome = AgendaTelefonica[consult_aux][0] #Pesquisa dentro da agenda telefonica o nome do contato
        telefone = AgendaTelefonica[consult_aux][1] #Pesquisa dentro da agenda telefonica o telefone do contato
        twitter = AgendaTelefonica[consult_aux][2] #Pesquisa dentro da agenda telefonica o twitter do contato
        instagram = AgendaTelefonica[consult_aux][3] #Pesquisa dentro da agenda telefonica o instagram do contato
        facebook = AgendaTelefonica[consult_aux][4] #Pesquisa dentro da agenda telefonica o facebook do contato
        email = AgendaTelefonica[consult_aux][4] #Pesquisa dentro da agenda telefonica o e-mail do contato
        print("Nome encontrado!") #caso as informações coincidirem, irá aparecer na tela que o nome foi encontrado
        saida_dados(nome, telefone, twitter, instagram, facebook, email) #imprime na tela as informações do contato         
        nome = digite_nome() #após isso os usuários digitam as novas informações do contato (primeiramente o nome)
        telefone = digite_telefone() #digitando o telefone e inserindo na variável
        twitter = digite_twitter() #digitando o twitter e inserindo na variável
        instagram = digite_instagram() #digitando o instagram e inserindo na variável
        facebook = digite_facebook() #digitando o facebook e inserindo na variável
        email = digite_email() #digitando o e-mail e inserindo na variável
        AgendaTelefonica[consult_aux] = [nome, telefone, twitter, instagram, facebook, email] #insere as novas informações dentro do contato auxiliar, substituindo-os)
    else:
        print("Contato não encontrado!") #imprime na tela caso o contato não seja encontrado
    
def Remover_Contato(): #Função para remover um contato
    global AgendaTelefonica   #chamando a variável AgendaTelefonica 
    nome = digite_nome() #Armazenando o nome do contato 
    aux = Pesquisar_contato(nome) #Pesquisando o contato dentro da agenda (pelo nome) e inserindo-o na variável auxiliar
    if aux != None: #condicional para procurar a palavra dentro da agenda
        del AgendaTelefonica[aux] #caso ache, o contato é deletado
    else:
        print("Nome não encontrado!") #Caso não ache, imprime na tela "Nome não encontrado!" e volta para o menu


 
while True: #começando os laços para fazer o menu e as condicionais do menu
    
        print("""
          
          1 - Criar contato:
          2 - Consultar cadastro:
          3 - Imprimir Relatório completo:
          4 - Alterar contato:
          5 - Remover contato:
          6 - Sair:
          
          """)
        
        opção = int(input("\nDigite sua opção: ")) #armazenamento da opção
       
        if opção == 1: #Se o usuário digita 1, chama a função de adicionar um contato
            quantidade = int(input("Digite a quantidade de contatos que deseja adicionar: "))   
        
            for quantidades in range(quantidade):
                Criar_Contato()
            
            
        elif opção == 2: #Se o usuário digita 2, chama a função de consultar um contato
                Consultar_Contato()
            
        elif opção == 3: #Se o usuário digita 3, chama a função de imprimir o relatório da agenda
                Imprimir_Agenda()
            
        elif opção == 4: #Se o usuário digita 4, chama a função de alterar um contato
                Alterar_Contato()
            
        elif opção == 5: #Se o usuário digita 5, chama a função de remover um contato
                Remover_Contato()
            
        elif opção == 6: #Se o usuário digita 6, encerra o programa
            print("Encerrando programa!")
            print("..........................................\n\n")
            break
        
        else:
            print("Valor incorreto! Digite uma opção aceitável!") #Se o usuário digita um valor fora do menu, imprime na tela a frase e retorna pro menu
            
            

            
        
        