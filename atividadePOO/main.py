from banco.Conta import ContaBancaria;


conta1 = ContaBancaria("433-4", "Everaldo", "corrente", 1000, 10000)

conta1.deposita(2000)
print(dir(conta1))

