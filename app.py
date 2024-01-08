from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión MySQL
db_config = {
    'host': '192.168.0.188',
    'user': 'fabrixio',
    'password': '1234',
    'database': 'prueba',
}

# Ruta para el formulario
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener datos del formulario
        edad = request.form['edad']
        diabetes = request.form['diabetes']
        hospitalizacion = request.form['hospitalizacion']

        # Conectar a la base de datos MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insertar datos en la tabla
        query = "INSERT INTO pruebarda (edad, diabetes, hospitalizacion) VALUES (%s, %s, %s)"
        values = (edad, diabetes, hospitalizacion)
        cursor.execute(query, values)

        # Confirmar la transacción y cerrar la conexión
        conn.commit()
        cursor.close()
        conn.close()

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
