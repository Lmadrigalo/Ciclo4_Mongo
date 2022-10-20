from flask import Flask
from flask import request
from flask import jsonify
from waitress import serve
import json
from controladores.estudianteControlador import EstudianteControlador

mi_aplicacion = Flask(__name__)

# instanciar un objeto de tipo controlador de estudiante
_controlador_estudiante = EstudianteControlador()

"""PATH PARA ADMINISTRAR ESTUDIANTES"""

# GET - LISTAR ESTUDIANTES
@mi_aplicacion.route('/estudiantes', methods=['GET'])
def listar_estudiante():
    datos_salida = _controlador_estudiante.listar_estudiante()
    return jsonify(datos_salida)

# POST -  CREAR ESTUDIANTES
@mi_aplicacion.route('/estudiantes', methods=['POST'])
def crear_estudiante():
    datos_entrada = request.get_json()
    datos_salida = _controlador_estudiante.crear_estudiante(datos_entrada)
    return jsonify(datos_salida)

# PUT - ACTUALIZAR
@mi_aplicacion.route('/estudiantes/<string:id>', methods=['PUT'])
def modificarEstudiante(id):
    datos_entrada = request.get_json()
    json= _controlador_estudiante.actualizar_estudiante(id,datos_entrada)
    return jsonify(json)

def cargar_configuracion():
    with open("config.json") as archivo:
        datos_configuracion = json.load(archivo)
    return datos_configuracion

# DELETE - ELIMINAR ESTUDIANTES
@mi_aplicacion.route('/estudiantes/<string:id>', methods=['DELETE'])
def eliminar_estudiante(id):
    datos_salida = _controlador_estudiante.eliminar_estudiante(id)
    return jsonify(datos_salida)

if __name__ == '__main__':
    datos_configuracion = cargar_configuracion()
    print("servidor ejecutandose...", "http://"+
          datos_configuracion["servidor"]+":"+datos_configuracion["puerto"])

serve(mi_aplicacion,
      host=datos_configuracion["servidor"], port=datos_configuracion["puerto"])
