# Sacar el precio de un area rectangular con base(b=120), altura(a=160). Cuesta x (30) dolares por 1 unidad cuadrada

class Rectangulo:
   def __init__(self, base, altura, costo_unidad=0):
       self.base = base
       self.altura = altura
       self.costo_unidad = costo_unidad

   def obtener_area(self):
       return self.base * self.altura

   def calcular_costo(self):
       area = self.obtener_area()
       return area * self.costo_unidad

r = Rectangulo(120, 160, 30)
print("Precio del Rectangulo: %s por unidades cuadradas" % (r.obtener_area()))
