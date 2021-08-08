from flask import Flask, render_template, url_for
import os
app = Flask(__name__, static_folder=os.path.abspath('static'))


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/video')
def video():
    return render_template("video.html")


#@app.route('/<page_name>/<string:num>')
#def gallery_img(page_name, num):
#    if page_name == "poemas_menores" or page_name == "st" or page_name == "respuestas":
 #       return render_template("collages.html", value=page_name, num=num)
  #  if page_name == "hojas_cuadriculadas" or page_name == "pezoneras":
   #     return render_template("objetos.html", value=page_name)
    #return render_template("gallery_img.html", name=page_name, num=num)


@app.route('/<page_name>')
def html_page(page_name):
    name = page_name.replace('_', ' ')
    aux = name.upper()
    texto = open("static/texts/"+page_name+".txt", "r")
    if page_name == "poemas_menores" or page_name == "st" or page_name == "respuestas":
        return render_template("collages.html", value=page_name, titulo=aux, texto=texto.read())
    if page_name == "hojas_cuadriculadas" or page_name == "pezoneras":
        return render_template("objetos.html", value=page_name, titulo=aux, texto=texto.read())
    return render_template("gallery.html", value=page_name, titulo=aux, texto=texto.read())
