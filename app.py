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

def main():
    registradores['PC'] = hex_para_indice("0xA0")

    #ciclo de busca:
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

if __name__ == "__main__":
    main()