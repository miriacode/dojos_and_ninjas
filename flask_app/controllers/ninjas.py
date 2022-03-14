from flask import Flask, render_template, request, redirect

from flask_app import app
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo


@app.route('/dojos')
def show_index():
    dojos = Dojo.muestra_dojos()
    return render_template("index.html", dojos=dojos)

@app.route('/ninjas')
def show_new():
    dojos = Dojo.muestra_dojos()
    return render_template("new.html", dojos=dojos)


@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        "dojo_id":dojo_id
    }
    ninjas = Ninja.get_ninjas_by_dojo_id(data)
    return render_template("dojo.html", ninjas=ninjas)


@app.route('/dojos/add', methods=['POST'])
def add_dojo():
    data = {
            "name": request.form['name']
            } 
    print(data)
    Dojo.add_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/newninja', methods=['POST'])
def add_ninja():
    print(request.form)
    Ninja.guardar(request.form)
    return redirect('/dojos')


