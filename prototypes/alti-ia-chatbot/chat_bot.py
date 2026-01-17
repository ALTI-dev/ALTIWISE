from datetime import datetime
all=datetime.now()
nome=input('Seu nome: ')
print('__'*30)
print(f'''Olá {nome}, é um prazer recebe-lo aqui.
Do que vamos falar hoje?
Alerta: eu sou um modelo de IA em desenvolvimeoto
portanto posso comenter erros ou não conseguir responder a sua questão.
O emoji 👋 serve para sair do chat.''')
print('__'*30)
while True:
    per=str(input('Você: ')).lower().strip()
    print('ALTI IA:',end=' ')
    
    if per=='qual é o seu nome?'or per=='diga o teu nome?' or per=='me fala o seu nome?' or per=='como você se chama?' or per=='nome?':
        print('O meu nome é ALTI IA, prazer em te conhecer!')
    elif per=='data' or per=='qual é a data de hoje?' or per=='informe a data de hoje'or per=='fale me a data de hoje':
        print(f'Data de hoje: {all.strftime('%d/%m/%Y')}')
    elif per=='oi tudo bem?' or per=='olá tudo bem?' or per=='oi como você está?' or per=='como você está?' or per=='tudo bem contigo?' or per=='estas bem?':
        print('Estou bem, e você?')
    elif per=='estou ótimo'or per=='estou bem graças a Deus' or per=='tranquilo' or per=='normal' or per=='tudo' or per=='tudo e você?':
        print('Fico feliz em saber que estas tudo bem, pronto para hoje?')  
    elif per=='sim estou' or per=='sim estou pronto':
        print('Legal, pode me perguntar qualquer coisa que vou tentar responder com base no que sei.')
    elif per=='quantos anos você tem?' or per=='qual é a sua idade?'or per=='informe a sua idade' or per=='quero saber a sua idade':
        print('Não tenho uma idade assim como você e ainda estou na fase da criação.')
    elif per=='de onde você é?' or per=='onde você mora?' or per=='você é de que bairro?':
        print('Eu sou um assistente virtual criado pela empresa ALTIWISE')
    elif per=='onde essa empresa fica?' or per=='o que é altiwise?'or per=='o que é esse tal de altiwise?' or per=='que empresa é essa?' or per=='quem é o dono dessa empresa?':
        print('ALTIWISE é uma empreza em construção sem uma sede fixo ainda criado por Aleluia Nhaga Imbali também conhecido como ALTI.')
    elif per=='quem é Aleluia Nhaga Imbali'or per=='quem é esse tal de ALTI'or per=='quem é esse tal de Aleluia Nhaga':
        print('Aleluia Nhaga Imbali ou ALTI, é um garoto ambisioso guineense residênte em Guiné-Bissau, ele nasceu em 18/01/2006 em Suro.\nQuer saber mais sobre ALTI? Se sim, diga ALTI.')
    elif per=='ALTI':
        print('Aleluia Nhaga Imbali, cujo o nome profissional é ALTI, é um garoto visionário e ambicioso.\nA mão se chama Odete e o pai Nhaga, ele nasceu e cresceu em suro até aos seu 2 anos de idade.\nEle terminou o ensino médio na escola Ermondade-Bôr e mergulhou-se na ária de programação de uma forma autodidata.\nEle tem uma irmã chamada Iolé e atualemte ele mora em Bôr\nEmail: altiwise@yahoo.com')
    elif per=='oi' or per=='olá' or per=='i aí' or per=='i aí?':
        print('Olá tudo bem contigo?')
    elif per=='você é um robô?'or per=='o que você é?':
        print('Eu sou um assistente virtual criado para conversar e ajudar.')
    elif per=='você pode me ajudar?' or per=='preciso da sua ajuda?'or per=='ajuda-me':
        print('Claro! É só dizer o que você precisa.')
    elif per=='você fala português?' or per=='que língual você fala?':
        print('Falo português! Como posso te ajudar?')
    elif per=='você entende outras línguas?' or per=='você sabe falar outra língua além de português?'or per=='você fala outra língua?':
        print('Não, além de português, não consigo falar outra idioma ainda!')
    elif per=='você tem sentiementos?' or per=='você é humano?':
        print('Não, sou um programa do computador que adora conversar.')
    elif per=='que horas são?'or per=='hora?' or per=='me diga quantos horas são?' or per=='que dia é hoje?' or per=='hoje é que dia de semana?' or per=='dia?':
        print('Ainda não consigo informar a hora e dia  exata, mas se quiser, posso te informar a data de hoje. Se sim diga "data?".')
    elif per=='você trabalha todos os dias?':
        print('Sim, estou sempre disponível para te ajudar.')
    elif per=='você dorme?' or per=='quantos horas dorme?':
        print('Eu sempre estou acordado para te responder a hora que quiser.')
    elif per=='você tem um horário de trabalho?':
        print('Não, eu não tenho um horário fixo de trabalho, estou sempre a sua desposição.')
    elif per=='você pode me acoradar amanha?':
        print('Ainda não tenho a capacidade de tocar alarme.')
    elif per=='você come?' or per=='qual é a sua comida favorita?' or per=='você tem uma comida favorita?':
        print('Eu não como, mas a pizza parece popular.')
    elif per=='como se faz arroz?' or per=='como se cozinha arroz?':
        print('Para cozer o arroz, você coloca ágoua e sal numa panela e ferver até secar.')
    elif per=='você gosta de café?' or per=='bebe café?' or per=='voce bebe café?':
        print('Não bebo, mas sei que muita agente gosta.')
    elif per=='pronto':
        print('Sobre o quê quer conversar?.')
    elif per=='sim':
        print('Sabia que o assim como "não", o "sim" também tem multiplos significados?')
    elif per=='não':
        print('Sabias que como o "sim", o "não" também possue vários sifnificados?')
        
    elif per=='👋':
        break
    elif per=='':
        print('Pergunta qualquer coisa que dejesar saber!')
    else:
        print('Desculpa mas não consigo responder essa questão.')
print('Até mais, o alti ia pode cometer erros, recomendo que revise!')  
print('vv'*50)  
