import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema...")
        
        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos? ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()

        if registro[0] >=1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")

        else:
            print("\nNo te has registrado correctamente")
  
    def login(self):
        print("\nVale!! Identificate en el sistema...")
        
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('','',email,password)

            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto !!! Intentalo más tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones Disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)
        
        accion = input("¿Qué quieres hacer?: ")

        hazel = notas.acciones.Acciones()

        if accion == "crear":
            hazel.crear(usuario)
            print("Vamos a crear")
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazel.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            hazel.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"ok {usuario[1]}, hasta pronto")
            exit()
        return None