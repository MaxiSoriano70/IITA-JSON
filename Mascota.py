import json

class BaseDeDatosMascotas:
    def __init__(self,nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def crear_base_de_datos(self):
        mascotas_data = [
            {
                "nombre": "Margo",
                "especie": "Perro",
                "color": "Marron",
                "edad": 3,
                "peso": 15,
                "altura": 0.5
            },
            {
                "nombre": "Luna",
                "especie": "Gato",
                "color": "Negro",
                "edad": 2,
                "peso": 5,
                "altura": 0.3
            },
            {
                "nombre": "Charlie",
                "especie": "Perro",
                "color": "Blanco",
                "edad": 5,
                "peso": 20,
                "altura": 0.6
            },
            {
                "nombre": "Whiskers",
                "especie": "Gato",
                "color": "Gris",
                "edad": 1,
                "peso": 4,
                "altura": 0.25
            },
            {
                "nombre": "Buddy",
                "especie": "Perro",
                "color": "Dorado",
                "edad": 4,
                "peso": 18,
                "altura": 0.55
            }
        ]
        with open(self.nombreArchivo, "w") as archivo:
            json.dump(mascotas_data, archivo, indent=4)
        print(f"Se ha guardado el archivo '{self.nombreArchivo}'.")

    def get_mascotas(self):
        with open(self.nombreArchivo, "r") as archivo:
            mascotas_data = json.load(archivo)
        print("===========================")
        print("===========================TODAS LAS MASCOTAS===========================")
        for mascota in mascotas_data:
            print("Datos de la mascota:")
            print(f"Nombre: {mascota['nombre']}")
            print(f"Especie: {mascota['especie']}")
            print(f"Color: {mascota['color']}")
            print(f"Edad: {mascota['edad']} años")
            print(f"Peso: {mascota['peso']} kg")
            print(f"Altura: {mascota['altura']} metros")
            print("===========================")

    def get_mascota(self, nombreMascota):
        with open(self.nombreArchivo, "r") as archivo:
            mascotas_data = json.load(archivo)
        print("============UNA MASCOTA===============")
        bandera = False
        for mascota in mascotas_data:
            if mascota['nombre'] == nombreMascota:
                print("Datos de la mascota:")
                print(f"Nombre: {mascota['nombre']}")
                print(f"Especie: {mascota['especie']}")
                print(f"Color: {mascota['color']}")
                print(f"Edad: {mascota['edad']} años")
                print(f"Peso: {mascota['peso']} kg")
                print(f"Altura: {mascota['altura']} metros")
                bandera = True
        if(bandera == False):
            print(F"La mascota con el nombre {nombreMascota} no existe.")
        print("===========================")

    def agregar_mascota(self, nombre, especie, color, edad, peso, altura):
        nueva_mascota = {
            "nombre": nombre,
            "especie": especie,
            "color": color,
            "edad": edad,
            "peso": peso,
            "altura": altura
        }

        print("============AGREGAR UNA MASCOTA===============")
        with open(self.nombreArchivo, "r+") as archivo:
            mascotas_data = json.load(archivo)
            #Agrega la nueva mascota
            mascotas_data.append(nueva_mascota)

            #Volver al principio del archivo para escribir los cambios
            archivo.seek(0)

            #Escribir la lista actualizada de mascotas en el archivo JSON
            json.dump(mascotas_data, archivo, indent=4)
            print(f"Se ha agregado la mascota {nombre} al archivo '{self.nombreArchivo}'.")
        print("===========================")



    def update_mascota(self, nombre, especie, color, edad, peso, altura):
        with open(self.nombreArchivo, "r") as archivo:
            mascotas_data = json.load(archivo)
        print("============UPDATE UNA MASCOTA===============")
        bandera = False
        for mascota in mascotas_data:
            if mascota['nombre'] == nombre:
                mascota['especie'] = especie
                mascota['color'] = color
                mascota['edad'] = edad
                mascota['peso'] = peso
                mascota['altura'] = altura
                print(f"Datos de la {mascota['nombre']} actualizados con exito!")
                bandera = True
        if(bandera == False):
            print(F"La mascota con el nombre {nombre} no existe.")
        else:
            with open(self.nombreArchivo, "w") as archivo:
                    json.dump(mascotas_data, archivo, indent=4)
        print("===========================")

    def eliminar_mascota(self, nombre):
        with open(self.nombreArchivo, "r+") as archivo:
            mascotas_data = json.load(archivo)

            mascotas_actualizadas = []
            bandera = False
            for mascota in mascotas_data:
                if mascota['nombre'] != nombre:
                    mascotas_actualizadas.append(mascota)
                else:
                    bandera = True

            if bandera == True:
                archivo.seek(0)  # Volver al principio del archivo
                archivo.truncate()  # Limpiar el contenido existente del archivo
                json.dump(mascotas_actualizadas, archivo, indent=4)  # Escribir la lista actualizada de mascotas
                print(f"Se ha eliminado la mascota {nombre} del archivo '{self.nombreArchivo}'.")
            else:
                print(f"No se encontró la mascota con el nombre {nombre} en el archivo '{self.nombreArchivo}'.")

baseDeDatosMascotas = BaseDeDatosMascotas("mascotasDB.json")

baseDeDatosMascotas.crear_base_de_datos()

baseDeDatosMascotas.get_mascota("Luna")

baseDeDatosMascotas.get_mascota("Lu")

baseDeDatosMascotas.agregar_mascota("Roco", "Perro", "Negro", 5 ,25.5 , 0.60)

baseDeDatosMascotas.get_mascotas()

baseDeDatosMascotas.update_mascota("Luna", "Conejo", "Blanco", 2, 1.5, 0.25)

baseDeDatosMascotas.eliminar_mascota("Lu")

baseDeDatosMascotas.eliminar_mascota("Buddy")

baseDeDatosMascotas.get_mascotas()