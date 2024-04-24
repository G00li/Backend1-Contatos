
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

Ao iniciar o seu ContactKeeper será exibido todos os seus contatos salvos. 

#### Na nave bar : 
-  Temos o nome da nossa aplicação que também funciona como um botão de Home. 
- Temos a barra de pesquisa, onde o utilizador pode inserir nome, apelido, telemóvel ou o email desejado. 

#### Na lista de contatos: 
É onde será exibido todos os seus contatos, divididos em 5 campos.
1. **ID** -> Onde será informado a ordem de registros que o contato foi criado. Por padrão, será exibido o ultimo contato adicionado primeiro na lista de contatos
2. **O primeiro nome** -> Nome em que o utilizador cadastrou o contato
3. **Apelido** -> Apelido que o utilizador cadastrou o contato
4. **Telemóvel** -> Exibe o telemóvel do contato
5. **Email** -> Exibe o email do contato 

## Licença MIT

Este projeto tem a licença fornecida através do [MIT License](https://opensource.org/license/mit)
