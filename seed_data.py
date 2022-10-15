from ejemplo.models import Familiar

Familiar(nombre="Josefina", direccion="Alvear 123", numero_pasaporte=123123).save()
Familiar(nombre="Juliana", direccion="Alvear 123", numero_pasaporte=456456).save()
Familiar(nombre="Juana", direccion="Alvear 123", numero_pasaporte=789789).save()
Familiar(nombre="Jeronimo", direccion="Alvear 123", numero_pasaporte=123456).save()

print("Se cargo con éxito los usuarios de pruebas")