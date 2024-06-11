from flask import Flask

app = Flask("minha aplicação")


@app.route("/")
def home ():
    return "<h1>Home Page</h1>"

@app.route("/contato")
def contato ():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos ():
    return "<h1>Produtos</h1>"

@app.route("/sobre")
def sobre ():
    return "<h1>Sobre</h1>"