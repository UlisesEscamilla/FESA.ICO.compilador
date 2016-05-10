# -*- coding: cp1252 -*-
import time

# Importamos los módulos necesarios
import wx
from formx import MyFrame1

"""

   Máquina virtual v 2.1
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
     tablaVar = {}           # Diccionario auxiliar para ligar la posición de memoria con su valor lógico
     loads = ["LDA","LDV","JMZ","JMP"]

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
             if(not(tokens[i][0:3] in self.loads)):             # Ignora como variables, los parametros de JMP, JMZ, LDA y LDV
                  if(tokens[i][4:] != "None"):
                      if(not(tokens[i][4:] in self.tablaVar)):                          
                          #if((tokens[i][4:]).isnumeric()):
                          if((tokens[i][4:]).isdigit()):
                               self.memory[limvar] = int((tokens[i][4:]))       # Inicializa la constante numerica 
                          else:
                               self.memory[limvar] = 0                          # Crea un espacio de memoria para una variable
                          
                          self.tablaVar[tokens[i][4:]] = limvar                 # Guarda en la tabla de Variables su dirección física
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
          return True



# Clase que hereda de myFrame1| (boton)
class MaquinaVirtual(MyFrame1):
    pc = 0              # Inicia en 0, lleva el conteo de la instrucción siguiente
    ac = 0              # Acumulador, no es un tipo de dato inmutable
    instructions = []   # lista de inastrucciones separadas en tokens
    memory = Memoria()         # Memoria virtual RAM
    # Instrucciones soportadas del ensamblador
    nemonicos = ["LDA","LDV","STA","IN1","IN2","IN3","IN4","ADD","SUB","MUL","DIV","JMZ","JMP","CALL","RET"]

    #Btn Cargar a memoria
    def b_loaodOnButtonClick(self, envent):
        #wx.MessageBox("Programador: Carlos Ramos \nEquipo 8 \nOctubre 2015 \nNo me robes por favor :)")
        
        self.readCode(self.m_filePicker1.GetPath())        
        self.bringToMemory()
        # Carga los nemonicos a la memoria RAM  
        row = 0
        for i in self.memory.memory.values():
             self.m_grid1.SetCellValue(row,0,str(i))
             row = row + 1
        # Carga los nombres de variables            
        for i in self.memory.tablaVar:
             self.m_grid1.SetCellValue(int(self.memory.tablaVar[i]),1,i)
                                           
    #Btn Ejecutar
    def b_ejecutarOnButtonClick(self, envent):
        delay = float(self.m_slider1.GetValue()/100.0)
        self.execute(delay)


    # Lee el codigo ensamblador de un archivo txt
    # Recibe un archivo txt
    # Retorna un list con cada línea de codigo separada en tokens
    # Depende de def:SeparaTokens()
    def readCode(self, fuente):
        archivo = open(fuente,"r")
        tokens = []
        for linea in archivo:
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
    def execute (self,delay):
         instruccion = ""
         var = 0
         while instruccion != "END":
              # Retraso para la animación de ejecución
              time.sleep(delay) # En segudos
              print(delay)
              # Lee el nemonico 
              instruccion = self.memory.memory[self.pc]
              aux = instruccion
              # Coloca la instruccion leída en la interfaz gráfica
              self.inow.SetLabel(str(instruccion))
              # Sombrea la instrucción alojada en memoria
              self.m_grid1.SetCellBackgroundColour(int(self.pc), 0,(255,255,0))
              
              self.m_grid1.MakeCellVisible(int(self.pc),0)
              #self.m_grid1.ForceRefresh()
              # Refresca el grid
              self.m_grid1.Refresh()
              # Refresca la ventana
              self.Update()
              
              instruccion = instruccion[0:3]
              var = aux[4:]
              # Guarda en una localidad de memoria el valor de AC
              if instruccion == "STA":
                  dirFisica = self.memory.tablaVar[var]
                  self.memory.memory[dirFisica] = self.ac
                  
              # Suma el AC y el contenido de una direccion de memoria
              elif instruccion == "ADD":
                  dirFisica = self.memory.tablaVar[var]                  
                  self.ac = self.ac + self.memory.memory[dirFisica]
              # Carga un el AC la suma de éste y una direccion de memoria
              elif instruccion == "MUL":
                  dirFisica = self.memory.tablaVar[var]                  
                  self.ac = self.ac * self.memory.memory[dirFisica]
              # Divide el AC entre el contenido de una direccion de memoria
              elif instruccion == "DIV":
                  dirFisica = self.memory.tablaVar[var]                  
                  self.ac = int(self.ac / self.memory.memory[dirFisica])
              # Saca el modulo del AC y el contenido de una direccion de memoria 
              elif instruccion == "MOD":
                  dirFisica = self.memory.tablaVar[var]                  
                  self.ac = self.ac % self.memory.memory[dirFisica]                  
              # Carga un el AC a una direccion de memoria
              elif instruccion == "LDA":                  
                  dirFisica = self.memory.tablaVar[var]                  
                  self.ac = self.memory.memory[dirFisica]                 
              # Carga un valor al AC
              elif instruccion == "LDV":
                  var = int(var)                   
                  self.ac = var
              # Lee un valor entero
              elif instruccion == "IN1":
                  self.ac = int(input("Introduce un dato "))
              # Lee un caracter
              elif instruccion == "IN2":
                  self.ac = input("Introduce un dato ")
              # Escribe el AC en pantalla como un entero
              elif (instruccion == "IN3"):
                   dirFisica = self.memory.tablaVar[var]
                   print(int(self.memory.memory[dirFisica]))                   
              # Escribe el AC en pantalla como un caracter
              elif (instruccion == "IN4"):
                   print (self.ac)
              # Escribe un mensaje en pantalla
              elif (instruccion == "MSG"):
                   print (self.ac)
              elif instruccion == "SUB":
                  dirFisica = self.memory.tablaVar[var]
                  self.ac =  self.ac - self.memory.memory[dirFisica]
              elif instruccion == "JMP":
                  # Sombrea la instrucción alojada en memoria
                  self.m_grid1.SetCellBackgroundColour(int(self.pc), 0,(255,255,255)) 
                  self.pc = int(var)
                  self.pco.SetLabel(str(self.pc))
              elif instruccion == "JMZ":                  
                  if(self.ac != 0):
                      # Sombrea la instrucción alojada en memoria
                      self.m_grid1.SetCellBackgroundColour(int(self.pc), 0,(255,255,255)) 
                      self.pc = int(self.pc) + 1
                      self.pco.SetLabel(str(self.pc))
                  else:                      
                      # Sombrea la instrucción alojada en memoria
                      self.m_grid1.SetCellBackgroundColour(int(self.pc), 0,(255,255,255))
                      self.pc = int(var)
              # Compara el AC vs una direccion de memoria
              elif instruccion == "CMP":
                  self.pc = int(var) 
              # Guarda la posición del PC
              elif instruccion == "CALL":
                  pila.append(int(self.pc) + 1)
              # Regresa a la instruccion llamadora
              elif instruccion == "RET":
                  self.pc = pila.pop()
              if(instruccion != "JMZ" and instruccion != "JMP" and instruccion!= "CALL" and instruccion != "RET"):
                  # Sombrea la instrucción alojada en memoria
                  self.m_grid1.SetCellBackgroundColour(int(self.pc), 0,(255,255,255))  
                  self.pc = int(self.pc) + 1
                  self.pco.SetLabel(str(self.pc))


"""
Conexion con la clase gráfica
"""

# Frame de inicio
class start(MyFrame1): 
        
    #Btn about
    def m_button7OnButtonClick(self, envent):
        wx.MessageBox("Programador: Carlos Ramos \nEquipo 8 \nOctubre 2015 \nNo me robes por favor :)")



# Creamos una aplicacion wxPython de Inicio
app = wx.App(False)
frame = MaquinaVirtual(None)
frame.Show()
app.MainLoop()


"""
mv = MaquinaVirtual()
mv.readCode("prog4.txt")
mv.bringToMemory()
mv.showMemory()
print(mv.memory.tablaVar)
mv.execute()
mv.showMemory()
print(mv.memory.tablaVar)
"""
