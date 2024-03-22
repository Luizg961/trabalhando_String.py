nome = "Luiz Gustvo"
idade = 23
profissao = "programador"
linguagem = "python"
saldo=45.268856

dados = {"nome": "luiz gustavo" , "idade":23}

print("nome: %s idade %d" % (nome,idade))
print("nome: {} idade {}" .format(nome,idade))

print("nome: {1} idade {0}" .format (nome,idade))
print("nome: {1} idade {0} nome: {1} {1} {0}" .format (nome,idade))

print("nome: {nome} idade {idade}" .format (nome=nome , idade=idade))
print("nome: {name} idade {age} {name} {age} " .format (age=idade , name=nome))
print("nome: {nome} idade {idade}" .format (**dados))

print(f"nome: {nome} idade: {idade}")
print(f"nome: {nome} idade: {idade} saldo: {saldo}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:0.2f}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:10.3f}")

