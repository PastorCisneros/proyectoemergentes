from pyknow import *

class animales(KnowledgeEngine):

    @Rule(Fact(falla = 'falla' << L("falla")))
    def a_1 (self, animal):
        print(".: SISTEMA EXPERTO DE FALLAS DE TRANSPORTE :.")
        print(" ")
        self.declare(Fact(falla = "falla", automovil = input("¿Es un automovil? (s/n): ")))
#AUTOMOVIL
    @Rule(Fact(falla = L("falla"), automovil = L("s")))
    def a_11(self):
        print("Es un automovil")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = input("¿Es automatico? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("s")))
    def a_111(self):
        print("Es un automovil y es automatico")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "s", modoestandar = input("¿Tiene modo estandar? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("s"), modoestandar = L("s")))
    def a_1111(self):
        print("Es una automovil automatico con modo estandar")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "s", modoestandar = "s", manejarestandar = input("¿Sabes manejar tipo estandar? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("s"), modoestandar = L("s"), manejarestandar = L("s")))
    def a_1112(self):
        print("ESCOJE TU MODO")
        self.declare(Fact(falla = "modo estandar", automovil = "s", automatico = "s", modoestandar = "s",manejarestandar ='s'))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("s"), modoestandar = L("s"), manejarestandar = L("n")))
    def a_112(self):
        print("CAMBIA AUTOMATICO")
        self.declare(Fact(falla = "cambio automatico", automovil = "s", automatico = "s", modoestandar = "s",manejarestandar ='n'))
################################################################3
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n")))
    def a_1121(self):
        print("Es un automovil estandar")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = input("¿Sabes manejar? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s")))
    def a_1122(self):
        print("Es una automovil estandar y no sabe manejar")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = ("s"), licencia = input("¿Tienes Licencia? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("n")))
    def a_11222(self):
        print("SACAR LICENCIA")
        self.declare(Fact(falla = "sacar licencia", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("n"), sacarlicencia = input("¿ Sacaras tu Licencia? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("n"),sacarlicencia = L("s")))
    def a_11221(self):
        print("OBTENER CITA")
        self.declare(Fact(falla = "obtener cita", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("n"), sacarlicencia = ("s")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("n"),sacarlicencia = L("s")))
    def a_11221(self):
        print("OBTENER MULTA")
         self.declare(Fact(falla = "obtener cita", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("n"), sacarlicencia = ("n")))

    @Rule(Fact(animal = L("animal"), extinto = L("s"), colmillos = L("n"), ave = L("n"), gigante = L("s"), cuernos = L("n")))
    def a_112212(self):
        print("El animal que busca es un T-REX")
        self.declare(Fact(animal = "trex", extinto = "s", colmillos = "n", ave = "n", gigante = "s", cuernos = "n"))
#NO EXTINTOS
    @Rule(Fact(animal = L("animal"), extinto = L("n")))
    def a_12(self):
        print("No es un animal extinto")
        self.declare(Fact(animal = "animal", extinto = "n", marino = input("¿Es un animal marino? (s/n): ")))
#MARINOS
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s")))
    def a_121(self):
        print("Es un animal marino")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = input("¿Es un molusco de ocho brazos? (s/n): ")))
#->MOLUSCOS
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("s")))
    def a_1211(self):
        print("Es un animal marino, molusco de ocho brazos")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "s", rot = input("¿La cabeza es redonda o triangular? (r/t): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("s"), rot = L("r")))
    def a_12111(self):
        print("El animal que busca es un PULPO")
        self.declare(Fact(animal = "pulpo", extinto = "n", marino = "s", molusco = "s", rot = "r"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("s"), rot = L("t")))
    def a_12112(self):
        print("El animal que busca es un CALAMAR")
        self.declare(Fact(animal = "calamar", extinto = "n", marino = "s", molusco = "s", rot = "t"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n")))
    def a_1212(self):
        print("Es un animal marino, pero no es un molusco")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = input("¿Es un crustaceo? (s/n): ")))
#->CRUSTACEOS
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("s")))
    def a_12121(self):
        print("Es un animal marino y crustaceo")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "s", tenazas = input("¿Tiene tenazas? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo =L("s"), tenazas = L("n")))
    def a_121212(self):
        print("El animal que buca es un CAMARON")
        self.declare(Fact(animal = "camaron", extinto = "n", marino = "s", molusco = "n", crustaceo = "s", tenazas = "n"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo =L("s"), tenazas = L("s")))
    def a_121211(self):
        print("Es un crustaceo con tenazas")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "s", tenazas = "s", grande = input("¿Es un crustaceo con tenazas grande? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("s"), tenazas = L("s"), grande = L("s")))
    def a_1212111(self):
        print("El animal que busca es una LANGOSTA")
        self.declare(Fact(animal = "langosta", extinto = "n", marino = "s", molusco = "n", crustaceo = "s", tenazas = "s", grande = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("s"), tenazas = L("s"), grande = L("n")))
    def a_1212112(self):
        print("Es un crustaceo con tenazas y no es grande")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "s", tenazas = "s", grande = "n", dos = input("¿su habitat es en agua dulce o salada? (d/s): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("s"), tenazas = L("s"), grande = L("n"), dos = L("d")))
    def a_12121121(self):
        print("El animal que busca es una JAIBA")
        self.declare(Fact(animal = "jaiba", extinto = "n", marino = "s", molusco = "n", crustaceo = "s", tenazas = "s", grande = "n", dos = "d"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("s"), tenazas = L("s"), grande = L("n"), dos = L("s")))
    def a_121211212(self):
        print("El animal que busca es un CANGREJO")
        self.declare(Fact(animal = "cangrejo", extinto = "n", marino = "s", molusco = "n", crustaceo = "s", tenazas = "s", grande = "n", dos = "s"))
#NO CRUSTACEO
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n")))
    def a_12122(self):
        print("Es un animal marino, pero no es crustaceo")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = input("¿Es un pez o un mamifero? (p/m): ")))
#->PEZ
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p")))
    def a_121221(self):
        print("Es un animal marino y es un pez")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = input("¿Es un pez grande? (s/n): ")))
