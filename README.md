# Telemedicina

Projeto criado durante o evento PYSTACK WEEK 10 da [Pythonando](https://pythonando.com.br/psw/evento/).
Foram utilizados principalmente Python e Django, além de SQLITE3 para armazenar os dados e Bootstrap como framework visual.

Este projeto é sistema de Telemedicina, permitindo o gerenciamento de consultas tanto para médicos quanto pacientes.

Visualizar requisito de Telas no [Figma](https://www.figma.com/proto/BLKeIQ7XgxIGnSQnfqGIed/Untitled?type=design&node-id=2-3&scaling=min-zoom&page-id=0%3A1)


### Funcionaldades Básicas

**Usuário:**
- Realizar cadastro, login e logout
- Habilitar funcialidades conforme o perfil do usuário

**Paciente:**
- Consultar especialidades e médicos
- Consultar disponibilidade de horários, agendar e cancelar consultas
- Receber o link da consulta no horário agendado
- Verificar anexos (receitas, atestados, etc)

**Médico:**
- Realizar cadastro
- Abrir horários para consultas
- Verificar agenda, colocar link da consulta, anexar documentos
- Iniciar ou cancelar consultas



### Para executar este projeto:

1. Abrir o terminal e executar os comandos abaixo:

```shell
git clone https://github.com/gtnasser/psw10.telemedicina.git
cd psw10.telemedicina
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python3 manage.py createsuperuser
python manage.py runserver
```

2. Abrir o browser e executar o sistema em [http://127.0.0.1:8000/usuarios/login](http://127.0.0.1:8000/usuarios/login/)

3. Abrir o módulo de administração do Django, login usando o superusuário, em [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/)

É necessário cadastrar as especialidades manualmente, através do módulo de administração.

### Melhorias Pós-Evento

Entendo que o evento, dentro de seu tempo limitado, tenha que abranger prioritariamente a implementação das funcionalidades básicas de um sistema utilizando Python e Django.
Assim, após o evento, temos a oportunidades de implementar várias melhorias para tornar o sistema mais robusto, confiável, e fácil de utilizar.
Isso complementa o objetivo principal de aprendizado em Python e Django, abrangendo também HTML, CSS e Bootstrap.

**Usuário:**
- redirecionar para tela de login quando não autenticado
- barra de navegação: mostrar o nome do usuário logado e incluir a opção *Sair*


