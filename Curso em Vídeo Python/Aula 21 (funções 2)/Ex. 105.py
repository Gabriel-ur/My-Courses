def notas(* n, sit=False):
    """
    Recebe notas de alunos:
        n: nota (1 ou +)
        sit: opcional, mostra situação
        return: dicionário com todas as informações
    Mostra o total de notas;
    Mostra a maior nota;
    Mostra a menor nota;
    Mostra a média dos notas;
    """
    al = {}

    al['Total'] = len(n)
    al['Maior nota'] = max(n)
    al['Menor nota'] = min(n)
    al['Média da turma'] = sum(n) / len(n)

    if sit == True:
        if al['Média da turma'] >= 7:
            al['Situação'] = 'BOA'
        elif 6 <= al['Média da turma'] < 7:
            al['Situação'] = 'RAZOÁVEL'
        else: 
            al['Situação'] = 'RUIM'

    print(al)


notas(2, 4, 7, 6, 6, sit=True)