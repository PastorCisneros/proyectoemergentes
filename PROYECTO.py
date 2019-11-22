from pyknow import *

class fallas(KnowledgeEngine):

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
    def a_1113(self):
        print("CAMBIA AUTOMATICO")
        self.declare(Fact(falla = "cambio automatico", automovil = "s", automatico = "s", modoestandar = "s",manejarestandar ='n'))
################################################################3
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n")))
    def a_1121(self):
        print("Es un automovil estandar")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = input("¿Sabes manejar? (s/n): ")))
    
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("n")))
    def a_1122(self):
        print("Es una automovil estandar y no sabe manejar pero vas aprender")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = ("n"), aprender = input("¿Quieres aprender? (s/n): ")))
    
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("n"),aprender=L("s")))
    def a_1123(self):
        print("BUSCAR CLASES")
        self.declare(Fact(falla = "buscar", automovil = "s", automatico = "n", manejar = ("n"), aprender = ("s")))
    
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("n"),aprender=L("n")))
    def a_1124(self):
        print("POSIBILIDAD DE ACCIDENTE")
        self.declare(Fact(falla = "accidente", automovil = "s", automatico = "n", manejar = ("n"), aprender = ("n")))
    

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s")))
    def a_1125(self):
        print("Es una automovil estandar y no sabe manejar")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = ("s"), licencia = input("¿Tienes Licencia? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("n")))
    def a_11222(self):
        print("SACAR LICENCIA")
        self.declare(Fact(falla = "sacar licencia", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("n"), sacarlicencia = input("¿ Sacaras tu Licencia? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("n"),sacarlicencia = L("s")))
    def a_11223(self):
        print("OBTENER CITA")
        self.declare(Fact(falla = "obtener cita", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("n"), sacarlicencia = ("s")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("n"),sacarlicencia = L("s")))
    def a_1122333333(self):
        print("OBTENER MULTA")
        self.declare(Fact(falla = "obtener multa", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("n"), sacarlicencia = ("n")))
#################################################
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s")))
    def a_112211112(self):
        print("Sabes manejar automovil modo estandar")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = input("¿ Llave en buen estado? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s")))
    def a_112212122(self):
        print("Sabes manejar automovil modo estandar y tienes llave")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = input("¿Tiene gasolina?s/n ")))   

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"), gasolina=L("n")))
    def a_112211111112(self):
        print("CARGAR GASOLINA")
        self.declare(Fact(falla = "cargar gasolina", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), cargogasolina = input("¿Cargo gasolina?s/n ")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("n"),cargogasolina=L("s")))
    def a_1134222(self):
        print("Cargo gasolina completa")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), cargogasolina = ("s"), arranca=input("¿Arranca s/n?")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("n"),cargogasolina=L("s"), arranca=L("n")))
    def a_1122342(self):
        print("GASOLINA ERRONEA")
        self.declare(Fact(falla = "gasolina erronea", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), cargogasolina = ("s"), arranca =("n")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("n"),cargogasolina=L("s"), arranca=L("s")))
    def a_1122223(self):
        print("GASOLINA CORRECTA")
        self.declare(Fact(falla = "gasolina erronea", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), cargogasolina = ("s"), arranca =("s")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("n"),cargogasolina=L("s"), arranca=L("n")))
    def a_1122224(self):
        print("GASOLINA ERRONEA")
        self.declare(Fact(falla = "gasolina erronea", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), cargogasolina = ("s"), arranca =("n"), gasolinaerronea=input("¿Cargo de gasolina erronea: s")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("n"),cargogasolina=L("s"), arranca=L("n"), gasolinaerronea=L("s")))
    def a_1122225(self):
        print("CAMBIO DE TANQUE DE COMBUSTIBLE")
        self.declare(Fact(falla = "cambio tanque", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), cargogasolina = ("s"), arranca =("n"), gasolinaerronea=("s")))
###########################################################################
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("n")))
    def a_1122226(self):
        print("IR CON EL CERRAJERO")
        self.declare(Fact(falla = "ir cerrejero", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), cerrajeroabierto = input("¿Esta abierto con el cerrajero? ")))   

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("n"), cerrajeroabierto=L("s")))
    def a_1122227(self):
        print("ARREGLAR LLAVE")
        self.declare(Fact(falla = "arreglar llave", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("n"), cerrajeroabierto = ("s")))   

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("n"), cerrajeroabierto=L("n")))
    def a_1122228(self):
        print("No tienes llave en buen estado para manejar")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("n"), cerrajeroabierto = ("n"),llaveemer=input("¿ tienes llave de emergencia?:s/n")))   

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("n"), cerrajeroabierto=L("n"),llaveemer=L("s")))
    def a_1122229(self):
        print("ARRANCA CARRO")
        self.declare(Fact(falla = "arranca", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("n"), cerrajeroabierto = ("n"),llaveemer=("s")))   

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"), cerrajeroabierto=L("n"),llaveemer=L("n")))
    def a_1122230(self):
        print("IR A LA AGENCIA")
        self.declare(Fact(falla = "ir a la agencia", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), cerrajeroabierto = ("n"),llaveemer=("n")))   
