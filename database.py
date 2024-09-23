from ilustration import *

indice_menu = ['1','2','3','4']
s_n_respostas = ['s','n']

titulo = '''

          .▄▄▄  ▄• ▄▌▄▄▄ .    ▄▄▄ .     ▄▄▄·     • ▌ ▄ ·.  ▄▄▄·  ▄ .▄▪   ▐ ▄ ·▄▄▄▄  ▄▄▄   ▄▄▄·     ·▄▄▄▄• ▄▌.▄▄ · ▪         ▐ ▄ 
▪         ▐▀•▀█ █▪██▌▀▄.▀·    ▀▄.▀·    ▐█ ▀█     ·██ ▐███▪▐█ ▀█ ██▪▐███ •█▌▐███▪ ██ ▀▄ █·▐█ ▀█     ▐▄▄·█▪██▌▐█ ▀. ██ ▪     •█▌▐█
 ▄█▀▄     █▌·.█▌█▌▐█▌▐▀▀▪▄    ▐▀▀▪▄    ▄█▀▀█     ▐█ ▌▐▌▐█·▄█▀▀█ ██▀▐█▐█·▐█▐▐▌▐█· ▐█▌▐▀▀▄ ▄█▀▀█     ██▪ █▌▐█▌▄▀▀▀█▄▐█· ▄█▀▄ ▐█▐▐▌
▐█▌.▐▌    ▐█▪▄█·▐█▄█▌▐█▄▄▌    ▐█▄▄▌    ▐█ ▪▐▌    ██ ██▌▐█▌▐█ ▪▐▌██▌▐▀▐█▌██▐█▌██. ██ ▐█•█▌▐█ ▪▐▌    ██▌.▐█▄█▌▐█▄▪▐█▐█▌▐█▌.▐▌██▐█▌
 ▀█▄▀▪    ·▀▀█.  ▀▀▀  ▀▀▀      ▀▀▀      ▀  ▀     ▀▀  █▪▀▀▀ ▀  ▀ ▀▀▀ ·▀▀▀▀▀ █▪▀▀▀▀▀• .▀  ▀ ▀  ▀     ▀▀▀  ▀▀▀  ▀▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪

'''

introducao = (
    "O projeto Mahindra Fusion, desenvolvido para a Challenge de 2024 em parceria com a Tech Mahindra, "
    "visa popularizar a Fórmula E, a principal competição de corrida de carros elétricos do mundo, "
    "que enfrenta desafios de audiência, especialmente no Brasil."
)

problema = (
    "A Fórmula E, apesar de suas inovações e apelo sustentável, não consegue consolidar uma base de fãs robusta, "
    "evidenciada pela baixa participação do público em eventos como o ePrix em São Paulo. Fatores como a falta de "
    "reconhecimento da categoria e tecnologias de divulgação atrativas contribuem para a discrepância de audiência "
    "em comparação com a Fórmula 1."
)

solucao = (
    "O Mahindra Fusion propõe a criação de um site que centralize as transmissões da Fórmula E, oferecendo uma "
    "experiência interativa e gamificada, incluindo:\n"
    "- Gamificação: Acumulação de pontos e recompensas por participação.\n"
    "- Apostas Virtuais: Incentivo à interação dos fãs através de apostas fictícias.\n"
    "- Bate-papo em Tempo Real: Criação de uma comunidade ativa durante as transmissões.\n"
    "- Transmissão ao Vivo: Recursos avançados como câmeras on-board, múltiplos ângulos de filmagem e "
    "estatísticas em tempo real.\n"
    "- Conteúdo Exclusivo: Perfis de pilotos, documentários e análises técnicas."
)

objetivos = (
    "Objetivos Esperados:\n"
    "- Aumentar a visibilidade da Fórmula E.\n"
    "- Engajar telespectadores com uma experiência interativa.\n"
    "- Crescer a audiência em pelo menos 30%."
)

justificativa = (
    "A proposta busca transformar a percepção do público em relação à Fórmula E, criando uma plataforma mais "
    "acessível e envolvente, o que deverá resultar em um aumento significativo da audiência."
)

