from banco import Cliente, Cuenta, Movimiento


antonio = Cliente('12345678A', 'Antonio', 'Martínez')

cuenta_1 = Cuenta(antonio)
cuenta_1.añadir_movimiento(Movimiento('Nómina', 1500))
cuenta_1.añadir_movimiento(Movimiento('Alquiler', -700))
cuenta_1.añadir_movimiento(Movimiento('Compra', -50))

cuenta_2 = Cuenta(antonio)
cuenta_2.añadir_movimiento(Movimiento('Transferencia', 500))
cuenta_2.añadir_movimiento(Movimiento('Recibo', -120))
cuenta_2.añadir_movimiento(Movimiento('Compra', -30))

print(f'Cuenta {cuenta_1.numero}: {cuenta_1.saldo} euros')
print(f'Cuenta {cuenta_2.numero}: {cuenta_2.saldo} euros')