#->PEZ GRANDE
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("s")))
    def a_1212211(self):
        print("Es un pez grande")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "s", tiburon = input("¿Es una especie de tiburon? (s/n): ")))
    
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("s"), tiburon = L("s")))
    def a_12122111(self):
        print("Es una especie de tiburon")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "s", tiburon = "s", atacan = input("¿El animal ataca para alimentarse? (s/n): ")))
    
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("s"), tiburon = L("n")))
    def a_12122112(self):
        print("El animal que busca es una MANTARAYA")
        self.declare(Fact(animal = "mantaraya", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "s", tiburon = "n"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("s"), tiburon = L("s"), atacan = L("s")))
    def a_121221111(self):
        print("El animal que busca es un TIBURON BLANCO")
        self.declare(Fact(animal = "tibblanco", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "s", tiburon = "s", atacan = "s"))
    
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("s"), tiburon = L("s"), atacan = L("n")))
    def a_121221112(self):
        print("El animal que busca es un TIBURON BALLENA")
        self.declare(Fact(animal = "tibballena", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "s", tiburon = "s", atacan = "n"))
#->PEZ NO GRANDE    
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n")))
    def a_1212212(self):
        print("Es un pez, pero no es grande")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = input("¿Se vende como comida enlatada? (s/n): ")))
