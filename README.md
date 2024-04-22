# Telemedicina

Projeto criado durante o evento PYSTACK WEEK 10 da Pythonando.
Foram utilizados principalmente Python e Django, além de SQLITE3 para armazenar os dados e Bootstrap como framework visual.

Este projeto é sistema de Telemedicina, permitindo o gerenciamento de consultas tanto para médicos quanto pacientes. 

Visualizar requisito de Telas no [Figma](https://www.figma.com/proto/BLKeIQ7XgxIGnSQnfqGIed/Untitled?type=design&node-id=2-3&scaling=min-zoom&page-id=0%3A1)


### Funcionaldades Básicas

**Paciente:**
- Realizar cadastro 
- Consultar especialidades e médicos
- Consultar disponibilidade de horários, agendar e cancelar consultas
- Receber o link da consulta no horário agendado  
- Verificar anexos (receitas, atestados, etc)

**Médico:**
- Realizar cadastro 
- Abrir horários para consultas 
- Verificar agenda, colocar link da consulta, anexar documentos
- Iniciar ou cancelar consultas 
- Verificar Desempenho (quantas consultas, valor recebido, etc)


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

