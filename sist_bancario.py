

from abc import ABC, abstractmethod


# CLASE BASE ABSTRACTA: CUENTABANCARIA
class CuentaBancaria(ABC):

  def __init__(self, titular: str, cbu: str, saldo_inicial: float = 0.0):
    self.titular = titular  # TITULAR (PÚBLICO)
    self._cbu = cbu  # _CBU (PROTEGIDO, DE SOLO LECTURA MEDIANTE @PROPERTY)
    self._saldo = (
        saldo_inicial  # _SALDO (PROTEGIDO, CON @PROPERTY Y @SALDO.SETTER)
    )

  # @property para _cbu (solo lectura)
  @property
  def cbu(self):
    return self._cbu

  # @property para leer el saldo
  @property
  def saldo(self):
    return self._saldo

  # @saldo.setter con validación ValueError si es menor a cero
  @saldo.setter
  def saldo(self, nuevo_saldo: float):
    if nuevo_saldo < 0:
      raise ValueError(
          "El saldo no puede ser menor a cero."
      )  #
    self._saldo = nuevo_saldo

  # DEPOSITAR(MONTO): Suma dinero validando que el monto sea mayor a 0
  def depositar(self, monto: float):
    if monto <= 0:
      raise ValueError("El monto a depositar debe ser mayor a 0.")
    self._saldo += monto
    print(
        f" Depósito de ${monto:,.2f} realizado con éxito. Saldo actual:"
        f" ${self._saldo:,.2f}"
    )

  # @abstractmethod DEF EXTRAER(SELF, MONTO): Método obligatorio sin cuerpo (pass)
  @abstractmethod
  def extraer(self, monto: float):
    pass

  # __str__(): Retorna el formato "[TIPODECUENTA] TITULAR: ... | CBU: ... | SALDO: $..."
  def __str__(self):
    tipo_cuenta = self.__class__.__name__.upper()
    return (
        f"[{tipo_cuenta}] TITULAR: {self.titular} | CBU: {self._cbu} | SALDO:"
        f" ${self._saldo:,.2f}"
    )


# CLASES HIJAS 


class CuentaAhorro(CuentaBancaria):

  def extraer(self, monto: float):
    if monto <= 0:
      raise ValueError("El monto a extraer debe ser mayor a 0.")
    if monto > self._saldo:
      print(
          f" Fondos insuficientes. Saldo actual: ${self._saldo:,.2f}"
          f"."
      )
      return False
    self._saldo -= monto
    print(
        f" Extracción de ${monto:,.2f} exitosa. Saldo actual:"
        f" ${self._saldo:,.2f}"
    )
    return True

  # Agrega el método propio aplicar_interes(): Suma al saldo un interés del 0.1% (tasa = 0.001)
  def aplicar_interes(self, tasa: float = 0.001):
    interes = self._saldo * tasa
    self._saldo += interes
    print(
        f" Interés aplicado ({tasa * 100}%): +${interes:,.2f}. Nuevo saldo:"
        f" ${self._saldo:,.2f}"
    )


class CuentaCorriente(CuentaBancaria):

  def __init__(
      self,
      titular: str,
      cbu: str,
      saldo_inicial: float = 0.0,
      limite_descubierto: float = 500.0,
  ):
    super().__init__(titular, cbu, saldo_inicial)
    self.limite_descubierto = (
        limite_descubierto  # Recibe por parámetro un limite_descubierto (por defecto $500)
    )

  # Sobrescribe extraer(monto): Permite retirar dinero incluso si el saldo no alcanza, siempre que no supere saldo + limite_descubierto.
  def extraer(self, monto: float):
    if monto <= 0:
      raise ValueError("El monto a extraer debe ser mayor a 0.")

    fondos_totales = self._saldo + self.limite_descubierto
    if monto > fondos_totales:
      print(
          " Extracción rechazada. Supera el saldo y el límite de"
          f" descubierto (${fondos_totales:,.2f})"
      )
      return False

    self._saldo -= monto
    print(
        f" Extracción en descubierto de ${monto:,.2f} exitosa. Saldo actual:"
        f" ${self._saldo:,.2f}"
    )
    return True

  def __str__(self):
    return f"{super().__str__()} | DESCUBIERTO: ${self.limite_descubierto:,.2f}"


class CuentaCheque(CuentaBancaria):

  def __init__(
      self,
      titular: str,
      cbu: str,
      saldo_inicial: float = 0.0,
      costo_emision: float = 50.0,
  ):
    super().__init__(titular, cbu, saldo_inicial)
    self.costo_emision = (
        costo_emision  # Recibe un costo_emision fijo por cheque/extracción (por defecto $50)
    )

  # Sobrescribe extraer(monto): Descuenta el monto solicitado más el costo administrativo por emisión de cheque ($50).
  def extraer(self, monto: float):
    if monto <= 0:
      raise ValueError("El monto a extraer debe ser mayor a 0.")

    monto_total = monto + self.costo_emision
    if monto_total > self._saldo:
      print(
          f" Fondos insuficientes para cubrir el monto de ${monto:,.2f} +"
          f" costo de emisión de ${self.costo_emision:,.2f}"
      )
      return False

    self._saldo -= monto_total
    print(
        f" Extracción de ${monto:,.2f} con costo de emisión de"
        f" ${self.costo_emision:,.2f} exitosa. Saldo actual: ${self._saldo:,.2f}"
    )
    return True

  def __str__(self):
    return f"{super().__str__()} | COSTO EMISIÓN: ${self.costo_emision:,.2f}"



# BLOQUE DE PRUEBAS

if __name__ == "__main__":
  print("--- PRUEBA CUENTA AHORRO ---")
  ca = CuentaAhorro("Micaela Medina", "1234567890", 10000.0)
  print(ca)
  ca.aplicar_interes()
  ca.extraer(5000.0)
  print(ca)

  print("\n--- PRUEBA CUENTA CORRIENTE (Por defecto $500 descubierto) ---")
  cc = CuentaCorriente("Micaela Medina", "0987654321", 1000.0)
  print(cc)
  cc.extraer(1200.0)  # Entra en descubierto perfectamente
  print(cc)

  print("\n--- PRUEBA CUENTA CHEQUE (Por defecto $50 costo emisión) ---")
  cq = CuentaCheque("Micaela Medina", "1122334455", 5000.0)
  print(cq)
  cq.extraer(1000.0)  # Extrae 1000 + 50 de costo
  print(cq)