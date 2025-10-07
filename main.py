from lib import cuadrado, triangulo
print("Proyecto Cuadrado")
print(cuadrado.get_identificador())
l=4
print(f"El area de un {cuadrado.get_identificador()} de lado {l} es:{cuadrado.area_cuadrado(l)} y el perimetro es {cuadrado.get_perimetro(l)}")
 
base=4
altura=2
print(triangulo.get_identificador())
print(f"El area de {triangulo.get_identificador())} de base {base} y altura {altura}\
	es: {triangulo.get_area(base,altura)} y el perimetro es: {triangulo.get_perimetro(base,base,base)}")
