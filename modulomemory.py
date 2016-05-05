# -*- coding: cp1252 -*-
"""

   Máquina virtual v 2.0
   Lee codigo ensamblador, previamente optimizado, y lo ejecuta paso a paso,
   mostrando en pantalla cada uno de ellos.
   Trabaja bajo el esquema de arquitectura Von Newman

   Lenguaje : Python 3.4
   Programadores: 
                  Carlos Ramos Flores
                  Ulises de la Cruz Escamilla
"""


"""
   #### Consideraciones ####
   # La localidad de memoria es un numero entero de 3 digitos
   # Las funciones que definan como valor de retorno a bool con True or False, 
     se trata del éxito de la operación. A menos que se indique lo contrario.
"""

class Memoria:
    
     longitud = 0            # longitud de la memoria
     memory = {}             # Diccionario que contiene la memoria
     tablaVar = {}     # Diccionario auxiliar para ligar la posición de memoria con su valor lógico

     # Crea un diccionario que simulará la memoria RAM
     # Recibe un int con la longitud que se creará la memoria
     # Retorna a bool con True or False
     def newMemory(self,tamanyo):
         # Asigna valor a variable int:longitud
         longitud = tamanyo
         return longitud


     # Carga cada token a una localidad de memoria
     # Recibe un list
     # Retorna a bool con True or False
     def loadMemory(self,tokens):
         # Asigna valor a variable dic:memory
         i = 0                # Recorrido de los tokens
         #x = 0               # Direccion de la memoria
         limite = len(tokens)
         limvar = limite                                        # Localidad donde se guardan las variables
         for i in range(limite):
             self.memory[i] = tokens[i]                         # Guarda en memoria el nemonico
             if(tokens[i][4:] != "None"):
                 if(not(tokens[i][4:] in self.tablaVar)):
                     self.memory[limvar] = 0                        # Crea un espacio de memoria para una variable
                     self.tablaVar[tokens[i][4:]] = limvar    # Guarda en la tabla de Variables su dirección física
                     limvar = limvar + 1  
         return True

    # Asigna valores de forma manual a la memoria
    # Recibe un diccionario
    # Retorna a bool con True or False
     def assignMemory(self,valoresAsig):
        pass
             # Asigna valor a variable dic:memory

     # Muestra los valores alojados en memoria
     # Retorna un diccionario con los valores de dic:memory
     def showMemory(self):
          for x in range(len(self.memory)):
               print (x, self.memory[x])
         #print self.memory
          return True


class MaquinaVirtual:
    pc = 0              # Inicia en 0, lleva el conteo de la instrucción siguiente
    ac = 0              # Acumulador, no es un tipo de dato inmutable
    instructions = []   # lista de inastrucciones separadas en tokens
    memory = Memoria()         # Memoria virtual RAM
    # Instrucciones soportadas del ensamblador
    nemonicos = ["LDA","LDV","STA","IN1","IN2","IN3","IN4","ADD","SUB","MUL","DIV","JMZ","JMP","CALL","RET"]
    
    # Lee el codigo ensamblador de un archivo txt
    # Recibe un archivo txt
    # Retorna un list con cada línea de codigo separada en tokens
    # Depende de def:SeparaTokens()
    def readCode(self, fuente):
        archivo = open(fuente,"r")
        tokens = []
        for linea in archivo:
            # LDA A
            # IN1 None
            #tokens.append(linea[0:3])
            #tokens.append(linea[4:-1])
            tokens.append(linea[0:-1])
        self.instructions = tokens
        return tokens

    # Lleva los tokens a la memoria
    def bringToMemory(self):
        self.memory.newMemory(len(self.instructions))      # Crea una memoria de tamaño len(tokens)
        self.memory.loadMemory(self.instructions)          # Carga los tokens en la memoria
        return True

    def showMemory(self):
         self.memory.showMemory()

    # Ejectuta las instrucciones de la memoria    
    def execute (self):
         instruccion = ""
         var = 0
         while instruccion != "END":
              # Lee el nemonico 
              instruccion = self.memory.memory[self.pc]
              aux = instruccion
              #print ("ins ",instruccion)
              instruccion = instruccion[0:3]
              var = aux[4:]

              # Carga en una localidad de memoria el valor de AC
              if instruccion == "STA":
                  #print("hola",var)
                  #print(self.memory.tablaVar[var])
                  dirFisica = self.memory.tablaVar[var]
                  self.memory.memory[dirFisica] = self.ac
              # Carga un el AC la suma de éste y una direccion de memoria
              elif instruccion == "ADD":
                  dirFisica = self.memory.tablaVar[var]
                  #print("1 ", self.memory.memory[dirFisica])
                  self.ac = self.ac + self.memory.memory[dirFisica]
               # Carga un el AC la suma de éste y una direccion de memoria
              elif instruccion == "MUL":
                  dirFisica = self.memory.tablaVar[var]
                  #print("1 ", self.memory.memory[dirFisica])
                  self.ac = self.ac * int(var)
              elif instruccion == "MOD":
                  dirFisica = self.memory.tablaVar[var]
                  #print("1 ", self.memory.memory[dirFisica])
                  self.ac = self.ac % int(var)
              # Carga un el AC a una direccion de memoria
              elif instruccion == "LDA":
                  #print("var ",var)
                  dirFisica = self.memory.tablaVar[var]
                  #print ("dirFis ",dirFisica)
                  self.ac = self.memory.memory[dirFisica]
                  #print ("lda ",self.ac)
              # Carga un valor al AC
              elif instruccion == "LDV":
                  dirFisica = self.memory.tablaVar[var]
                  self.ac = self.memory.memory[dirFisica]
              # Lee un valor entero
              elif instruccion == "IN1":
                  self.ac = int(input("Introduce un dato "))
              # Lee un caracter
              elif instruccion == "IN2":
                  self.ac = input("Introduce un dato ")
              # Escribe el AC en pantalla como un entero
              elif (instruccion == "IN3"):
                   print(int(self.ac))
              # Escribe el AC en pantalla como un caracter
              elif (instruccion == "IN4"):
                  print (self.ac)
              elif instruccion == "SUB":
                  #print("SUB AC ", self.ac)
                  #print("SUB TABLAV ", self.memory.tablaVar[var])
                  dirFisica = self.memory.tablaVar[var]
                  self.ac = self.memory.memory[dirFisica] - self.ac ################################################
                  print("SUB ", self.ac)
                  #print ("acum ",ac)
              elif instruccion == "JMP":
                  self.pc = int(var)
                  #print ("acum ",ac)
              elif instruccion == "JMZ":
                  #print("self.ac ", self.ac)
                  if(self.ac > 0):
                      self.pc = int(self.pc) + 1 
                      
                      #print ("self.pc ",self.pc)
                  else:
                      #self.pc = int(self.pc) + 1
                      self.pc = int(var)
                      #print "entro ", self.ac
              # Guarda la posición del PC
              elif instruccion == "CALL":
                  pila.append(int(self.pc) + 1)
              # Regresa a la instruccion llamadora
              elif instruccion == "RET":
                  self.pc = pila.pop()
              if(instruccion != "JMZ" and instruccion!= "CALL" and instruccion != "RET"):
                  self.pc = int(self.pc) + 1
              



mv = MaquinaVirtual()
mv.readCode("prog2.txt")
mv.bringToMemory()
mv.showMemory()
print(mv.memory.tablaVar)
mv.execute()
mv.showMemory()
print(mv.memory.tablaVar)




