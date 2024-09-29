# MAHINDRA FUSION (Python)

## Integrantes:
- Caio Felipe de Lima Bezerra          RM: 556197
- Gabriel Terra Lilla dos Santos       RM: 554575
- Lucas Derenze Simidu                 RM: 555931
- Marcos Vinícius da Silva Costa       RM: 555490
- Ricardo Cerazi Di Tilia              RM: 555155

<br><br>

## 1. Descrição do Projeto

O sistema é uma plataforma de apostas voltada para corridas de Fórmula E, permitindo que os usuários criem contas, explorem informações sobre NFTs (Tokens Não Fungíveis) relacionados às corridas e façam apostas em eventos.

Os usuários podem visualizar detalhes de diferentes NFTs, acessar informações sobre as corridas e apostar em seus corredores favoritos.

O sistema também inclui funcionalidades de validação, como verificação de idade e confirmação de dados pessoais, além de mostrar resultados de apostas realizadas.

<br><br>

## 2. Objetivo do Projeto

O objetivo do sistema é proporcionar uma experiência interativa e envolvente para os usuários que desejam participar de apostas em corridas de Fórmula E, ao mesmo tempo em que exploram NFTs associados, assim contribuindo para a propagação de sua imagem, fazendo um sistema totalmente interativo e atrativo para o público consumidor;

Ele busca:

- **Facilitar a Criação de Contas:** Permitir que novos usuários criem contas facilmente, garantindo a segurança e a integridade de seus dados;

- **Oferecer Informações Abrangentes:** Fornecer detalhes sobre os NFTs e as corridas, ajudando os usuários a tomar decisões informadas ao realizar apostas;

- **Permitir Apostas Seguras e Divertidas:** Garantir que as apostas sejam feitas de maneira fácil, com um sistema que calcula odds e exibe resultados de forma clara;

- **Promover um Ambiente de Apostas Responsáveis:** Validar a idade dos usuários e fornecer feedback sobre suas apostas, incentivando uma participação consciente e responsável nas corridas;

- **Interação Visual e Informativa:** Utilizar elementos gráficos e interativos para melhorar a experiência do usuário e facilitar a navegação pelo sistema;

<br><br>

## 3. Instalação de pré-requisitos

Para usufruir do sistema com êxito, é necessário possuir conhecimento da versão do Python que foi utilizada para o desenvolvimento, nesse caso, sendo o “Python 3.12.2”;

Também é necessário a instalação de certas bibliotecas para o funcionamento magistral do sistema, sendo eles:

- **Pandas, comando:** `pip install pandas`
- **Tabulate, comando:** `pip install tabulate`

<br><br>

## 4. Organização de Arquivos

A organização dos arquivos no repositório do sistema Mahindra Fusion, desenvolvido em Python, segue a seguinte estrutura:



<br>

### MAHINDRA_FUSION_PYTHON/ 
### ├── bet.py 
### ├── database.py 
### ├── function.py 
### ├── ilustration.py 
### ├── LICENSE 
### ├── main.py 
### └── README.md



### 4.1. main.py

O arquivo `main.py` implementa o sistema principal da aplicação, utilizando de menu principal para a área de compras de NFTs (tokens não fungíveis) ligados a corridas e onde importa as funcionalidades de apostas em corridas fictícias da `bet.py`, também permitindo a criação e gerenciamento de contas de usuário.

**Menu Principal:** O usuário pode acessar a conta, saber mais sobre o sistema, entrar no mercado de NFTs ou acessar um sistema de apostas.

**Opções:**

- **Sua conta:** Ver ou criar uma conta de usuário, onde são armazenados dados como nome, idade, CPF, email e telefone;
- **Sobre Nós:** Apresenta um resumo sobre o serviço;
- **BET:** Permite ao usuário acessar um sistema de apostas, mas só é acessível para maiores de idade;
- **Mercado Virtual (Fusion Market):** Oferece NFTs relacionados a corridas, com detalhes sobre cada NFT e a possibilidade de visualizar informações adicionais e gráficos;

**Criação e Verificação de Conta:** O sistema solicita e valida os dados do usuário para criar uma conta, como nome, idade, CPF e email;

- Se a conta já existir, os dados são exibidos;
- Se o usuário for menor de idade, ele é redirecionado ao menu;

**Mercado de NFTs:** O usuário pode visualizar uma lista de NFTs disponíveis para compra ou visualização. Detalhes de cada NFT são mostrados, incluindo informações sobre o piloto, veículo, velocidade e corrida, além de permitir visualizações gráficas.

### 4.2. bet.py

Este arquivo `bet.py` implementa um sistema de apostas fictícias para 5 corridas de Fórmula E com suas credenciais geradas aleatoriamente a cada execução, utilizando uma interface simples e eficaz de comando onde o usuário pode escolher entre essas corridas, realizar suas apostas a partir da escolha de um corredor e um valor, então visualizar seus resultados. O sistema se destaca pelo cálculo das probabilidades (odds), a randomização dos resultados e a simulação de corridas com diferentes competidores.

**Importações e Dependências:** O arquivo utiliza bibliotecas como:

- `random` para randomizar a posição dos corredores.
- `pandas` para organizar e exibir as corridas em forma de tabela.
- `tabulate` para melhorar a apresentação das tabelas no terminal.

Outras funções e dados são importados de arquivos externos (`database`, `function`, `ilustration`), fornecem funcionalidades adicionais, como ilustrações e dados sobre os competidores e corridas.

**Apostas:** As apostas são armazenadas nos dicionários `apostas` (para acompanhar as apostas atuais) e `apostas_realizadas` (para registrar as corridas em que o usuário já apostou, evitando duplicidade).

