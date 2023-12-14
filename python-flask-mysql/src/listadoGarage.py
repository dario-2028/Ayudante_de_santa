from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

# Obtén la ruta del directorio del script actual
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

app = Flask(__name__, template_folder=template_dir)


# Rutas de la aplicación
@app.route("/")
def home():
    connection = db.get_database_connection()
    # Obtener la conexión desde el módulo database
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  listadogarage")  # Cambiado a 'sum' en lugar de 'Sum'
    myresult = cursor.fetchall()
    # convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()  # Cerrar el cursor
    connection.close()  # Cerrar la conexión a la base de datos
    return render_template("index2.html", data=insertObject)


# ruta para guardar usuarios en la base
@app.route("/user", methods=["POST"])
def addUser():
    nombreYapellido = request.form["nombreYapellido"]  # Nombre de la columna corregido
    marcaVehiculo = request.form["marcaVehiculo"]
    patente = request.form["patente"]
    fechaDeIngreso = request.form["fechaDeIngreso"]  # Nombre de la columna corregido
    fechaDeEgreso = request.form["fechaDeEgreso"]
    foto = request.form["foto"]
    pago = request.form["pago"]

    if (
        nombreYapellido
        and marcaVehiculo
        and patente
        and fechaDeIngreso
        and fechaDeEgreso
        and foto
        and pago
    ):
        connection = db.get_database_connection()
        cursor = connection.cursor()

        try:
            sql = "INSERT INTO listadogarage ( nombreYapellido, marcaVehiculo, patente,fechadeIngreso ,fechaDeEgreso,foto ,pago) VALUES (%s, %s, %s,%s, %s, %s,%s)"  # Nombre de las columnas corregido
            data = (
                nombreYapellido,
                marcaVehiculo,
                patente,
                fechaDeIngreso,
                fechaDeEgreso,
                foto,
                pago,
            )
            cursor.execute(sql, data)
            connection.commit()
        except Exception as e:
            print(f"Error al insertar en la base de datos: {e}")
        finally:
            cursor.close()
            connection.close()

    return redirect(url_for("home"))


# metodo para editar
@app.route("/edit/<string:idEstacionamiento>", methods=["PUT"])
def edit(idEstacionamiento):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    try:
        nombreYapellido = request.form["nombreYapellido"]
        marcaVehiculo = request.form["marcaVehiculo"]
        patente = request.form["patente"]
        fechaDeIngreso = request.form["fechaDeIngreso"]
        fechaDeEgreso = request.form["fechadeEgreso"]
        foto = request.form["foto"]
        pago = request.form["pago"]

        sql = "UPDATE listadogarage SET nombreYapellido = %s, marcaVehiculo = %s, patente = %s,fechaDeEgreso = %s, fechaDeIngreso = %s, foto = %s ,pago = %s WHERE idEstacionamiento = %s"
        data = (
            nombreYapellido,
            marcaVehiculo,
            patente,
            fechaDeIngreso,
            fechaDeEgreso,
            foto,
            pago,
            idEstacionamiento,
        )
        cursor.execute(sql, data)
        connection.commit()
    except Exception as e:
        print(f"Error al actualizar en la base de datos: {e}")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for("home"))


# Ruta para eliminar usuarios
@app.route("/delete/<string:idEstacionamiento>")
def delete(idEstacionamiento):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    try:
        sql = "DELETE FROM listadogarage  WHERE idEstacionamiento = %s"
        cursor.execute(sql, (idEstacionamiento))
        connection.commit()
    except Exception as e:
        print(f"Error al eliminar en la base de datos: {e}")
    finally:
        cursor.close()
        connection.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
