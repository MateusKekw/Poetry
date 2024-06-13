A PU KA - TI KA - I T S 


curl -sSL https://install.python-poetry.org | python3 -

export PATH="/home/estudante1/.local/bin:$PATH"

poetry --version

poetry new projeto_lp3

poetry shell

 Ctrl + Shift + P Select Interpreter

Selecionar o ambiente virtual

poetry add Flask

flask --app projeto_lp3/app.py run

poetry run flask --app projeto_lp3/app.py run
