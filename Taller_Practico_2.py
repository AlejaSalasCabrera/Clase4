class Comment:
    id_com = 0
    comentario = ""
    fecha_com = ""

    def __init__(self, id_com, comentario, fecha_com):
        self.id_com = id_com
        self.comentario = comentario
        self.fecha_com = fecha_com

    def Crear_Comentario(self):
        self.id_com = input("ingrese su id de comentario:")
        self.comentario = input("ingrese su comentario:")
        self.fecha_com = input("ingrese la fech de publicain:")

class Post(Comment):
    id_post = 0
    titulo = ""
    fecha_post = ""

    def __init__(self, id_com, comentario, fecha_com, id_post, titulo, fecha_post):
        Comment.__init__(self, id_com, comentario, fecha_com)
        self.id_post = id_post
        self.titulo = titulo
        self.fecha_post = fecha_post

    def Crear_Post(self):
        self.id_post = input("ingrese su id de post:")
        self.titulo = input("ingrese su titulo de post:")
        self.fecha_post = input("ingrese su fecha de publicacion de post: ")


class User(Post):
    id_user = 0
    nombre = ""
    contraseña = ""

    def __init__(self, id_user, nombre, contraseña):
        self.id_user = id_user
        self.nombre = nombre
        self.contraseña = contraseña

    def Crear_User(self):

        self.id_user = input("ingrese su identificacion: ")
        self.nombre = input("ingrese su nombre: ")
        self.contraseña = input("ingrese su contraseña: ")

