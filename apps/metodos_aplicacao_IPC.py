"""
    Este modulo destina-se aos metodos para o funcionamento do sistema do ipc

"""
def Calcula_Relativo_IPC_subitem(peso_atual, peso_anterior):
    """
        este metodo calculara a razao entre o peso atual do subitem e o peso anterior do subitem
    """
    return peso_atual/peso_anterior

def Calcula_CGrupo(relativo, peso_item):
    """
        este metodo ira calcular o c-grupo
    """
    return relativo * peso_item

def Calculo_razao_mensal_subitem(preco_atual, preco_anterior):
    """
        Este metodo retornara a razao entre o preco do mes atual e o preco anterior dos subintens, serve como base para o metodo que calcula
    a media dos subitens daquele mes.

    """
    return preco_atual/preco_anterior


def RetornaPercentualPrecos(preco_atual, preco_anterior):
    '''
        Metodo que calcula a porcentagem de variacao de preco de um mes para outro
    '''
    produto = preco_anterior- preco_atual
    primeira_parte = preco_anterior*produto
    return (primeira_parte/100)

def Calcula_Media_Mensal_Subitem(total_razao_subitens, numero_subitens):
    """
        Este metodo busca retornar a media geral mensal dos subitens, divide o somatorio das razoes dos subitens pelo numero total de subintes.
    """
    return total_razao_subitens/numero_subitens


def Calcula_peso():

    """
        calcula o peso de forma generica
    """
    pass