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
        {"nome": "Coca cola", "descricao": "Mata a sede e tu tbm =)", "imagem": "https://p.turbosquid.com/ts-thumb/HX/VJZEKq/Kb/01/jpg/1630333961/600x600/fit_q87/aff8f4e9ab2bb3481c7e37abfdac8e9d2aae071f/01.jpg"},
        {"nome": "Bolachinha", "descricao": "Mata tua fome", "imagem": "https://static.itdg.com.br/images/360-240/340f3563c37c9741cb962a1309793f0c/264064-original.jpg"}
        ]
    return render_template('produtos.html', produtos = listaProdutos)

@app.route("/termos")
def termos ():
    return render_template('termos.html')

@app.route("/politica")
def politia ():
    return render_template('politica.html')

@app.route("/howto")
def howto ():
    return render_template('howto.html')

if __name__ == "__main__":
    app.run()