conclusao = (
    "Com o crescimento do mercado de streaming, o Mahindra Fusion apresenta uma oportunidade de expandir a "
    "presença da Fórmula E, fortalecer sua base de fãs e promover um engajamento sustentável e contínuo."
)

produtos = {
    'NFT1': {
        'id': '1',
        'qtd': '12',
        'equipe': 'DS Techeetah',
        'veiculo': 'DS E-Tense FE21',
        'piloto': 'Jean-Éric Vergne',
        'velocidade': '280 km/h (DS E-Tense FE21)',
        'corrida': 'E-Prix de Mônaco 2019 (Vergne venceu a corrida)',
        'pista': 'Circuito de Mônaco',
        'volta': '52.385 segundos',
        'codigo': '8*&7$2ñÇæþð¿½¶Û!#=9&5 +|}1|4&5( ;:8ñÇæþð¿½¶Û$1~<*9>#| _+9$ñÇæþð¿½¶Û=~4^&5}3:| }~ñÇæþð¿½¶Û[|@#]_$|*ñÇæþð¿½¶Û*_1%$;{!#=9&5 +|}1|&^7|>^#+9_= 8;&$3*!%[9#ñÇæþð¿½¶Û(*^&9|[$$4~7<+*5/@^+3|*9%;7_*!*6+ -:_9+^7;_$[*~@&4 $;&^!#~*9(ñÇæþð¿½¶Û]*9&+6%7|$:3!^#*<%8;_+6^|)$9*&3*[ #5*&_9$!^;7<$~1> 3;$&%ñÇæþð¿½¶Û_%#8&;]7<+$_!9*4)$^5!ñÇæþð¿½¶Û&;3#_~[ 9&$_!^7<+*µñÇ{ *@^6%$3;_!~7&#+9 >~$&;_1^9*!#%4@+aBcD1#@mNoP^&sTuV;:3_!A*cD{F&kG<%=qR2>iJ#h&$yL+W4%}vZ(5*Xz0-_7@ñÇæþð¿½¶ÛiH=%}jQ|>Y6*>uRk@b*Mp$3|8D|w&^@yR&$O|:P|8B}|5d(!*~2C|/vH6|rW*9=</J$*h&5!F@|;6v!y@Q*{>2|3#C}B/4*W1%_k&>z|^u*Rj=;F|y}9>X+;z5:|$6iF~d&;k}|@bR9&*w=|x^!1!@c$|%T>2J6&^4@{oQ|!7)D}z8%|}^5S{3p#z4|!<D3&}X|$5B1k%=u{ñÇæþð¿½¶Ûz6@*}A!4R*Q9j+3y$C_&*x4=!5^z7*{*<Q}|;aC#~F@3_+5%1|V6^*sA}!w|R2}kY<~4#j5X|@=z+S_7&9^M|o>Rj{3!µñÇæþð¿½¶Û¼º»ab#d',
        'preco': {'final': '$5500', 'base': '$100'},
        'desenho': colored_art1
    },
    'NFT2': {
        'id': '2',
        'qtd': '7',
        'equipe': 'Audi Sport ABT Schaeffler',
        'veiculo': 'Audi e-tron FE07',
        'piloto': 'Lucas di Grassi',
        'velocidade': '280 km/h (Audi e-tron FE07)',
        'corrida': 'E-Prix de Berlim 2017 (Di Grassi venceu a corrida e garantiu o campeonato)',
        'pista': 'Tempelhof Airport Street Circuit (Berlim)',
        'volta': '1:08.202 minutos',
        'codigo': 'iefm#%h9812E##$ASFJIS$%D234KFSO*@#634&$@!#ty!h&!*hfygyfgiwueh&y#!g*G6QGDQTAWD9&5+|}1|&^7|>^#+9_=8;&$3*!%[9#|~):(*^&9|[$$4~7<+*5/@^+3|*9%;7_*!*6+-:_9+^7;_$[*~@&4$;&^!#~*9(4>#*7]*9&+6%7|$:3!^#*<%8;_+6^|)$9*&3*[#5*&_9$!^;7<$~1>3;$&%_7^9|$2*!@_%#8&;]7<+$_!9*4)$^5!>6%|7&;3#_~[9&$_!^7<+*$;3~_{*@^6%$3;_!~7&#+9>~$&;_1^9*!#%4@+]aBcD1#@mNoP^&sTuV;:3_!A*cD{F&kG<%=qR2>iJ#h&$yL+W4%}vZ(5*Xz0-_7@!$1^<iH=%}jQ|>Y6*>uRk@b*Mp$3|8D|w&^@yR&$O|:P|8B}|5d(!*~2C|/vH6|rW*9=</J$*h&5!F@|;6v!y@Q*{>2|3#C}B/4*W1%_k&>z|^u*Rj=;F|y}9>X+;z5:|$6iF~d&;k}|@bR9&*w=|x^!1!@c$|%T>2J6&^4@{oQ|!7)D}z8%|}^5S{3p#z4|!<D3&}X|$5B1k%=u{;c^>|z6@*}A!4R*Q9j+3y$C_&*x4=!5^z7*{*<Q}|;aC#~F@3_+5%1|V6^*sA}!w|R2}kY<~4#j5X|@=z+S_7&9^M|o>Rj{3!',
        'desenho': colored_art2
    },
    'NFT3': {
        'id': '3',
        'qtd': '9',
        'equipe': 'Jaguar TCS Racing',
        'veiculo': 'Jaguar I-Type 5',
        'piloto': 'Mitch Evans',
        'velocidade': '280 km/h (Jaguar I-Type 5)',
        'corrida': 'E-Prix de Cidade do México 2022 (Evans venceu a corrida)',
        'pista': 'Autódromo Hermanos Rodríguez (Cidade do México)',
        'volta': '1:08.200 minutos',
        'codigo': '3hÉ@C9&3T¿ës¿û|Tð¿ºç8ð{f^Cv5}+¹Ç|qE4$5( l:87´ñ¿ÇwL$1~ÛcLx)9<#E|Õ+9$xï¿Çç¿ý=¡4j^&5*3:ç}5ñ¿|}Xë_#ñ¿ö¿;{!#sU9&E|5 +|}1|5&^7|>^#+9_= 8ë&$3*!%[9#ñÇæþð¿½¶$(*^&9|[$$4ç7<+*5/@^+3|*9%;7_*!*6+-:_9+^7;_$[*~@&4 $;&^!#~*9(?#ñÇæþð¿½¶(]*9&+6%7|$:3!^#*<%8;_+6^|)$9*&3*[ #5*&_9$!^;7<$~1> 3;$&%ñÇæþð¿½¶_%#8&;]7<+$_!9*4)$^5!ñÇæþð¿½¶U&;3#_~[ 9&$_!^7<+*µñÇ{ *@^6%$3;_!~7&#+9 >~$&;_1^9*!#%4@+aBcD1#@mNoP^&sTuV;:3_!A*cD{F&kG<%=qR2>iJ#h&$yL+W4%}vZ(5*Xz0-_7@ñÇæþð¿½¶ÛiH=%}jQ|>Y6*>uRk@b*Mp$3|8D|w&^@yR&$O|:P|8B}|5d(!*~2C|/vH6|rW*9=</J$*h&5!F@|;6v!y@Q*{>2|3#C}B/4*W1%_k&>z|^u*Rj=;F|y}9>X+;z5:|$6iF~d&;k}|@bR9&*w=|x^!1!@c$|%T>2J6&^4@{oQ|!7)D}z8%|}^5S{3p#z4|!<D3&}X|$5B1k%=u{ñÇæþð¿½¶Ûz6@*}A!4R*Q9j+3y$C_&*x4=!5^z7*{*<Q}|;aC#~F@3_+5%1|V6^*sA}!w|R2}kY<~4#j5X|@=z+S_7&9^M|o>Rj{3!',
        'preco': {'final': '$4600', 'base': '$100'},
        'desenho': colored_art3
    }
}