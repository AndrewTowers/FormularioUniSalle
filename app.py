from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# 🔗 Conexión a MongoDB Atlas
client = MongoClient("mongodb+srv://andrew:Is3H6lgZWSmLBpid@cluster0.se0juh3.mongodb.net/")
print("Conectado a Mongo:", db.list_collection_names())

db = client.FormularioUniSalle
collection = db.formulario

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        collection.insert_one({
            'nombre': nombre,
            'correo': correo,
            'mensaje': mensaje
        })
        return redirect('/')
    return render_template('front.html')

if __name__ == "__main__":
    app.run(debug=True)
