from memoria import registradores, memoria_ram

def atualizar_flags(valor):
  registradores['Z'] = 1 if valor == 0 else 0
  registradores['N'] = 1 if valor < 0 else 0

def endereco_para_inteiro(endereco):
  if isinstance(endereco, int):
        return endereco

  # Transforma M(x) em x
  endereco = endereco.strip().replace('M(', '').replace(')', '')
  return int(endereco, 0)

def executar_load(endereco):
    # AC ← MEM[X]
    registradores['MAR'] = endereco_para_inteiro(endereco)
    registradores['MBR'] = memoria_ram[registradores['MAR']]
    registradores['AC'] = registradores['MBR']
    atualizar_flags(registradores['AC'])

def executar_loadI(endereco):
    # AC ← MEM[MEM[X]]  (indireto)
    registradores['MAR'] = endereco_para_inteiro(endereco)
    registradores["MBR"] = memoria_ram[registradores["MAR"]]
    registradores['MAR'] = registradores["MBR"]
    registradores['MBR'] = memoria_ram[registradores['MAR']]
    registradores['AC'] = registradores['MBR']
    atualizar_flags(registradores['AC'])

def executar_store(endereco):
    # MEM[X] ← AC
    registradores['MAR'] = endereco_para_inteiro(endereco)
    registradores['MBR'] = registradores['AC']
    memoria_ram[registradores['MAR']] = registradores['MBR']

def executar_storeI(endereco):
    # MEM[MEM[X]] ← AC  (indireto)
    registradores['MAR'] = endereco_para_inteiro(endereco)
    registradores['MBR'] = memoria_ram[registradores['MAR']]
    registradores['MAR'] = registradores['MBR']
    memoria_ram[registradores['MAR']] = registradores['AC']

def executar_add(endereco):
    # AC ← AC + MEM[X]
    registradores['MAR'] = endereco_para_inteiro(endereco)
    registradores['MBR'] = memoria_ram[registradores['MAR']]
    resultado = registradores['AC'] + registradores['MBR']
    registradores['C'] = 1 if resultado > 0xFFFF else 0
    registradores['AC'] = resultado
    atualizar_flags(registradores['AC'])

def executar_sub(endereco):
    # AC ← AC - MEM[X]
    registradores['MAR'] = endereco_para_inteiro(endereco)
    registradores['MBR'] = memoria_ram[registradores['MAR']]
    registradores['AC'] = registradores['AC'] - registradores['MBR']
    atualizar_flags(registradores['AC'])

def executar_mult(endereco):
    # M:AC ← AC * MEM[X]
    registradores['MAR'] = endereco_para_inteiro(endereco)
    registradores['MBR'] = memoria_ram[registradores['MAR']]
    resultado = registradores['AC'] * registradores['MBR']
    registradores['M'] = resultado
    registradores['AC'] = resultado
    atualizar_flags(registradores['AC'])

def executar_jump(endereco):
    # PC ← X
    registradores['PC'] = endereco_para_inteiro(endereco)

def executar_jump_positivo(endereco):
    # se AC >= 0: PC ← end
    if registradores["AC"] >= 0:
        registradores["PC"] = endereco_para_inteiro(endereco)

def executar_move(destino, origem):
    # destino ← origem
    registradores[destino] = registradores[origem]
