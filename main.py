from lib import cuadrado
from lib.circunferencia import get_area

print ("Proyecto Figuras")
print (cuadrado.get_identificador())
lado = 4
print(f"El area de un {cuadrado.get_identificador()} de lado {lado} es: "
     f"{cuadrado.get_area(lado)} y el perimetro es {cuadrado.get_perimetro(lado)}")

print(f"El area de una circunferencia de radio 5 es: {get_area(5)}")