**O processo de apostar envolve:**
- Exibir uma lista dos competidores da corrida, junto com suas posições e odds (probabilidades de ganho);
- Solicitar ao usuário que escolha um corredor (com base em sua posição) e o valor da aposta;
- Registrar essa aposta, incluindo o corredor escolhido, o valor e as odds calculadas;

**Cálculo das Odds:** A função `calcular_odds` ajusta as odds (probabilidades de ganho) com base na posição do corredor. Corredores com melhores posições têm odds mais baixos, enquanto aqueles com posições inferiores possuem odds maiores, refletindo um risco maior e, portanto, uma recompensa potencial maior.

A fórmula usada para as odds é `round(10.0 - (posicao - 1) * (8.5 / 19), 2)`, que diminui as odds gradualmente com base na posição do corredor.

**Simulação da Corrida:** A função `exibir_corrida` embaralha a lista de corredores para simular a corrida, gerando uma tabela com os competidores, suas posições e odds.
- Se o usuário já apostou naquela corrida, ele é notificado que não pode apostar novamente;
- Caso contrário, o usuário é solicitado a fazer uma aposta, escolhendo a posição do corredor e o valor em dinheiro;

**Exibição dos Resultados:** A função `mostrar_resultados` simula o resultado final de cada corrida de forma aleatória (usando `random.randint` para determinar a posição final do corredor);
- O usuário ganha a aposta se o corredor escolhido terminar em uma das três primeiras posições;
- O lucro é calculado multiplicando o valor apostado pelas odds do corredor. Se o usuário perder, ele recebe uma mensagem correspondente;

**Corridas Disponíveis:** As corridas são pré-definidas no programa e incluem eventos como:

- São Paulo E-Prix
- Mônaco E-Prix
- Nova Iorque E-Prix
- Berlim E-Prix
- Londres E-Prix

Cada corrida tem sua própria função, e ao ser selecionada pelo usuário, chama a função `exibir_corrida` para iniciar o processo de apostas.

**Navegação no Menu:** O menu principal (`bet_menu`) permite ao usuário selecionar uma corrida para apostar ou visualizar os resultados das apostas feitas;

Há também a opção de retornar ao menu principal do programa (importado do módulo `main`), o que indica que esse sistema de apostas pode ser parte de um programa maior.

A interação com o menu é feita via input do usuário, e a navegação continua até que o usuário escolha sair ou retornar.

**Fluxo de Retorno:** Após cada ação, como apostar ou visualizar os resultados, o usuário é levado de volta ao menu de apostas através da função `voltar_bet`, que pausa o programa até o usuário pressionar ENTER, limpando a tela e exibindo o menu novamente.

**Funções principais:**

- `calcular_odds("posicao")`: Calcular as odds com base na posição do corredor;
- `exibir_corrida(corrida, nome_corrida)`: Exibe a corrida com os competidores, suas posições e odds, e permite que o usuário faça apostas;
- `mostrar_resultados(nft)`: Exibe o resultado final das corridas e calcula o ganho ou perda do usuário com base nas apostas feitas;
- `corrida1`, `corrida2`, `corrida3`, `corrida4`, `corrida5(nft)`: Funções específicas para cada corrida, que chamam `exibir_corrida` e permitem a navegação no menu;
- `bet_menu(nft)`: Menu principal onde o usuário escolhe a corrida ou visualiza os resultados;

### 4.3. database.py

Este arquivo `database.py` parece ser parte de um projeto voltado para interagir com NFTs relacionados à Fórmula E, além de simular um banco de dados onde são armazenados os NFTs disponíveis para compra e informações sobre corridas.

**Estrutura do Banco de Dados:** O arquivo define uma lista chamada `nfts`, onde cada item representa um NFT, consistindo em um dicionário com os seguintes campos:

- `nome`: Nome do NFT;
- `piloto`: Nome do piloto do carro;
- `velocidade`: Um valor aleatório que representa a velocidade do carro;
- `corrida`: Nome da corrida na qual o NFT está associado.

Essa estrutura permite que o sistema tenha um registro organizado de NFTs, facilitando a busca e a visualização de detalhes sobre cada item. É uma implementação simples de um "banco de dados" que armazena informações relevantes sobre os NFTs disponíveis para o usuário.

A lista `nfts` pode ser utilizada por outras partes do sistema, como o menu de visualização e compra de NFTs.

### 4.4. function.py

O arquivo `function.py` é dedicado à criação de ilustrações em ASCII que são exibidas ao usuário durante a interação com o sistema. Ele define uma função chamada `ilustrar`, que usa prints para apresentar uma arte em ASCII relacionada à Fórmula E e aos NFTs, melhorando a estética e a experiência do usuário.

Essa abordagem simples adiciona um toque visual ao sistema e ajuda a manter o usuário engajado durante a navegação pelo programa.

**Opcionais:** Existem outras funções de ilustração que poderiam ser adicionadas ao projeto para enriquecer ainda mais a experiência do usuário.

<br><br>

## 5. Conclusão

O sistema Mahindra Fusion é uma aplicação interativa e moderna que combina apostas em corridas de Fórmula E com a compra de NFTs. Através de uma interface amigável e funcionalidades práticas, os usuários têm a oportunidade de explorar e participar de um ambiente envolvente e dinâmico, promovendo uma experiência única no mundo das corridas e dos tokens não fungíveis.

O projeto reflete a crescente popularidade dos NFTs e das apostas online, sendo uma ótima introdução ao desenvolvimento de sistemas em Python com foco em usabilidade e interação com o usuário.
