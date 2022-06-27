
class Cuenta():
    '''
    classdocs
    '''
    def __init__(self, saldoInicial):
        '''
        Constructor
        '''
        self.saldo=saldoInicial
    def __str__ (self):
        return "La cuenta bancaria tiene un saldo de " + str(self.saldo)
    def depositar(self,monto):
        self.saldo+=monto
    def extraer(self,monto):
        if self.saldo >= monto:
            self.saldo-=monto
        else:
            print("No hay saldo disponible")
            
#ahora agregue esta linea editando en github 
# y yo agrego esta desde vsc 

#agrego esta linea desde LAB daec con otra cuenta
