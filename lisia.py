
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função que retorna a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Função para exibir o status do reservatório
def exibir_status(nivel):
    if 1 <= nivel <= 5:
        cor = definir_cor(nivel)
        mensagem = niveis[nivel - 1]
        print(cor + mensagem + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "Nível inválido!" + Style.RESET_ALL)

# Simulação dos níveis (sem entrada do usuário)
print("=== Monitoramento do Reservatório ===\n")

for nivel in range(1, 6):
    exibir_status(nivel)