import os

memoria_ram = [0] * 256

registradores = {
    'A': 0, 'B': 0,
    'PC': 0, 'IR': '',
    'MAR': 0, 'MBR': 0,
    'AC': 0, 'M': 0, 'R': 0,
    'C': 0, 'N': 0, 'Z': 0
}

def hex_para_indice(hex_str):
    hex_str = hex_str.strip()
    return int(hex_str, 16)

def indice_para_hex(indice):
    return f"0x{indice:02X}"

def ler_entrada(caminho):
    if not os.path.exists(caminho):
        print(f"Arquivo de testes '{caminho}' não foi encontrado.")
        return

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

        if not linha or linha.startswith('#'):
            if linha.startswith('#'):
                continue
            secao_atual += 1
            continue

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

def main():
    programa = interpretar_entrada("teste.txt")

    if programa is None:
        return

    for i, valor in enumerate(programa['dados']):
        memoria_ram[i] = valor

    registradores['PC'] = programa['endereco_inicial']

    # ciclo de busca:
    registradores['MAR'] = registradores['PC']
    registradores['MBR'] = memoria_ram[registradores['MAR']]
    registradores['IR'] = registradores['MBR']
    registradores['PC'] += 1

    #debug:
    print(f"PC : {indice_para_hex(registradores['PC'])}")
    print(f"MAR: {indice_para_hex(registradores['MAR'])}")
    print(f"IR : {registradores['IR']}")
    print(f"A  : {registradores['A']}")
    print(f"B  : {registradores['B']}")
    print(f"\nDados carregados: {programa['dados']}")
    print(f"Instruções a executar: {programa['instrucoes']}")

if __name__ == "__main__":
    main()
