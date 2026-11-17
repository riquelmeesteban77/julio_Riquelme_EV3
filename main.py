from flask import Flask, render_template, request
app = Flask(__name__)
#Ruta principal muestra los dos botones
@app.route('/')
def home():
    return render_template('index.html')
#ruta ejercicio 1 procesa notas y asistencia desde ejercicio1.html
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None #resultado parte como None porque no se han procesado datos
    estado = None #estado parte como None porque cuando se inicia la página no hemos ingresado datos
    if request.method == 'POST':
        #Utilizamos bloque try-catch para asegurar el ingreso del tipo de dato correcto
        try:
            #Captura los datos del formulario
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            #Calculo promedio
            promedio = round((nota1 + nota2 + nota3) /3, 1)

            #Validacion de aprobacion
            #Promedio sea mayor o igual a 40, asistencia sea mayor o igual a 75%, estado será APROBADO
            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"
            #Diccionario, que cumple el rol de empaquetar los datos ya procesados y los pasa de una sola vez a la plantilla HTML
            resultado = {
                'promedio': promedio,
                'asistencia': asistencia,
                'estado': estado
            }
        #Capturamos ValueError en caso de que algún usuario valores fuera de rangos
        except ValueError:
            resultado = {'error: ' 'Por favor, ingres números válidos'}
    return render_template('ejercicio1.html', resultado=resultado)
#ruta ejercicio 2 procesa el nombre mas largo y el contador de caracteres desde ejercicio2.html
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        if not nombre1 or not nombre2 or not nombre3:
            resultado = {'error': 'Por favor, completa todos los campos.'}
        else:
            # Creamos una lista con los nombres ingresados
            nombres = [nombre1, nombre2, nombre3]

            # Buscamos el nombre con mayor cantidad de caracteres (en caso de empate, max toma el primero)
            nombre_largo = max(nombres, key=len)
            cantidad_caracteres = len(nombre_largo)

            resultado = {
                'nombre_largo': nombre_largo,
                'caracteres': cantidad_caracteres
            }

    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)