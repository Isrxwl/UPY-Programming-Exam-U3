
import logging

# Configuración básica del logging
logging.basicConfig(filename='cajero.log', level=logging.ERROR, 
                    format='%(levelname)s:%(message)s', filemode='w')

# a) Define tu propia excepcion SaldoInsuficienteError
class SaldoInsuficienteError(Exception):
    def __init__(self, faltan):
        self.faltan = faltan
        self.message = f"faltan {self.faltan} pesos"
        super().__init__(self.message)

# INPUT
cuentas = {"1001": 5000, "1002": 1200}
operaciones = [("1001", "1500"), ("9999", "300"), ("1002", "abc"), 
               ("1002", "5000"), ("1001", "-100")]

# PROCESS
intentos = 0
exitosos = 0

for num_cuenta, monto_texto in operaciones:
    try:
        # b) Convierte el monto con int() dentro del try
        monto = int(monto_texto)
        
        # c) Lanza ValueError con raise cuando el monto no es positivo
        if monto <= 0:
            raise ValueError("Monto inválido, debe ser positivo")
        
        # Esto lanzará KeyError automáticamente si la cuenta no existe en el diccionario
        saldo_actual = cuentas[num_cuenta] 
        
        # d) Lanza SaldoInsuficienteError cuando el monto supera el saldo
        if monto > saldo_actual:
            faltante = monto - saldo_actual
            raise SaldoInsuficienteError(faltante)
            
        # Si todo sale bien, descuenta el monto
        cuentas[num_cuenta] -= monto
        
    # e) y g) Usa except separados y registra cada error en cajero.log
    except KeyError as e:
        error_msg = f"Cuenta inexistente: {e}"
        print(f"Error: {error_msg}")
        logging.error(error_msg)
        
    except ValueError as e:
        error_msg = f"Monto inválido: {e}"
        print(f"Error: {error_msg}")
        logging.error(error_msg)
        
    except SaldoInsuficienteError as e:
        error_msg = f"Saldo insuficiente: {e.message}"
        print(f"Error: {error_msg}")
        logging.error(error_msg)
        
    # f) Usa else para el caso exitoso
    else:
        exitosos += 1
        print(f"Operación exitosa: retiro de {monto} de la cuenta {num_cuenta}")
        
    # f) Usa finally para contar los intentos
    finally:
        intentos += 1

# OUTPUT
print("-" * 30)
print(f"Total de intentos: {intentos}")
print(f"Operaciones exitosas: {exitosos}")
print(f"Saldos finales: {cuentas}")

print("\nContenido de 'cajero.log':")
with open("cajero.log", "r") as log_file:
    print(log_file.read())