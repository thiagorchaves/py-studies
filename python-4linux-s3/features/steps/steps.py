from behave import step

def soma (x,y):
    return x + y

@step('somar "{n1}" com "{n2}"')
def test_soma(context, n1, n2):
    context.r_soma = soma(int(n1), int(n2))

@step('o resultado deve ser "{esperado}"')
def test_soma_result(context, esperado):
    assert context.r_soma == int(esperado), "descrição do erro"