class CuentaBancaria:

    def __init__(self, titular):
        self.titular = titular;
        self.saldo = 0;

    def depositar(self, monto: int):
        self.saldo += monto;
        print(f"Se deposito ${self.saldo} en la cuenta de {self.titular}");

    def retirar(self, monto:int):

        if(monto > self.saldo):
            print("[ERROR] El monto solicitado excede el saldo de la cuenta");
        else:
            self.saldo -= monto;
            print(f"Se retiro ${monto} de la cuenta de {self.titular}");


cuenta1 = CuentaBancaria("Santiago");
cuenta1.depositar(1000);
cuenta1.retirar(900);
cuenta1.retirar(200);
