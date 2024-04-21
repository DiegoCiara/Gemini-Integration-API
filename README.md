# Gemini Integration API
Este projeto é um exemplo feito em Python utilizando Flask para integração com o modelo gemini-1.5-pro, com o propósito de responder perguntas em JSON para que seja integrada em outras aplicações. Com este projeto, pode-se fazer com que uma API consuma o JSON retornado pela resposta da assistente e cadastre-a em um DB, ou que um front-end consuma a resposta para mostrar ao usuário ou utilizar em um sistema. A vantagem desse projeto é fazer com que as respostas que precisariam ser configuradas, sejam personalizada de acordo com a necessidade de cada projeto, na pasta `/system_instructions`, economizando tempo de configuração de um projeto.

## Instalando as dependências:
`pip install Flask google-generativeai`

### Insira suas instruções na pasta `/system_instructions` na raiz do projeto.

## Adicionando API_KEY nas variáveis de ambiente:
Gere e copie sua chave API do Gemini em https://aistudio.google.com/app/.
No Linux ou MacOS, adicione uma linha no arquivo `~/.bashrc` (ou `~/.bash_profile,` dependendo do shell que você usa) com o seguinte:
`export API_KEY_GEMINI="sua_chave_api_gemini"`

Após editar o arquivo, execute:
`source ~/.bashrc`

## Rodando um ambiente virtual:
`python3 -m venv venv`                 
`source venv/bin/activate`

## Ou caso não der certo:
`pip install virtualenv`               
`virtualenv venv`

## Rodando o projeto em um ambiente de desenvolvimento:
`flask run`

Certifique-se de criar um ambiente virtual antes de rodar o projeto.