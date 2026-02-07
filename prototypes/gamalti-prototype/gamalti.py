from  time import sleep 
from random import choice
print("_"*54)
print("Mini jogo de perguntas, escolha um ( ❤️  💭 ⚖️  🔥  🌍 ⏳ 🧠 🎭 🚀 🔒 📖 ) e responda a questão!")

opç=('❤️','💭','⚖️','🔥','🌍','⏳','🧠','🎭','🚀','🔒','📖')
Perguntas={'❤️':('O amor pode existir sem confiança?',
                 'O que diferencia paixão de amor verdadeiro?',
                 'É possível amar sem esperar nada em troca?'),
           
'💭':('Uma ideia só tem valor quando é aplicada?',
     'O que é mais importante: pensar rápido ou pensar profundo?',
     'Como distingues uma opinião de um argumento sólido?'),

'⚖️':('Justiça e igualdade são a mesma coisa?',
     'É melhor uma lei justa ou uma lei eficaz?',
     'O que pesa mais: intenção ou consequência?'),

'🔥':('A paixão pode ser perigosa? Explica.',
     'O que é mais difícil: acender ou manter uma chama?',
     'O entusiasmo sem disciplina leva a resultados?'),

'🌍':('O progresso humano sempre beneficia o planeta?',
     'O que é mais valioso: preservar ou explorar recursos?',
     'O mundo é feito mais de diferenças ou de semelhanças?'),

'⏳':('O tempo cura ou apenas ensina?',
     'É melhor viver o presente ou planejar o futuro?',
     'O que significa ‘perder tempo’ de verdade?'),
    
'🧠':('Inteligência e sabedoria são iguais e porquê?',
     'O raciocínio pode existir sem emoção? Porquê?',
     'O que é mais difícil: aprender ou desaprender? Porquê?'),

'🎭':('Fingir pode ser uma forma de sobrevivência?',
     'A autenticidade tem limites?',
     'O que revela mais: a máscara ou o rosto?'),

'🚀':('O avanço tecnológico sempre traz progresso humano?',
     'O que é mais importante: velocidade ou direção?',
     'Sonhar alto é suficiente para chegar longe?'),
           
'🔒':('Liberdade e segurança podem coexistir plenamente?',
     'O que prende mais: regras ou medos?',
     'É melhor proteger ou confiar?'),

'📖':('O que significa escrever a própria história?',
     'O que significa criar algo que ensina enquanto provoca reflexão?')
}

