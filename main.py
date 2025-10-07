from lib import cuadrado, triangulo, rectangulo
print("Proyecto Cuadrado")
print(cuadrado.get_identificador())
l=4
print(f"El area de un {cuadrado.get_identificador()} de lado {l} es:{cuadrado.area_cuadrado(l)} y el perimetro es {cuadrado.get_perimetro(l)}")
 
base=4
altura=2
print(triangulo.identificador())
print(f"El area de {triangulo.identificador()} de base {base} y altura {altura}\
	es: {triangulo.get_area(base,altura)} y el perimetro es: {triangulo.get_perimetro(base,base,base)}")

base=4
altura=2
print(rectangulo.get_identificador())
print(f"El area de un {rectangulo.get_identificador()} de base {base} y altura {altura} es: {rectangulo.area_rectangulo(base,altura)}\
      y el perimetro es: {rectangulo.perimetro_rectangulo(base,altura)}")
