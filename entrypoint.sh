#!/bin/sh

#Executa as migracoes do banco de dados
poetry run alembic upgrade head

#inicia a aplicacao
poetry run fastapi run fast_zero/app.py --host 0.0.0.0
