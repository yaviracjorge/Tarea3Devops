from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Bienvenido</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #4facfe, #00f2fe);
                font-family: Arial, sans-serif;
            }

            .contenedor {
                background: white;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
                text-align: center;
            }

            h1 {
                color: #333;
                font-size: 3rem;
                margin-bottom: 10px;
            }

            p {
                color: #666;
                font-size: 1.2rem;
            }

            .boton {
                margin-top: 20px;
                display: inline-block;
                padding: 12px 25px;
                background: #4facfe;
                color: white;
                text-decoration: none;
                border-radius: 10px;
                transition: 0.3s;
            }

            .boton:hover {
                background: #007bff;
            }
        </style>
    </head>
    <body>
        <div class="contenedor">
            <h1>¡Bienvenido!</h1>
            <p>Esta página fue creada con Python y Flask.</p>
            <a href="#" class="boton">Comenzar</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)