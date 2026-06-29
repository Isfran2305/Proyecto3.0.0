from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = ""

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "+":
                resultado = num1 + num2
            elif operacion == "-":
                resultado = num1 - num2
            elif operacion == "*":
                resultado = num1 * num2
            elif operacion == "/":
                resultado = "No se puede dividir entre cero" if num2 == 0 else num1 / num2
        except:
            resultado = "Datos inválidos"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculadora</title>
        <style>
            body {{
                font-family: Arial;
                background: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .contenedor {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,.2);
                text-align: center;
            }}
            input, select, button {{
                margin: 8px;
                padding: 10px;
                font-size: 16px;
            }}
            h2 {{
                color: #2563eb;
            }}
        </style>
    </head>
    <body>
        <div class="contenedor">
            <h2>🧮 Calculadora</h2>

            <form method="POST">
                <input type="number" step="any" name="num1" placeholder="Número 1" required><br>

                <select name="operacion">
                    <option value="+">+</option>
                    <option value="-">-</option>
                    <option value="*">×</option>
                    <option value="/">÷</option>
                </select><br>

                <input type="number" step="any" name="num2" placeholder="Número 2" required><br>

                <button type="submit">Calcular</button>
            </form>

            <h3>Resultado: {resultado}</h3>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)