from flask import Flask
from validate_docbr import CPF
from validate_docbr import CNPJ

app = Flask("minha aplicação")


@app.route("/")
def home ():
    return "<h1>Home Page</h1>"

@app.route("/contato")
def contato ():
    return "<h1>Contato</h1>"

@app.route("/gerar-cpf")
def gerarCPF ():
    cpf = CPF()

    new_cpf_one = cpf.generate(True)

    return ("<h2> CPF: " + new_cpf_one + " </h2>")

@app.route("/gerar-cnpj")
def gerarCNPJ():
    cnpj = CNPJ()

    new_cnpj_one = cnpj.generate(True)

    return ("<h2> CNPJ: " + new_cnpj_one + " <h2>")

@app.route("/servicos")
def servicos():
    return "<h1> Nossos Serviços <h1>"

@app.route("/sobre")
def sobre ():
    return "<h1>Sobre</h1>"


# /gerar-cpf (deve devolver um cpf random)
# /gerar-cnpj (deve devolver um cnpj random)
# /servicos (deve devolver um título com "Nossos Serviços")




app.run()