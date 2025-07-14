from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        notas = [float(request.form.get(f'nota{i}')) for i in range(1,4)]
        asistencia = float(request.form.get('asistencia'))
        promedio = sum(notas)/3
        estado = 'Aprobado' if promedio >= 40 and asistencia >= 75 else 'Reprobado'
        resultado = {'promedio': promedio, 'estado': estado}
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombres = [request.form.get(f'nombre{i}') for i in range(1,4)]
        nombre_largo = max(nombres, key=len)
        resultado = {'nombre': nombre_largo, 'longitud': len(nombre_largo)}
    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
