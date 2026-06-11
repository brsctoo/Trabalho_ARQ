memoria_ram = [0] * 256

registradores = {
    'A': 0, 'B': 0,
    'PC': 0, 'IR': '',
    'MAR': 0, 'MBR': 0,
    'AC': 0, 'M': 0, 'R': 0,
    'C': 0, 'N': 0, 'Z': 0
}

def executar_load(endereco):
    registradores["AC"] = memoria_ram[endereco]
    
def executar_store(endereco):
    memoria_ram[endereco] = registradores["AC"]

def executar_add(endereco):
    registradores["AC"] += memoria_ram[endereco]

def executar_sub(endereco):
    registradores["AC"] -= memoria_ram[endereco]
    
def executar_mult(endereco):
    registradores["AC"] *= memoria_ram[endereco]

def executar_jump(endereco):
    registradores["PC"] = endereco

def executar_jump_positivo(endereco):
    if registradores["AC"] > 0:
        registradores["PC"] = endereco

def executar_move(destino, origem):
    registradores[destino] = registradores[origem]

def executar_loadI(endereco):
    registradores["MAR"] = endereco
    registradores["MBR"] = memoria_ram[registradores["MAR"]]
    registradores["AC"] = memoria_ram[registradores["MBR"]]

def executar_storeI(endereco):
    registradores["MAR"] = endereco
    registradores["MBR"] = memoria_ram[registradores["MAR"]]
    memoria_ram[registradores["MBR"]] = registradores["AC"]