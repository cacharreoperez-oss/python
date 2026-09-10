class Cliente:
	def __init__(self, dni, nombre, apellidos):
		self.__dni = dni
		self.__nombre = nombre
		self.__apellidos = apellidos

	@property
	def dni(self):
		return self.__dni

	@property
	def nombre(self):
		return self.__nombre

	@property
	def apellidos(self):
		return self.__apellidos


class Movimiento:
	def __init__(self, concepto, cantidad):
		self.__concepto = concepto
		self.__cantidad = cantidad

	@property
	def concepto(self):
		return self.__concepto

	@property
	def cantidad(self):
		return self.__cantidad


class Cuenta:
	__siguiente_numero = 1

	def __init__(self, titular):
		self.__numero = Cuenta.__siguiente_numero
		Cuenta.__siguiente_numero += 1
		self.__titular = titular
		self.__movimientos = []
		self.__saldo = 0

	@property
	def numero(self):
		return self.__numero

	@property
	def titular(self):
		return self.__titular

	@property
	def movimientos(self):
		return tuple(self.__movimientos)

	@property
	def saldo(self):
		return self.__saldo

	def añadir_movimiento(self, movimiento):
		self.__movimientos.append(movimiento)
		self.__saldo += movimiento.cantidad
