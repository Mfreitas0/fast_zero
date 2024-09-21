# Gerenciador de Tarefas - Lista de Tarefas

O principal objetivo deste projeto é criar uma API funcional e robusta para gerenciar tarefas. A aplicação 
permitirá que os usuários se autentiquem, criem, leiam, atualizem, excluam tarefas e aplicando autenticação
de usuários e operações CRUD completas. Tudo isso será feito 
garantindo que a API seja confiável e devidamente testada.

## Ferramentas e Tecnologias Utilizadas

Para a construção do projeto, utilizaremos:

- **FastAPI** v0.114: Framework moderno para a construção de APIs.
- **Pydantic** v2.0: Validação de dados e modelagem.
- **SQLAlchemy ORM** v2.0: Mapeamento objeto-relacional para o banco de dados.
- **Alembic**: Gerenciamento de migrações de banco de dados.
- **Python 3.11/3.12**: Linguagem de programação.
- **Pytest**: Framework para testes, garantindo que as APIs sejam funcionais e confiáveis.

## Funcionalidades

- **Autenticação de Usuários**: Sistema de registro, login e autenticação JWT (JSON Web Tokens).
- **CRUD de Tarefas**:
  - **Criação**: Adicione novas tarefas à sua lista.
  - **Leitura**: Liste todas as tarefas ou visualize uma tarefa específica.
  - **Atualização**: Atualize o status ou detalhes de uma tarefa.
  - **Exclusão**: Remova tarefas que não são mais necessárias.
- **Testes Automatizados**: O projeto inclui uma suíte de testes desenvolvida com **pytest** para garantir a qualidade da API.

## Deploy

Este projeto está disponível online através do Fly.io. Você pode acessar a API clicando no link abaixo:

[Gerenciador de Tarefas no Fly.io](https://fastzeroapp-0001.fly.dev)

## Instalação e Execução

### Pré-requisitos

- [Docker](https://www.docker.com/get-started)
- [Python 3.11+](https://www.python.org/downloads/)

### Passos para rodar o projeto

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/gerenciador-tarefas.git
    cd gerenciador-tarefas
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Execute as migrações de banco de dados:

    ```bash
    alembic upgrade head
    ```

4. Inicie a aplicação com o Docker:

    ```bash
    docker-compose up
    ```

5. Acesse a API no navegador:

   - Documentação interativa (Swagger UI): [http://localhost:8000/docs](http://localhost:8000/docs)
   - OpenAPI schema: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

## Testes

Rodar os testes é simples com o **pytest**:

```bash
pytest
```

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