####################################################################################
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s")))
    def a_1122212(self):
        print("Tiene gasolina y su llave es la correcta")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = input("¿Tiene agua?s/n ")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("n")))
    def a_1122213(self):
        print("SE VA A CALENTAR")
        self.declare(Fact(falla = "calento", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("n")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s")))
    def a_1122214(self):
        print("Tiene gasolina, agua y su llave es la correcta")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=input("¿Tiene aceite?")))
    
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("n")))
    def a_1122215(self):
        print("SE VA A DESVIELAR")
        self.declare(Fact(falla = "desvielar", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("n")))
    
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("s")))
    def a_1122216(self):
        print("Tiene gasolina, agua y su llave es la correcta")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("s"),luces=input("¿Funcionan las luces:s/n?")))
    

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("s"),luces=L("n")))
    def a_1122217(self):
        print("VERIFICAR CARGA DE BATERIA")
        self.declare(Fact(falla = "verificar carga", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("s"),luces=("n"),carga=input("¿tiene carga?:s/n")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("s"),luces=L("n"),carga=L("n")))
    def a_1122218(self):
        print("LLEVAR AL ELECTRICO")
        self.declare(Fact(falla = "llevar electrico", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("s"),luces=("n"),carga=("n")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("s"),luces=L("n"),carga=L("s")))
    def a_1122219(self):
        print("CAMBIAR PILA")
        self.declare(Fact(falla = "cambiar pila", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("s"),luces=("n"),carga=("s")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("s"),luces=L("s")))
    def a_1122220(self):
        print("LLEVAR AL ELECTRICO")
        self.declare(Fact(falla = "llevar electrico", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("s"),luces=("s"),carretera=input("carretera en buen estado?:s/n")))
    
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("s"),luces=L("s"),carretera=L("n")))
    def a_1122234(self):
        print("CAMBIAR RUTA")
        self.declare(Fact(falla = "cambiar ruta", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("s"),luces=("s"),carretera=("n")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("s"),luces=L("s"),carretera=L("s")))
    def a_1122235(self):
        print("Todo va muy bien hasta ahora")
        self.declare(Fact(falla = "falla", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("s"),luces=("s"),carretera=("s"),oscuro=("esta oscuro?:s/n")))
    
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("s"),luces=L("s"),carretera=L("s"),oscuro=L("s")))
    def a_1122236(self):
        print("PUEDES TENER UN ACCIDENTE")
        self.declare(Fact(falla = "accidente", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("s"),luces=("s"),carretera=("s"),oscuro=("s"),ninos=input("Tienes niños adelante ?s/n")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("s"),luces=L("s"),carretera=L("s"),oscuro=L("s"),ninos=L("s")))
    def a_1122237(self):
        print("TENDRAS MULTA")
        self.declare(Fact(falla = "multa", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("s"),luces=("s"),carretera=("s"),oscuro=("s"),ninos=("s")))

    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("s"),luces=L("s"),carretera=L("s"),oscuro=L("s"),ninos=L("n")))
    def a_1122238(self):
        print("ESTADO PERFECTO")
        self.declare(Fact(falla = "perfecto", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("s"),luces=("s"),carretera=("s"),oscuro=("s"),ninos=("n")))
    
    @Rule(Fact(falla = L("falla"), automovil = L("s"), automatico = L("n"), manejar = L("s"), licencia = L("s"),estadollave =L("s"),gasolina=L("s"),agua=L("s"),aceite=L("s"),luces=L("s"),carretera=L("s"),oscuro=L("n")))
    def a_1122239(self):
        print("SIN PROBLEMAS")
        self.declare(Fact(falla = "problemasout", automovil = "s", automatico = "n", manejar = ("s"), licencia = ("s"), estadollave = ("s"), gasolina = ("n"), agua = ("s"), aceite=("s"),luces=("s"),carretera=("s"),oscuro=("n")))
