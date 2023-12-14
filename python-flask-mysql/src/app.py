from flask import Flask, render_template, request, redirect, url_for
import os
import database as db
from flask import url_for



# Obtén la ruta del directorio del script actual
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

app = Flask(__name__, template_folder=template_dir)


# Rutas de la aplicación
@app.route("/")
def home():
    connection =  db.get_database_connection()
      # Obtener la conexión desde el módulo database
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sum")  # Cambiado a 'sum' en lugar de 'Sum'
    myresult = cursor.fetchall()
    # convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        data_dict = dict(zip(columnNames, record))

        # Obtén las URLs completas y agrégales a la respuesta
        data_dict["url_regalo"] = url_for('static', filename=data_dict['regalo'])

        insertObject.append(data_dict)

    cursor.close()
    connection.close()

    return render_template("index.html", data=insertObject)

# ruta para guardar usuarios en la base
@app.route("/user", methods=["POST"])
def addUser():
    username = request.form["nombreYapellido"]  # Nombre de la columna corregido
    direccion = request.form["direccion"]
    regalo = request.form["regalo"]

    if username and direccion and regalo:
        connection = db.get_database_connection()
        cursor = connection.cursor()

        try:
            sql = "INSERT INTO `sum` (`nombreYapellido`, `direccion`, `regalo`) VALUES (%s, %s, %s)"  # Nombre de las columnas corregido
            data = (username, direccion, regalo)
            cursor.execute(sql, data)
            connection.commit()
        except Exception as e:
            print(f"Error al insertar en la base de datos: {e}")
        finally:
            cursor.close()
            connection.close()

    return redirect(url_for("home"))


# metodo para editar
@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    try:
        username = request.form["nombreYapellido"]
        direccion = request.form["direccion"]
        regalo = request.form["regalo"]

        sql = "UPDATE `sum` SET `nombreYapellido` = %s, `direccion` = %s, `regalo` = %s WHERE id = %s"
        data = (username, direccion, regalo, id)
        cursor.execute(sql, data)
        connection.commit()
    except Exception as e:
        print(f"Error al actualizar en la base de datos: {e}")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for("home"))


# Ruta para eliminar usuarios
@app.route('/delete/<string:id>')
def delete(id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    try:
        sql = "DELETE FROM `sum` WHERE id = %s"
        cursor.execute(sql, (id,))
        connection.commit()
    except Exception as e:
        print(f"Error al eliminar en la base de datos: {e}")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True, port=4000)
