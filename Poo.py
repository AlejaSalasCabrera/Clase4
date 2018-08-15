#Clase
class Persona:
    #atributos
    nombre = ""
    edad = 0
    pais = ""

    #Constructor
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
    #Metodos
    def saludar(self):
        print("Hola mi nombre es : {} ".format(self.nombre))

    def despedir(self):
        print("Hasta pronto: {} ".format(self.nombre))

    def comprar(self):
        print("puedo comprar x cosa")

#crear la instancia de una clase
alejandra = Persona("alejandra salas", 25, "colombia")

print(alejandra.nombre)
print(alejandra.edad)
print(alejandra.pais)
alejandra.saludar()
alejandra.comprar()
alejandra.despedir()

#Herencia Simple
class Estudiante(Persona):
    colegio = ""

    def __init__(self, nombre, edad, pais, colegio):
        Persona.__init__(self, nombre, edad, pais)
        self.colegio = colegio

    def get_colegio(self):
        print("su colegio es: {}".format(self.colegio))

Aleja = Estudiante('gloria', 25 , 'colombia', 'carlos pizarro')

Aleja.saludar()
Aleja.comprar()
Aleja.despedir()
Aleja.get_colegio()

#Herencia Multiple

class Universidad(Estudiante):
    programa = ""

    def __init__(self, nombre, edad, pais, colegio, programa):
        #inanciar la clase de la que Hereda
        Estudiante.__init__(self, nombre, edad, pais, colegio)
        self.programa = programa

    def get_programa(self):
        print("su programa es : {}".format(self.programa))

cesmag = Universidad('carlos',41 , 'italia', 'inem', 'ing sistemas')
cesmag.saludar()
cesmag.comprar()
cesmag.despedir()
cesmag.get_colegio()
cesmag.get_programa()



class Cargo:
    cargo = ""

    def __init__(self, cargo):
        self.cargo = cargo

    def get_cargo(self):
        print("su cargo es: {}".format(self.cargo))

class Trabajador(Persona, Cargo):
    sueldo = 0

    def __init__(self, nombre, edad, pais, cargo, sueldo):
        Persona.__init__(self, nombre, edad, pais)
        Cargo.__init__(self, cargo)
        self.sueldo = sueldo

    def get_sueldo(self):
        print("su salirio es de: {}".format(self.sueldo))

diana = Trabajador('Diana', 42, 'brasil', 'arquitecta', 1000000)
diana.saludar()
diana.comprar()
diana.despedir()
diana.get_cargo()
diana.get_sueldo()