#->->ENLATADA
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("s")))
    def a_12122121(self):
        print("Es un pez que se vende en comida enlatada")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "s", grandee = input("¿Es grande? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("s"), grandee = L("s")))
    def a_121221211(self):
        print("El animal que busca es un ATUN")
        self.declare(Fact(animal = "atun", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "s", grandee = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("s"), grandee = L("n")))
    def a_121221212(self):
        print("No es un pez grande y se vende enlatado")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "s", grandee = "n", long = input("¿Tiene menos de 30cm de longitud? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("s"), grandee = L("n"), long = L("s")))
    def a_1212212121(self):
        print("El animal que busca es una SARDINA")
        self.declare(Fact(animal = "sardina", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "s", grandee = "n", long = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("s"), grandee = L("n"), long = L("n")))
    def a_1212212122(self):
        print("Es un pez que se vende enlatado y mayor a 30cm de longitud")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "s", grandee = "n", long = "n", aletas = input("¿Tiene aletas cortas o largas? (c/l): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("s"), grandee = L("n"), long = L("n"), aletas = L("c")))
    def a_12122121221(self):
        print("El animal que busca es una TRUCHA")
        self.declare(Fact(animal = "trucha", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "s", grandee = "n", long = "n", aletas = "c"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("s"), grandee = L("n"), long = L("n"), aletas = L("l")))
    def a_12122121222(self):
        print("El animal que busca es un SALMON")
        self.declare(Fact(animal = "salmon", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "s", grandee = "n", long = "n", aletas = "l"))
#->->NO ENLATADA
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("n")))
    def a_12122122(self):
        print("Es un pez y no se vende como enlatado")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "n", foa = input("¿Su nombre se relaciona con una fiesta o con un arma? (f/a): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("n"), foa = L("f")))
    def a_121221221(self):
        print("Es un pez y su nombre se relaciona a una fiesta")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "n", foa = "f", infla = input("¿Se infla? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("n"), foa = L("f"), infla = L("s")))
    def a_1212212211(self):
        print("El animal que busca es un PEZ GLOBO")
        self.declare(Fact(animal = "pezglobo", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "n", foa = "f", infla = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("n"), foa = L("f"), infla = L("n")))
    def a_1212212212(self):
        print("El animal que busca es un PEZ PAYASO")
        self.declare(Fact(animal = "pezpayaso", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "n", foa = "f", infla = "n"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("n"), foa = L("a")))
    def a_121221222(self):
        print("Es un pez y su nombre se relaciona a una arma")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "n", foa = "a", boca = input("¿Su boca es muy picuda y fina? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("n"), foa = L("a"), boca = L("s")))
    def a_1212212221(self):
        print("El animal que busca es un PEZ ESPADA")
        self.declare(Fact(animal = "pezespada", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "n", foa = "a", boca = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("p"), grande = L("n"), enlatado = L("n"), foa = L("a"), boca = L("n")))
    def a_1212212222(self):
        print("El animal que busca es un PEZ SIERRA")
        self.declare(Fact(animal = "pezsierra", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "p", grande = "n", enlatado = "n", foa = "a", boca = "n"))
#MAMIFEROS MARINOS
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("m")))
    def a_121222(self):
        print("Es un animal marino y es mamifero")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "m", gigante = input("¿Es gigante? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom= L("m"), gigante = L("s")))
    def a_1212221(self):
        print("El animal que busca es una BALLENA")
        self.declare(Fact(animal = "ballena", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "m", gigante = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom = L("m"), gigante = L("n")))
    def a_1212222(self):
        print("Es un animal marino mamifero, pero no es gigante")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "m", gigante = "n", color = input("¿Es blanco y negro? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom = L("m"), gigante = L("n"), color =("s")))
    def a_12122221(self):
        print("El animal que busca es una ORCA")
        self.declare(Fact(animal = "orca", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "m", gigante = "n", color = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom = L("m"), gigante = L("n"), color =("n")))
    def a_12122222(self):
        print("Es un animal marino mamifero, pero no es blanco y negro")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "m", gigante = "n", color = "n", inteligente = input("¿Se considera un animal bastante inteligente? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom = L("m"), gigante = L("n"), color =("n"), inteligente = L("s")))
    def a_121222221(self):
        print("El animal que busca es un DELFIN")
        self.declare(Fact(animal = "delfin", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "m", gigante = "n", color = "n", inteligente = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom = L("m"), gigante = L("n"), color =("n"), inteligente = L("n")))
    def a_121222222(self):
        print("Es un animal marino mamifero, pero no se considera tan inteligente")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "m", gigante = "n", color = "n", inteligente ="n", colmillos = input("¿Tiene colmillos? (s/n): ")))
    
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom = L("m"), gigante = L("n"), color =("n"), inteligente = L("n"), colmillos = L("s")))
    def a_1212222221(self):
        print("El animal que busca es una MORSA")
        self.declare(Fact(animal = "morsa", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "m", gigante = "n", color = "n", inteligente ="n", colmillos = "s"))
    
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("s"), molusco = L("n"), crustaceo = L("n"), pom = L("m"), gigante = L("n"), color =("n"), inteligente = L("n"), colmillos = L("n")))
    def a_1212222222(self):
        print("El animal que busca es una FOCA")
        self.declare(Fact(animal = "foca", extinto = "n", marino = "s", molusco = "n", crustaceo = "n", pom = "m", gigante = "n", color = "n", inteligente ="n", colmillos = "n"))
#NO MARINOS
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n")))
    def a_122(self):
        print("No es un animal marino")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = input("¿Tiene plumas y pico? (s/n): ")))
