class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        #El signo "=" es asignación,
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")
    
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa if self.fuerza > enemigo.defensa else 0
        
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if not enemigo.esta_vivo():
            enemigo.morir()

        print("Vida de", enemigo.nombre, "es", enemigo.vida)
        
#Creando clase "Guerrero" que hereda de la clase padre "Personaje"
class Guerrero(Personaje):
    #Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        #Llamar a la clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        
#Pedirle al usuario escoger un arma
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1)Espada de plata, daño 10. (2) Espada de bronce, daño 8"))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 8
        else:
            print("Valor incorrecto")
    
    #Sobrescribir método
    def atributos(self):
        super().atributos()
        print("-Espada:",self.espada)
    
    #Sobrescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

#Creando clase "Mago" que hereda de la clase padre "Personaje"   
class Mago(Personaje):
    #Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        #Llamar a la clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
        
    #Sobrescribir método
    def atributos(self):
        super().atributos()
        print("-Libro:",self.libro)
    
    #Sobrescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

trakalosa = Personaje("La trakalosa de Monterrey", 20, 15, 10, 100)
hercules = Guerrero("Hércules", 20, 15, 10, 100, 5)
diosito = Mago("Diosito", 20, 15, 10, 100, 5)
#Imprimir atributos antes del ataque
trakalosa.atributos()
hercules.atributos()
diosito.atributos()
#Ataques
trakalosa.atacar(hercules)
hercules.atacar(diosito)
diosito.atacar(trakalosa)
#Imprimir atributos después del ataque
trakalosa.atributos()
hercules.atributos()
diosito.atributos()