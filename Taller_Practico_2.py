dcon = {}
duser = {}
dpost = {}
contenidouser = {'user':duser, 'post':dpost, 'comment':dcon}



class Comment:
    id_com = 0
    comentario = ""
    id_post = 0


    '''def __init__(self, id_com, comentario):
        self.id_com = id_com
        self.comentario = comentario'''


    def Crear_Comentario(self):
        self.id_post = input("ingre id post")
        for post in contenidouser['post']:
            if post == self.id_post:
                self.id_com = input("ingrese su id de comentario: ")
                self.comentario = input("ingrese su comentario: ")
                dcon[self.id_com] = {self.id_post:self.comentario}
            else:
                print("El post no existe")



class Post(Comment):
    id_post = 0
    titulo = ""
    id_user = 0

    '''def __init__(self, id_com, comentario, id_post, titulo):
        Comment.__init__(self, id_com, comentario)
        self.id_post = id_post
        self.titulo = titulo'''


    def Crear_Post(self):
        self.id_user = input("ingrese su id de usuario: ")
        for us in contenidouser['user']:
            if us == self.id_user:
                self.id_post = input("ingrese su id de post:")
                self.titulo = input("ingrese su titulo de post:")

                dpost[self.id_post] = {self.id_user : self.titulo}

            else:
                print("el usuario no existe: ")


class User(Post):
    id_user = 0
    nombre = ""

    '''def __init__(self, id_user, nombre):
        self.id_user = id_user
        self.nombre = nombre'''

    def Crear_User(self):

        self.id_user = input("ingrese su identificacion: ")
        self.nombre = input("ingrese su nombre: ")

        duser[self.id_user] = self.nombre


print("Menu de opciones")
print("1. crear usuario")
print("2. crear post")
print("3. crear comentario")
print("4. buscar")

opc =int(input("Digite la opcion: "))

while opc != 5:

    usuario = User()
    if opc == 1:
        usuario.Crear_User()

    elif opc == 2:

        usuario.Crear_Post()
    elif opc == 3:
        usuario.Crear_Comentario()
    elif opc == 4:
        print(contenidouser)
    else:

        print("error")

    opc =int(input("Digite la opcion: "))