#####################AVION 
    @Rule(Fact(falla = L("falla"), automovil = L("n")))
    def a_1(self):
        print("Es un avion")
        self.declare(Fact(falla = "falla", automovil = "n", nuevo = input("¿Es un avion nuevo? (s/n): ")))
    

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("n")))
    def a_2(self):
        print("Es un avion viejo")
        self.declare(Fact(falla = "falla", automovil = "n", nuevo="n", mantenimiento = input("¿tiene mantenimiento reciente? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("n"), mantenimiento=L("s")))
    def a_3(self):
        print("PUEDE DESPEJAR")
        self.declare(Fact(falla = "despejar", automovil = "n", nuevo="n", mantenimiento = ("s")))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("n"),mantenimiento=L("n")))
    def a_4(self):
        print("Es un avion viejo")
        self.declare(Fact(falla = "falla", automovil = "n", nuevo="n", mantenimiento="n", estabilizadores = input("¿Los estabilizadores funcionan? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("n"),mantenimiento=L("n"),estabilizadores=L("n")))
    def a_5(self):
        print("LIMPIA LOS ESTABILIZADORES")
        self.declare(Fact(falla = "limpia", automovil = "n", nuevo="n", mantenimiento="n", estabilizadores = ("n")))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("n"),mantenimiento=L("n"),estabilizadores=L("s")))
    def a_6(self):
        print("Es un avion viejo sin mantenimiento")
        self.declare(Fact(falla = "falla", automovil = "n", nuevo="n", mantenimiento="n", estabilizadores="s", combustible = input("¿Tiene combustible? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("n"),mantenimiento=L("n"),estabilizadores=L("s"),combustible=L("n")))
    def a_8(self):
        print("MAMAPERO CON PROBLEMAS")
        self.declare(Fact(falla = "falla", automovil = "n", nuevo="n", mantenimiento="n", estabilizadores="s", combustible = ("n")))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("n"),mantenimiento=L("n"),estabilizadores=L("s"),combustible=L("s")))
    def a_9(self):
        print("Es un avion viejo sin mantenimiento")
        self.declare(Fact(falla = "falla", automovil = "n", nuevo="n", mantenimiento="n", estabilizadores="s", combustible = ("s"),sonido = input("¿Hace sonidos anormales? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("n"),mantenimiento=L("n"),estabilizadores=L("s"),combustible=L("s"),sonido=L("n")))
    def a_10(self):
        print("PUEDE DESPEJAR")
        self.declare(Fact(falla = "despejar", automovil = "n", nuevo="n", mantenimiento="n", estabilizadores="s", combustible = ("s"),sonido = ("n")))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("n"),mantenimiento=L("n"),estabilizadores=L("s"),combustible=L("s"),sonidoL=("s")))
    def a_13(self):
        print("Es un avion viejo sin mantenimiento que hace sonidos")
        self.declare(Fact(falla = "falla", automovil = "n", nuevo="n", mantenimiento="n", estabilizadores="s", combustible = ("s"),sonido = ("s"), frente = input("¿En el frente? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("n"),mantenimiento=L("n"),estabilizadores=L("s"),combustible=L("s"),sonidoL=("s"),frente=L("s")))
    def a_14(self):
        print("TIMON DE DIRECCION CON PROBLEMAS")
        self.declare(Fact(falla = "timon", automovil = "n", nuevo="n", mantenimiento="n", estabilizadores="s", combustible = ("s"),sonido = ("s"), frente="s"))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("n"),mantenimiento=L("n"),estabilizadores=L("s"),combustible=L("s"),sonidoL=("s"),frente=L("n")))
    def a_15(self):
        print("CONO Y HELICE CON PROBLEMAS")
        self.declare(Fact(falla = "helice", automovil = "n", nuevo="n", mantenimiento="n", estabilizadores="s", combustible = ("s"),sonido = ("s"), frente="n"))


#########################################
    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("s")))
    def a_1101(self):
        print("Es un avion nuevo")
        self.declare(Fact(falla = "falla", automovil = "n", nuevo="s", pilotos = input("¿tiene pilotos expertos? (s/n): ")))
    
    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("s"),pilotos=L("n")))
    def a_1102(self):
        print("PROTOCOLO A1")
        self.declare(Fact(falla = "protocolo", automovil = "n", nuevo="s", pilotos = ("n")))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("s"),pilotos=L("s")))
    def a_1103(self):
        print("Es un avion nuevo con pilotos capacitados")
        self.declare(Fact(falla = "falla", automovil = "n", nuevo="s", pilotos="s",meteorologia = input("meteorologia buena? (s/n): ")))

    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("s"),pilotos=L("s"),meteorologia=L("s")))
    def a_1104(self):
        print("CAMBIAR ALERON")
        self.declare(Fact(falla = "falla", automovil = "n", nuevo="s", pilotos="s",meteorologia = ("s")))
    
    @Rule(Fact(falla = L("falla"), automovil = L("n"),nuevo=L("s"),pilotos=L("s"),meteorologia=L("n")))
    def a_1105(self):
        print("ACTIVAR ESTABILIZADOR")
        self.declare(Fact(falla = "falla", automovil = "n", nuevo="s", pilotos="s",meteorologia = ("n")))