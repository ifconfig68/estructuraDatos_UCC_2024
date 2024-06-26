from .tipos import Item
from .tipos import Vehiculo
from random import randint

class Nodo:
    def __init__(self, valor: Vehiculo  ):
        
        self.valor = valor
        self.siguiente = None
        
        
        
       
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    
    def esta_vacia(self):
        return self.primero is None

    def encolar(self, valor: Vehiculo  ) :
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.valor.id = randint(1, 1000)
        nuevo_nodo.valor.revisado = False
       
        
       
        if self.esta_vacia():
            self.primero = nuevo_nodo
                     
            
        else:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
        #print (nuevo_nodo.id)
    
    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        return valor
    
    def ver_listado(self):
        elementos = []
        if self.esta_vacia():
            return elementos
        current = self.primero
        while current:
            elementos.append(current.valor)
            current = current.siguiente
        return elementos    
    
    def ver_primero(self):
        if self.esta_vacia():
            return print(f"ingrese datos. la cola se encuentra vacia")
        return self.primero.valor

    def ver_ultimo(self):
        if self.esta_vacia():
            return print(f"ingrese datos. la cola se encuentra vacia")
        return self.ultimo.valor

    def contar(self):
        count = 0
        current = self.primero
        while current:
            count += 1
            current = current.siguiente
        return count
    
    
    
    def lavar_por_id(cola, id_vehiculo):
        current = cola.primero
        while current:
            if current.valor.id == id_vehiculo:
                current.valor.revisado = True
                
                print(f"Vehículo con ID {id_vehiculo} lavado.")
                             
                return
            current = current.siguiente
        print(f"No se encontró un vehículo con ID {id_vehiculo} en la cola.")
        
        
  
    
 
        