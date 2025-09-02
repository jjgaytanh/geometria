from geometria import TrianguloRectangulo

t1 = TrianguloRectangulo(3, 4)
print(f"Triángulo rectángulo con catetos {t1.x} y {t1.y} creado.")
print(f"Hipotenusa: {t1.hipotenusa()}")
print(f"Perímetro: {t1.perimetro()}")
print(f"Area: {t1.area()}")
