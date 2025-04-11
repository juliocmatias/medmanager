# 🩺 MedManager API

API RESTful de **Gerenciamento de Consultas Médicas**, desenvolvida como parte de um processo seletivo para uma ONG com foco em inclusão social.

O projeto tem como objetivo oferecer uma base sólida, segura e escalável para futuras integrações com sistemas como pagamentos (AssAs) e fluxos de deploy automatizados.

---

## 🧰 Tecnologias Utilizadas

- [Python 3.12](https://www.python.org/)
- [Django 5.x](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Poetry](https://python-poetry.org/) — gerenciamento de dependências
- [PostgreSQL](https://www.postgresql.org/) — banco de dados
- [Docker](https://www.docker.com/) — ambiente isolado
- [GitHub Actions](https://github.com/features/actions) — CI/CD (a implementar)

---

## 🚀 Como rodar o projeto

### 📦 Usando Docker (recomendado)

> Pré-requisitos: Docker + Docker Compose instalados

```bash
# Subir a aplicação
docker-compose up --build

# Aplicar migrações (em outro terminal)
docker-compose exec web python manage.py migrate

# Criar superusuário (opcional)
docker-compose exec web python manage.py createsuperuser

```

Acesse: http://localhost:8000/admin

### 💻 Sem Docker (modo local com Poetry)

>Pré-requisitos: Python 3.12+, Poetry

```bash
# Instalar dependências
poetry install

# Ativar ambiente virtual
poetry shell

# Rodar migrações
make migrate

# Criar superusuário (opcional)
make superuser

# Iniciar o servidor
make run
```

## 🔌 Endpoints principais (ainda em construção)

| **Recurso**       | **Método**    | **Rota**                                      | **Descrição**                           |
|--------------------|---------------|-----------------------------------------------|-----------------------------------------|
| **Profissionais**  | `GET`         | `/api/health-professionals/`                 | Listar todos os profissionais           |
| **Profissionais**  | `POST`        | `/api/health-professionals/`                 | Cadastrar um novo profissional          |
| **Profissionais**  | `PUT`/`PATCH` | `/api/health-professionals/<id>/`            | Atualizar informações de um profissional|
| **Profissionais**  | `DELETE`      | `/api/health-professionals/<id>/`            | Excluir um profissional específico      |
| **Consultas**      | `POST`        | `/api/appointments/`                         | Agendar uma nova consulta               |
| **Consultas**      | `GET`         | `/api/appointments/?professional=<id>`       | Buscar consultas por profissional       |

## 🧪 Comandos úteis

Todos os comandos são executados com `make`:

| Comando                | Descrição                                                 |
|------------------------|-----------------------------------------------------------|
| `make test`            | Executa os testes com pytest                              |
| `make lint`            | Verifica problemas de lint com Flake8                     |
| `make format`          | Formata o código com isort e black                        |
| `make check-format`    | Verifica se o código está formatado corretamente          |
| `make check-format-fix`| Verifica e corrige a formatação com black e isort         |
| `make run`             | Inicia o servidor Django                                  |
| `make dev`             | Alias para `make run` (mantido por organização/flexibilidade) |


## ✅ Checklist do Desafio

- [x] **Cadastro e gerenciamento de profissionais**  
  Funcionalidades para cadastrar, atualizar, listar e excluir profissionais de saúde.

- [x] **Agendamento de consultas vinculadas**  
  Permite o agendamento de consultas associadas a profissionais cadastrados.

- [x] **Busca por ID da pessoa profissional**  
  Implementação da funcionalidade de busca detalhada de um profissional pelo seu ID.

- [x] **Sanitização e segurança nos dados**  
  Validação e proteção dos dados contra vulnerabilidades.

- [ ] **Deploy em Staging e Produção**  
  Configuração de ambientes de staging e produção.

- [ ] **Integração com AssAs (split de pagamento)**  
  Integração com o serviço AssAs para split de pagamentos.

- [ ] **Documentação de fluxo de rollback**  
  Instruções claras para rollback em caso de falhas no deploy.

- [ ] **Cobertura de testes + CI (GitHub Actions)**  
  Alta cobertura de testes e integração contínua com GitHub Actions.


## 🫂 Sobre a iniciativa

Este projeto faz parte de um processo seletivo de uma ONG que atua com inclusão social e saúde. O sistema busca garantir que pessoas trans, LGBTQIAPN+ e outras populações vulnerabilizadas tenham acesso a atendimentos médicos com dignidade e respeito.

## 📄 Licença

Este projeto está sob a licença MIT.