Respostas={'❤️':('Otimo esse teu raciocinio 🤝.\nTambem podemos olhar por outra perspectiva\n🌱, a confianca pode ser o alicerce\n🧱 que sustenta o sentimento ao longo do tempo ⏳.',
     'Boa colocacao ✨.\nE possivel ver assim tambem\n🔍, a paixao costuma ser intensa\n🔥 e imediata, enquanto o amor verdadeiro cresce com cuidado\n💞, tempo ⏳ e compromisso 🤝.',
     'Faz sentido o que dizes 😊.\nOutra leitura e que o amor pode ser livre de exigencias\n🎈, mas ainda assim valoriza troca 🤲,\nrespeito 🤍 e presenca 🌟.',),
           
'⚖️':('Boa reflexao 🤝. Justica busca equilibrio e igualdade busca tratar todos de forma semelhante, mas nem sempre sao a mesma coisa 🌱.',
     'Interessante esse ponto 😊. Uma lei justa toca a etica e uma lei eficaz resolve problemas, o ideal e aproximar as duas ⚖️.',
     'Faz sentido o que dizes 🌟. A intencao mostra o motivo e a consequencia mostra o impacto, as duas ajudam a avaliar melhor 🌊.',),

'🔥':('Teu raciocinio e valido 🔥. A paixao pode inspirar, mas tambem pode cegar se nao houver cuidado e equilibrio 🤝.',
     'Boa colocacao ✨. Acender uma chama e rapido, manter exige constancia, atencao e escolha diaria ⏳.',
     'Gostei da tua ideia 🌱. Entusiasmo move, disciplina sustenta, juntos eles geram resultados mais solidos 🧱.',),
    
'🌍':('Boa visao 🌍. O progresso pode trazer beneficios, mas precisa respeitar limites do planeta para ser duradouro 🌱.',
     'Interessante teu ponto 😊. Preservar garante futuro e explorar traz ganhos imediatos, o equilibrio costuma ser o caminho ⚖️.',
     'Faz sentido o que dizes 🤝. O mundo tem diferencas e semelhancas, e o valor esta em reconhecer e aprender com ambas 🌟.',),
    
'⏳':('Boa reflexao ⏳. O tempo pode curar algumas feridas e tambem ensinar a lidar melhor com elas 🌱.',
     'Interessante teu raciocinio 😊. Viver o presente e essencial, mas planejar ajuda a construir caminhos mais firmes 🧭.',
     'Gostei do que disseste 🔍. Perder tempo pode ser gastar energia sem direcao, e ganhar tempo e dar sentido ao que se faz 🌟.',),
    
'🧠':('Boa colocacao 🤝. Inteligencia lida com capacidade de pensar, sabedoria lida com usar isso com sentido e equilibrio 🌱.',
     'Faz sentido tua visao 😊. O raciocinio pode existir, mas a emocao influencia o rumo e a escolha do pensamento 💫.',
     'Interessante essa ideia 🌟. Aprender exige abertura e desaprender exige coragem para largar o que ja nao serve 🧱.',),
    
'🎭':('Boa reflexao 🎭. Fingir as vezes protege, mas quando vira habito pode esconder quem somos de verdade 🌱.',
     'Gostei do teu ponto 😊. Ser autentico e bonito, mas ainda precisamos de limites para conviver com respeito 🤝.',
     'Faz sentido o que dizes 🔍. A mascara mostra o que queremos proteger, o rosto mostra o que queremos revelar 🌟.',),
    
'🚀':( 'Boa colocacao 🚀. Tecnologia avanca, mas o progresso humano depende de valores, escolhas e uso consciente 🌱.',
     'Interessante teu raciocinio 😊. Velocidade sem direcao pode perder o rumo, direcao sem velocidade pode atrasar, o ideal e equilibrar 🧭.',
     'Faz sentido o que dizes 🌟. Sonhar alto inspira, mas caminho e consistencia fazem chegar mais longe 🧱.',),
   
'🔒':('Boa reflexao 🔒. Liberdade e seguranca podem coexistir quando ha respeito e limites claros para todos 🤝.',
     'Gostei da tua ideia 😊. Regras controlam por fora, medos prendem por dentro, entender os dois ajuda a se libertar 🌱.',
     'Faz sentido teu ponto 🌟. Proteger e importante, mas confiar cria ligacoes fortes quando ha responsabilidade 💫.',),
    
'📖':('Boa colocacao 📖. Escrever a propria historia e escolher caminhos, aprender com erros e seguir com intencao 🌱.',
     'Interessante tua visao 😊. Criar algo que ensina e provocar reflexao, e como deixar uma luz acesa para outros 💡.',),
    
'💭':('Boa ideia esse teu ponto 🤝. Podemos ver por outro angulo 🌱, uma ideia ganha mais vida quando se transforma em acao e impacto real ✨.',
     'Interessante essa visao 😊. Ha quem prefira velocidade ⚡ e ha quem prefira profundidade 🌊, as duas podem se completar dependendo do momento.',
     'Gostei do teu raciocinio 🔍. Uma opiniao nasce de percepcao pessoal, enquanto um argumento solido se apoia em razoes, exemplos e ligacao clara entre ideias 📘.',),
}

while True:
    escolha=str(input("Emoji?: ")).strip()
    while not escolha in opç:
        escolha=str(input('Emoji não encontrado, escolha de novo: ')).strip()
    print("🥰 Aguarde...")
    sleep(1)
    while escolha in opç:
        ap=choice(Perguntas[escolha])
        ar=Perguntas[escolha].index(ap)
        str(input(f"{ap}\nSeu raciocínio: ")) 
        print("🤞  🤞 um momento...")
        sleep(2)
        print(Respostas[escolha][ar])
        break
    con=str(input('Quer continuar? S/N: ')).upper()
    while con!='S'and con!='N':
        con=str(input('Erro na escolha! (S/N): ')).upper()
    if con=='N':
        break
print("_"*54)
print("✨ Fim do mini jogo! Obrigado por refletir comigo ✨") 
print("_"*54)
print("Criador: Aleleuia Nhaga Imbali\nContato: alti23@outlook.pt")
