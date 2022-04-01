
def notas(*num, sit=False):
    """
    Calcula a média de uma aluno.
    :param num: Cada nota, pode receber mais de uma
    :param sit: (opcional) Mostra a situação do aluno de acordo com sua nota.
    :return: Retorna um dicionário com várias informações.
    """
    aluno = dict()
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['média'] = sum(num) / len(num)
    if sit:
        if aluno['média'] >= 7:
            aluno['situação'] = 'BOA'
        elif aluno['média'] >= 5:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


resp = notas(8, 10, 9, sit=True)
for k, v in resp.items():
    print(f'{k.title()}: {v}')
