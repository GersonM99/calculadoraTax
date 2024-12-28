def calcular_tax():

    nombre_producto = input("nombre del producto:")
    valor_producto = float(input("valor del producto:"))
    peso = float(input("peso del producto en kg:"))
    retraso = input("lleva más de 30 días de retraso?(True/False):")
    retraso = retraso.lower() == "true"

#fase1 calculadora de peso
    if peso >= 10:
        impuesto = valor_producto * 0.03
    else:
        impuesto = valor_producto * 0.057

#fase2 validador de retrasos

    if retraso:
        descuento = valor_producto * 0.03
        valor_producto -= descuento

#fase3 creacion de nuevas variables para imprimir

    precio_final = valor_producto + impuesto
    producto_final = nombre_producto

#fase final imprimir

    print(f"Resumen del pedido:")
    print(f"Producto: {producto_final}")
    print(f"Valor original: {valor_producto}")
    print(f"Impuesto: {impuesto}")
    if retraso:
#es necesario darle un tab a la siguiente linea pues de otra manera el if da error
        print(f"Descuento por retraso:{descuento}")
    print(f"Precio final:{precio_final}")

calcular_tax()