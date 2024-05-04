class ContaBancaria:
    __slots__=['_numero_agencia', '_titular', '_saldo', '_limite', '_tipo_conta']
    
    def __init__(self, numero_agencia, cliente, tipo_conta, saldo, limite) :
        self._numero_agencia = numero_agencia;
        self._titular = cliente;
        self._tipo_conta = tipo_conta;
        self._saldo = saldo;
        self._limite = limite;
        
    def consultar_saldo(self):
        return self._saldo;
    
    def saca(self, valor):
        self._saldo = self._saldo - valor;
        return self._saldo;
        
    def deposita(self, valor):
        self._saldo = self._saldo + valor;
        
    
    def transferePara(self, destino, valor):
        tmp = self.saca(valor);
        destino.deposita(tmp);
        
    def obter_extrato(self):
        return self.transacoes;

    def alterar_titular(self, novo_titular):
        self.nome = novo_titular;
        
    

   