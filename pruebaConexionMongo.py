import pymongo
import certifi
from  bson.objectid import ObjectId

ca = certifi.where()

client = pymongo.MongoClient(
    "mongodb+srv://lmadrigalo:poison@ciclo4.oddcq5g.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = ca)
db = client["app-academico"]

print(db.list_collection_names())

#CRUD ESTUDIANTES - INSCRIPCION

_estudiante_coleccion = db.estudiante
_inscripcion_coleccion = db.inscripcion

print(_estudiante_coleccion.find)

#insert - estudiante
_estudiante = {
    "nombre":"Naty",
    "apellido":"Granada"
}

_estudiante_id = _estudiante_coleccion.insert_one(_estudiante).inserted_id
print("se ha creado el estudiante con codigo",_estudiante_id)


_inscripcion = {
  "estudiante_id": str(_estudiante_id),
  "fecha": "202-08-20"
}

_inscripcion_id = _inscripcion_coleccion.insert_one(_inscripcion).inserted_id
print("se ha creado una inscripcion con codigo ",_inscripcion_id)

#read - estudiantes

print(_estudiante_coleccion.find_one())

for estudiante in _estudiante_coleccion.find():
  print(estudiante["nombre"])

#update - estudiante  
consulta = {"_id":ObjectId('6350a727f8e856ff445107ab')}
actualizacion = {"$set":{"nombre":"DIEGO","apellido":"CASTILLO"}}
_estudiante_coleccion.update_one(consulta,actualizacion)

#delete - estudiante  
consulta2 = {"_id":ObjectId('6350b721f4fccdca0cdb0083')}
_estudiante_coleccion.delete_one(consulta2)