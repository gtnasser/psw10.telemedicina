#!/usr/bin/env python
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healing.settings')

try:
    django.setup()
    from django.contrib.auth.models import User
    from medico.models import Especialidades
 
    print('Especialidades:')
    if not Especialidades.objects.filter(especialidade='cardiologia').exists():
        newrec = Especialidades.objects.create(especialidade='cardiologia')
    if not Especialidades.objects.filter(especialidade='clin.geral').exists():
        newrec = Especialidades.objects.create(especialidade='clin.geral')
    if not Especialidades.objects.filter(especialidade='psicologia').exists():
        newrec = Especialidades.objects.create(especialidade='psicologia')
    esps = Especialidades.objects.all() 
    for esp in esps:
        print(f'- {esp}')

except ImportError as exc:
    raise ImportError("Erro na inclusao dos registros Demo. Utilize o Django Admin para cria-los.")