#AVES
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s")))
    def a_1221(self):
        print("Es un ave")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "s", garras = input("¿Posee pico afilado y patas con grandes garras? (s/n): ")))
#GARRAS
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("s")))
    def a_12211(self):
        print("Es un ave con pico afilado y patas con grandes garras")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "s", garras = "s", valto = input("¿Vuela a grandes alturas? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("s"), valto = L("s")))
    def a_122111(self):
        print("Es un ave con pico afilado, patas con grandes garras y vuela a grandes alturas")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "s", garras = "s", valto = "s", cola = input("¿Tiene una cola esbelta? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("s"), valto = L("s"), cola = L("s")))
    def a_1221111(self):
        print("El animal que busca es un HALCON")
        self.declare(Fact(animal = "halcon", extinto = "n", marino = "n", ave = "s", garras = "s", valto = "s", cola = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("s"), valto = L("s"), cola = L("n")))
    def a_1221112(self):
        print("El animal que busca es una AGUILA ")
        self.declare(Fact(animal = "aguila", extinto = "n", marino = "n", ave = "s", garras = "s", valto = "s", cola = "n"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("s"), valto = L("n")))
    def a_122112(self):
        print("Es un ave con pico afilado y patas con grandes garras pero no vuela tan alto")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "s", garras = "s", valto = "n", plumas = input("¿Posee plumas alzadas en la cabeza? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("s"), valto = L("n"), plumas = L("s")))
    def a_1221121(self):
        print("El animal que busca es un BUHO")
        self.declare(Fact(animal = "buho", extinto = "n", marino = "n", ave = "s", garras = "s", valto = "n", plumas = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("s"), valto = L("n"), plumas = L("n")))
    def a_1221122(self):
        print("El animal que busca es una LECHUZA ")
        self.declare(Fact(animal = "lechuza", extinto = "n", marino = "n", ave = "s", garras = "s", valto = "n", plumas = "n"))
#NO GARRAS
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n")))
    def a_12212(self):
        print("No es un ave con pico afilado ni con grandes garras")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "s", garras = "n", pico = input("¿Tiene el pico aplanado? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("s")))
    def a_122121(self):
        print("Es un ave con pico aplanado")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "s", cuello = input("¿Posee el cuello demasiaod largo? (s/n): ")))
 
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("s"), cuello = L("s")))
    def a_1221211(self):
        print("El animal que busca es un CISNE")
        self.declare(Fact(animal = "cisne", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "s", cuello ="s"))
 
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("s"), cuello = L("n")))
    def a_1221212(self):
        print("No tiene el cuello demasiado largo")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "s", cuello = "n", color = input("¿Puede llegar a ser amarillo? (s/n): ")))
 
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("s"), cuello = L("n"), color = L("s")))
    def a_12212121(self):
        print("El animal que busca es un PATO")
        self.declare(Fact(animal = "pato", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "s", cuello = "n", color = "s"))
 
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("s"), cuello = L("n"), color = L("n")))
    def a_12212122(self):
        print("El animal que busca es un GANSO")
        self.declare(Fact(animal = "pato", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "s", cuello = "n", color = "n"))
#NO pico aplanado
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("n")))
    def a_122122(self):
        print("Es un ave y no tiene el pico aplanado")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "n", tamano = input("¿Es grande o pequeño? (g/p): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("n"), tamano = L("g")))
    def a_1221221(self):
        print("Es un ave corredora")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "n", tamano = "g", tod = input("¿Posee tres o dos dedos en las patas? (t/d): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("n"), tamano = L("g"), tod = L("t")))
    def a_12212211(self):
        print("Eel animal que busca es un NANDU")
        self.declare(Fact(animal = "nandu", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "n", tamano = "g", tod = "t"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("n"), tamano = L("g"), tod = L("d")))
    def a_12212212(self):
        print("Eel animal que busca es un AVESTRUZ")
        self.declare(Fact(animal = "avestruz", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "n", tamano = "g", tod = "d"))
    
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("n"), tamano = L("p")))
    def a_1221222(self):
        print("Es un ave pequeña")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "n", tamano = "p", picol = input("¿Tiene un pico largo para succionar? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("n"), tamano = L("p"), picol = L("s")))
    def a_12212221(self):
        print("El animal que busca es un COLIBRI")
        self.declare(Fact(animal = "colibri", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "n", tamano = "p", picol = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("n"), tamano = L("p"), picol = L("n")))
    def a_12212222(self):
        print("Es un pajaron pequeño pero no tiene pico largo")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "n", tamano = "p", picol = "n", color = input("¿Es colorido? (s/n): ")))
    
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("n"), tamano = L("p"), picol = L("n"), color = L("s")))
    def a_122122221(self):
        print("El animal que busca es un PAJARO CARBONERO")
        self.declare(Fact(animal = "carbonero", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "n", tamano = "p", picol = "n", color = "s"))
    
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("s"), garras = L("n"), pico = L("n"), tamano = L("p"), picol = L("n"), color = L("n")))
    def a_122122222(self):
        print("El animal que busca es un PAJARO GORRION")
        self.declare(Fact(animal = "gorrion", extinto = "n", marino = "n", ave = "s", garras = "n", pico = "n", tamano = "p", picol = "n", color = "n"))
 #NO AVES   
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n")))
    def a_1222(self):
        print("No es un ave")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = input("¿Anda, nada y repta? (s/n): ")))
