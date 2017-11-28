#!/usr/bin/python

import os
import sys

if sys.argv[-1] == 'rs':
    os.system('pipenv run python ./unolog/manage.py runserver_plus')
elif sys.argv[-1] == 'sh':
    os.system('pipenv run python ./unolog/manage.py shell_plus')
elif sys.argv[-1] == 'm':
    os.system('pipenv run python ./unolog/manage.py migrate')
elif sys.argv[-1] == 'mm':
    os.system('pipenv run python ./unolog/manage.py makemigrations')

elif len(sys.argv) > 1:
    os.system('pipenv run python ./unolog/manage.py {0}'.format(sys.argv[-1]))
