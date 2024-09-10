class Pessoa:
    # atributos
    cidade = "Brasília"
    telefone = "(61) 98765-4321"
    email = "nome@gmail.com"

# Subclasse (classe-filha)
class PessoaFisica(Pessoa):
    nome = "Fulano de tal"
    cpf = "123.456.678-11"
    peso = 80
    altura = 1.70

class PessoaJuridica(Pessoa):
    nome_fantasia = "Cobra Kai"
    razao_social = "Fulano de tal S.A"
    cnpj = "62.245.916/0001-69"


if __name__ == '__main__':
    # instancia de objetos
    usuario = PessoaFisica()
    empresa = PessoaJuridica()

print(f"{"-"*30} DADOS DO USUARIO {"-"*30}")
print(f"Nome do usuário: {usuario.nome}.")
print(f"CPF do usuário: {usuario.cpf}.")
print(f"Peso do usuário: {usuario.peso}.")
print(f"Altura do usuário: {usuario.altura}.")
print(f"Cidade do usuário: {usuario.cidade}.")
print(f"Telefone do usuário: {usuario.telefone}.")
print(f"E-mail do usuário: {usuario.email}.")

print(f"{"-"*30} DADOS DO USUARIO {"-"*30}")
print(f"Nome da empresa: {usuario.nome}.")
print(f"Razão Social da empresa: {usuario.cpf}.")
print(f"CNPJ da empresa: {usuario.peso}.")
print(f"Cidade sede da empresa: {usuario.altura}.")
print(f"Telefone da empresa: {usuario.cidade}.")
print(f"E-mail da empresa: {usuario.telefone}.")