#REPTILES
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s")))
    def a_12221(self):
        print("Es un reptil")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = input("¿Posee un caparazon? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("s")))
    def a_122211(self):
        print("El animal que busca es una TORTUGA")
        self.declare(Fact(animal = "tortuga", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n")))
    def a_122212(self):
        print("El reptil no tiene caparazon")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = input("¿Tiene patas? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("s")))
    def a_1222121(self):
        print("El reptil tiene patas")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "s", grande = input("¿Es grande? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("s"), grande = L("s")))
    def a_12221211(self):
        print("El reptil tiene patas y es grande")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "s", grande = "s", uov = input("¿Tiene el hocico en forma de U o de V? (u/v): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("s"), grande = L("s"), uov = L("u")))
    def a_122212111(self):
        print("El animal que busca es un CAIMAN")
        self.declare(Fact(animal = "caiman", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "s", grande = "s", uov = "u"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("s"), grande = L("s"), uov = L("v")))
    def a_122212112(self):
        print("El animal que busca es un COCODRILO")
        self.declare(Fact(animal = "cocodrilo", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "s", grande = "s", uov = "v"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("s"), grande = L("n")))
    def a_12221212(self):
        print("El reptil tiene patas, pero no es grande")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "s", grande = "n", camu = input("¿Puede camuflajearse facilmente y enrollar la cola? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("s"), grande = L("n"), camu = L("s")))
    def a_122212121(self):
        print("El animal que busca es un CAMALEON")
        self.declare(Fact(animal = "camaleon", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "s", grande = "n", camu = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("s"), grande = L("n"), camu = L("n")))
    def a_122212122(self):
        print("El animal que busca es una IGUANA")
        self.declare(Fact(animal = "iguana", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "s", grande = "n", camu = "n"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("n")))
    def a_1222122(self):
        print("El reptil no tiene patas, es un tipo de serpiente")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "n", sonido = input("¿Puede emitir sonido con su cola? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("n"), sonido = L("s")))
    def a_12221221(self):
        print("El animal que busca es una VIBORA DE CASCABEL")
        self.declare(Fact(animal = "cascabel", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "n", sonido = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("n"), sonido = L("n")))
    def a_12221222(self):
        print("La serpiente no emite sonidos con la cola")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "n", sonido = "n", levan = input("¿Puede mantenerse levantada? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("n"), sonido = L("n"), levan = L("s")))
    def a_122212221(self):
        print("El animal que busca es una COBRA")
        self.declare(Fact(animal = "cobra", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "n", sonido = "n", levan = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("s"), caparazon = L("n"), patas = L("n"), sonido = L("n"), levan = L("n")))
    def a_122212222(self):
        print("El animal que busca es una BOA")
        self.declare(Fact(animal = "boa", extinto = "n", marino = "n", ave = "n", reptil = "s", caparazon = "n", patas = "n", sonido = "n", levan = "n"))
#NO REPTILES
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n")))
    def a_12222(self):
        print("No es un reptil, pero es un terrestre")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = input("¿Tiene pezuñas? (s/n): ")))
#UNGULADO
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s")))
    def a_122221(self):
        print("Es un animal ungulado")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = input("¿Tiene cuernos? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("s")))
    def a_1222211(self):
        print("Es un animal ungulado y tiene cuernos")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "s", nariz = input("¿Tiene los cuernos en la nariz? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("s"), nariz = L("s")))
    def a_12222111(self):
        print("El animal que busca es un RINOCERONTE")
        self.declare(Fact(animal = "rinoceronte", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "s", nariz = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("s"), nariz = L("n")))
    def a_12222112(self):
        print("El animal tiene cuernos pero no en la nariz")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "s", nariz = "n", ramas = input("¿Sus cuernos parecen ramas? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("s"), nariz = L("n"), ramas = L("s")))
    def a_122221121(self):
        print("El animal que busca es un VENADO")
        self.declare(Fact(animal = "venado", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "s", nariz = "n", ramas = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("s"), nariz = L("n"), ramas = L("n")))
    def a_122221122(self):
        print("El animal que busca es una CABRA")
        self.declare(Fact(animal = "cabra", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "s", nariz = "n", ramas = "n"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("n")))
    def a_1222212(self):
        print("Es un animal ungulado y no tiene cuernos")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "n", lana = input("¿Tiene lana? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("n"), lana = L("s")))
    def a_12222121(self):
        print("Es un animal ungulado y tiene lana")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "n", lana = "s", cuello = input("¿Tiene el cuello largo? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("n"), lana = L("s"), cuello = L("s")))
    def a_122221211(self):
        print("El animal que busca es una LLAMA")
        self.declare(Fact(animal = "llama", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "n", lana = "s", cuello = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("n"), lana = L("s"), cuello = L("n")))
    def a_122221212(self):
        print("El animal que busca es una OVEJA")
        self.declare(Fact(animal = "oveja", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "n", lana = "s", cuello = "n"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("n"), lana = L("n")))
    def a_12222122(self):
        print("Es un animal es ungulado y no tiene lana")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "n", lana = "n", cuello = input("¿Tiene el cuello largo? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("n"), lana = L("n"), cuello = L("s")))
    def a_122221221(self):
        print("El animal que busca es una JIRAFA")
        self.declare(Fact(animal = "jirafa", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "n", lana = "n", cuello = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("n"), lana = L("n"), cuello = L("n")))
    def a_122221222(self):
        print("El animal no tiene el cuello tan largo")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "n", lana = "n", cuello = "n", rayas = input("¿Tiene rayas? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("n"), lana = L("n"), cuello = L("n"), rayas = L("s")))
    def a_1222212221(self):
        print("El animal que busca es una CEBRA")
        self.declare(Fact(animal = "cebra", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "n", lana = "n", cuello = "n", rayas = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("s"), cuernos = L("n"), lana = L("n"), cuello = L("n"), rayas = L("n")))
    def a_1222212222(self):
        print("El animal que busca es un CABALLO")
        self.declare(Fact(animal = "caballo", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "s", cuernos = "n", lana = "n", cuello = "n", rayas = "n"))
#NO UNGULADO
    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("n")))
    def a_122222(self):
        print("Es un animal terrestre")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "n", salvaje = input("¿Es salvaje? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("n"), salvaje = L("s")))
    def a_1222221(self):
        print("Es un felino")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "n", salvaje = "s", rom = input("¿Tiene rayas o manchas? (r/m): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("n"), salvaje = L("s"), rom = L("r")))
    def a_12222211(self):
        print("El animal que busca es un TIGRE")
        self.declare(Fact(animal = "tigre", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "n", salvaje = "s", rom = "r"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("n"), salvaje = L("s"), rom = L("m")))
    def a_12222212(self):
        print("El animal que busca es un LEOPARDO")
        self.declare(Fact(animal = "leopardo", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "n", salvaje = "s", rom = "m"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("n"), salvaje = L("n")))
    def a_1222222(self):
        print("Es un primate")
        self.declare(Fact(animal = "animal", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "n", salvaje = "n", grande = input("¿Es grande? (s/n): ")))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("n"), salvaje = L("n"), grande = L("s")))
    def a_12222221(self):
        print("El animal que busca es un GORILA")
        self.declare(Fact(animal = "GORILA", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "n", salvaje = "n", grande = "s"))

    @Rule(Fact(animal = L("animal"), extinto = L("n"), marino = L("n"), ave = L("n"), reptil = L("n"), pezuñas = L("n"), salvaje = L("n"), grande = L("n")))
    def a_12222222(self):
        print("El animal que busca es un MONO")
        self.declare(Fact(animal = "mono", extinto = "n", marino = "n", ave = "n", reptil = "n", pezuñas = "n", salvaje = "n", grande = "n"))
