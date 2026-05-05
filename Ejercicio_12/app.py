from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

productos = []
ultimo_codigo = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scanner")
def scanner():
    return render_template("scanner.html")

@app.route("/guardar", methods=["POST"])
def guardar():
    global ultimo_codigo

    data = request.get_json()
    codigo = data["codigo"]

    if codigo != ultimo_codigo:
        productos.append(codigo)
        ultimo_codigo = codigo
        print("Agregado:", codigo)

    return jsonify({"ok": True})

@app.route("/productos")
def productos_lista():
    return jsonify(productos)

@app.route("/eliminar", methods=["POST"])
def eliminar():
    data = request.get_json()
    codigo = data["codigo"]

    if codigo in productos:
        productos.remove(codigo)

    return jsonify({"ok": True})

@app.route("/limpiar", methods=["POST"])
def limpiar():
    global productos
    productos = []
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
