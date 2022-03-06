#!/usr/bin/python3
"""Modulo de pruebas para la clase BaseModel"""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import inspect
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """
    """

    @classmethod
    def test_setUp(self):
        """Configurar para pruebas de cadenas de documentos"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_instancia(self):
        """Prueba la instanciación de la clase BaseModel"""
        b = BaseModel()
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_restablece(self):
        """Restablece los datos de FileStorage."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_init_sin_argumentos(self):
        """Prueba __init__ sin argumentos."""
        self.test_restablece()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        mensaje = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), mensaje)

    def test_init_varios_argumentos(self):
        """Tests __init__ con varios argumentos."""
        self.test_restablece()
        args = [iterador for iterador in range(1000)]
        base = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        base = BaseModel(*args)

    def test_momento_creacion(self):
        """Prueba si updated_at y created_at están
        actualizados en el momento de la creación."""
        dato = datetime.now()
        base = BaseModel()
        diff = base.updated_at - base.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = base.created_at - dato
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_id(self):
        """Pruebas para identificaciones de usuario únicas."""

        ld = [BaseModel().id for iterador in range(1000)]
        self.assertEqual(len(set(ld)), len(ld))

    def test_save(self):
        """Prueba el método de instancia pública save()."""

        base = BaseModel()
        time.sleep(0.5)
        tiempo = datetime.now()
        base.save()
        diff = base.updated_at - tiempo
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        """Pruebas para el método __str__."""
        base = BaseModel()
        signos = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        aparacion = signos.match(str(base))
        self.assertIsNotNone(aparacion)
        self.assertEqual(aparacion.group(1), "BaseModel")
        self.assertEqual(aparacion.group(2), base.id)
        subgru = aparacion.group(3)
        subgru = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", subgru)
        jso = json.loads(subgru.replace("'", '"'))
        copia = base.__dict__.copy()
        copia["created_at"] = repr(copia["created_at"])
        copia["updated_at"] = repr(copia["updated_at"])
        self.assertEqual(jso, copia)

    def test_to_dict(self):
        """Prueba el método de instancia pública to_dict()."""

        base = BaseModel()
        base.name = "Sebastian"
        base.age = 35
        diccio = base.to_dict()
        self.assertEqual(diccio["id"], base.id)
        self.assertEqual(diccio["__class__"], type(base).__name__)
        self.assertEqual(diccio["created_at"], base.created_at.isoformat())
        self.assertEqual(diccio["updated_at"], base.updated_at.isoformat())
        self.assertEqual(diccio["name"], base.name)
        self.assertEqual(diccio["age"], base.age)

    def test_to_dict_sin_argumentos(self):
        """Prueba to_dict() sin argumentos."""
        self.test_restablece()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        mensaje = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), mensaje)

    def test_to_dict_varios_argumentos(self):
        """Prueba to_dict() con varios argumentos."""
        self.test_restablece()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_instanciacion(self):
        """Prueba la creación de instancias con **kwargs"""

        base = BaseModel()
        base.name = "Sebastian"
        base.my_number = 21
        base_json = base.to_dict()
        model = BaseModel(**base_json)
        self.assertEqual(model.to_dict(), base.to_dict())

    def test_instantiation_dict(self):
        """Prueba la creación de instancias con **kwargs del dictado
        personalizado."""
        diccionario = {
            "__class__": "BaseModel",
            "updated_at": datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
            "created_at": datetime.now().isoformat(),
            "id": uuid.uuid4(),
            "my_first_name": "Sebastian",
            "my_number": 21,
        }
        obj = BaseModel(**diccionario)
        self.assertEqual(obj.to_dict(), diccionario)

    def test_save_desde_save(self):
        """Prueba que llama a storage.save() desde save()."""
        self.test_restablece()
        base = BaseModel()
        base.save()
        key = "{}.{}".format(type(base).__name__, base.id)
        llave = {key: base.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(llave)))
            f.seek(0)
            self.assertEqual(json.load(f), llave)

    def test_save_sin_argumentos(self):
        """Prueba save() sin argumentos"""
        self.test_restablece()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        mensaje = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), mensaje)

    def test_save_varios_argumentos(self):
        """Prueba save() con demasiados argumentos."""
        self.test_restablece()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        mensaje = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), mensaje)


if __name__ == "__main__":
    unittest.main()
