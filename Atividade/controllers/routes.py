import urllib.request
from flask import render_template, request
import urllib
import json

filmes_list = ["https://m.media-amazon.com/images/I/51EG732BV3L.jpg",
                "https://upload.wikimedia.org/wikipedia/pt/a/a7/Toy_Story_1995.jpg",
                "https://play-lh.googleusercontent.com/64SMx5o6rrX5HIGVkKt8aJaunQ-owWPlvqRv-MBTs4ZMF5yk3-X-nPj7GmSmuPqiAkg23HgOI8O9mNPgLw",
                "https://m.media-amazon.com/images/I/91kFYg4fX3L._AC_SY679_.jpg",
                "https://m.media-amazon.com/images/I/51Qvs9i5a%2BL._AC_.jpg"]
filmes_dici = [
    {
        "nome": "Matrix",
        "ano": 1999,
        "publico": "Fãs de ficção científica e ação",
        "idade_minima": 14,
        "imagem": "https://m.media-amazon.com/images/I/51EG732BV3L.jpg"
    },
    {
        "nome": "Toy Story",
        "ano": 1995,
        "publico": "Infantil e família",
        "idade_minima": 0,
        "imagem": "https://upload.wikimedia.org/wikipedia/pt/a/a7/Toy_Story_1995.jpg"
    },
    {
        "nome": "Coringa",
        "ano": 2019,
        "publico": "Adultos",
        "idade_minima": 18,
        "imagem": "https://play-lh.googleusercontent.com/64SMx5o6rrX5HIGVkKt8aJaunQ-owWPlvqRv-MBTs4ZMF5yk3-X-nPj7GmSmuPqiAkg23HgOI8O9mNPgLw=w240-h480-rw"
    },
    {
        "nome": "Interstellar",
        "ano": 2014,
        "publico": "Adultos e jovens",
        "idade_minima": 12,
        "imagem": "https://m.media-amazon.com/images/I/91kFYg4fX3L._AC_SY679_.jpg"
    },
    {
        "nome": "O Senhor dos Anéis: A Sociedade do Anel",
        "ano": 2001,
        "publico": "Fãs de fantasia e aventura",
        "idade_minima": 12,
        "imagem": "https://m.media-amazon.com/images/I/51Qvs9i5a%2BL._AC_.jpg"
    }
]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/filmes_lista',methods=['GET','POST'])
    def filmes():
        # filmes = ["Matrix", "Toy Story", "Coringa", "Interstellar", "O Senhor dos Anéis: A Sociedade do Anel"]
    

        if request.method == 'POST':
            if request.form.get('imagem'):
                filmes_list.append(request.form.get('imagem'))
        return render_template('filmes_lista.html',filmes=filmes_list)



    @app.route('/filmes_dicionario',methods=['GET','POST'])
    def filme():
        if request.method == 'POST':
            nome = request.form.get('nome')
            ano = request.form.get('ano')
            publico = request.form.get('publico')
            idade_minima = request.form.get('idade_minima')
            imagem = request.form.get('imagem')
            
            
            novo_filme = {
                "nome": nome,
                "ano": int(ano),  
                "publico": publico,
                "idade_minima": int(idade_minima),  
                "imagem": imagem
            }
            
            
            filmes_dici.append(novo_filme)
        
        return render_template('filmes_dicionario.html', filmes=filmes_dici)

    @app.route('/rickandmorty',methods=['GET','POST'])
    def rick():
        url = "https://rickandmortyapi.com/api/character"
        res= urllib.request.urlopen(url)
        data = res.read()
        desenho = json.loads(data)

        return render_template('rickandmorty.html', desenho=desenho)