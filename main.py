import os
import sys
from memoria import registradores, memoria_ram
from instrucoes import executar_instrucao

def hex_para_indice(hex_str):
    hex_str = hex_str.strip()
    return int(hex_str, 16)

def indice_para_hex(indice):
    if isinstance(indice, str):
        return indice
    return f"0x{indice:02X}"

def ler_entrada(caminho):
    if not os.path.exists(caminho):
        print(f"Arquivo de testes '{caminho}' não foi encontrado.")
        return None
    linhas = []
    with open(caminho) as arq:
        for i in arq:
            linhas.append(i)
    return linhas

def interpretar_entrada(caminho):
    lst_linhas = ler_entrada(caminho)
    if not lst_linhas:
        return None

    dados = []
    endereco_inicial = None
    instrucoes = []
    secao_atual = 0

    for linha in lst_linhas:
        linha = linha.strip()
        if not linha:
            secao_atual += 1
            continue
        if linha.startswith('#'):
            continue

#        if not linha or linha.startswith('#'):
#            if linha.startswith('#'):
#                continue
#            secao_atual += 1
#            continue

        if secao_atual == 0:
            try:
                dados.append(int(linha, 0))
            except ValueError:
                print(f"Erro ao interpretar dado: {linha}")

        elif secao_atual == 1:
            try:
                endereco_inicial = hex_para_indice(linha)
            except ValueError:
                print(f"Erro ao interpretar endereço: {linha}")

        elif secao_atual == 2:
            instrucoes.append(linha)

    return {
        'dados': dados,
        'endereco_inicial': endereco_inicial,
        'instrucoes': instrucoes
    }

def printar_estado():
    ''' Imprime o estado dos regs e da memória para debug '''
    print(f"\nPC: {indice_para_hex(registradores['PC'])} | MAR: {indice_para_hex(registradores['MAR'])}")
    print(f"IR: {registradores['IR']} | MBR: {indice_para_hex(registradores['MBR'])}")
    print(f"A: {registradores['A']} | B: {registradores['B']}")
    print(f"AC: {registradores['AC']}" f" | M: {registradores['M']} | R: {registradores['R']}")
    print(f"C: {registradores['C']} | N: {registradores['N']} | Z: {registradores['Z']}")
    print("\n" * 2)

def main():
    if sys.argv[1]:
        arquivo = sys.argv[1]
    else:
        print("Use 'python main.py [nome do txt]'")
        return
    programa = interpretar_entrada(arquivo)

    if programa is None:
        return

    for i, valor in enumerate(programa['dados']):
        memoria_ram[0x100 + i] = valor

    addr_instrucao = programa['endereco_inicial'] 
    for instrucao in programa['instrucoes']:
        memoria_ram[addr_instrucao] = instrucao
        addr_instrucao +=1
    
    registradores['PC'] = programa['endereco_inicial']

    print("Estado Inicial:")
    printar_estado()
    
    flag = True
    while flag:

        # ciclo de busca:
        registradores['MAR'] = registradores['PC']
        registradores['MBR'] = memoria_ram[registradores['MAR']]
        registradores['IR'] = registradores['MBR']
        registradores['PC'] += 1

        instrucao_atual = registradores['IR']
        if instrucao_atual == 0 or instrucao_atual == "":
            print("Fim do programa.")
            flag = False
            continue
    
        print(f"Instrução a ser executada: {instrucao_atual}")

        #Execucao:
        executar_instrucao(instrucao_atual)
        printar_estado()
        # input("Pressione ENTER para continuar...")
        


    #debug
    printar_estado()

if __name__ == "__main__":
    main()
