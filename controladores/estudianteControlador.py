from modelos.estudianteModelo import EstudianteModelo

class EstudianteControlador():
    def __init__(self):
        pass

    def listar_estudiante(self):
        datos_estudiante = {
            "id":"1",
            "nombre":"jhon",
            "apellido":"mendez"
        }

        return datos_estudiante

    def crear_estudiante(self,datos_entrada):
        _estudiante = EstudianteModelo(datos_entrada)
        return _estudiante.__dict__

    def eliminar_estudiante(self,id):
        respuesta = {
            "respuesta": "usuario con codigo" + " " + id + " " + "eliminado"
        }
        return respuesta

    def actualizar_estudiante(self, id, datos_entrada):
        print("Actualizando el estudiante con id",id)
        elEstudiante = EstudianteModelo(datos_entrada)
        print("Se ha creado un objeto", " ", elEstudiante)
        return elEstudiante.__dict__