from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

app = Flask(__name__)

@app.route("/")
def home ():
    return render_template('index.html')

@app.route("/contato")
def contato ():
    return render_template('contato.html')


@app.route("/produtos")
def produtos():
    listaProdutos = [
        {"home": "Coca cola", "descricao": "Mata a sede e tu tbm =)"},
        {"home": "Bolachinha", "descricao": "Mata tua fone"}
        ]
    return render_template('produtos.html', produtos = listaProdutos)

if __name__ == "__main__":
    app.run()