# ContactKeeper 📞 📧 🔐

Durante muitos séculos, a comunicação por escrita apenas existiu através de cartas registradas somadas a uma longa espera para ser entregue ao destinatário. 
Já nos tempos atuais, grande parte da nossa comunicação se deve através da internet, através de aplicativos de mensagens, redes sociais e emails. Em que garantem uma entrega quase momentânea ao destinatário. 

Porém, quase todos os nossos contatos estão "espalhados" em aplicativos de emails e lista telefônica (em que estão disponíveis apenas no telemóvel). Caso perca o telemóvel.... Já se foram os contatos. 

E nesse contexto que surge a ContactKeeper...


## Objetivo da aplicação:

O objetivo da ContactKeeper é garantir que todos os seus contatos estejam salvos em um só lugar disponível em qualquer lugar.
Seja pelo telemóvel, pelo tablet, pelo portátil, pelo computador ou qualquer outro aparelho eletrônico que se conecte a internet, você terá acesso ao seus contatos. Sem risco algum de perdê-los devido ao fato de estarem salvos em apenas um aparelho. 


## Por que Django?

Escolhi Django como minha framework, basicamente por ter um grande leque de templates já pré prontas, onde devo apenas importá-las e utilizá-las mediante a necessidade do meu projeto. Além do mais, tudo que preciso e como utilizar está na documentação fornecida pela própria framework. 
Outros dois pontos cruciais para minha escolha, foi a fácil administração do banco de dados que esta framework oferece e a segurança não só na criação quando  como também no armazenamento dos mesmos. 


## Processo de Instalação: 

1. Clone o nosso repositório disponível em  [ContactKeeper - Repositorio](https://github.com/G00li/Backend1-Contatos.git)
2. Busque pelo repositório clonado em sua máquina e aceda ao ficheiro `Project`
3. Abra o Terminal de Comandos dentro do ficheiro Project
4. Execute o comando
	```
	docker-compose up --build
	```
5. Aceda o localhost no seu navegador utilizando o endereço abaixo na barra de endereços
	```
	http://localhost:8000/
	```


## Como utilizar a aplicação: 

Caso tenha utilizador: 
1. **Login** 
	Ao entrar na aplicação, será requisitado seu login e password para que entre no seu respectivo perfil de usuário e obtenha todos os seus dados 
	
2. **Pesquisar contato desejado** 
	Ao aceder seu perfil, você poderá pesquisar o contato desejado e, caso encontre, conseguirá aceder a informação
	
3. **Criar novo contato**
	Caso queira adicionar um novo contato na sua lista de contatos, basta preencher um formulário com o nome, apelido, telemóvel, email (opcional) e, caso queira, poderá não só adicionar uma descrição para se recordar de onde reconhece aquela pessoa, como também poderá categorizá-lo com uma tag já existente ou então gerar uma nova. 
	Além disso, será salvo a data e a hora da criação daquele contato específico. 
	
4. **Deletar Contato** 
	O utilizador poderá excluir um contato ao aceder suas informações. 

O ContactKeeper também permite ao usuário organizar seus contatos por nome, categoria e telemóvel. 


