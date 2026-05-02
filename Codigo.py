from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Lista com as mensagens correspondentes aos níveis
mensagens = [
    "Nível 1 - Muito baixo, ação imediata❗",
    "Nível 2 - Baixo, poderia estar maior",
    "Nível 3 - Médio, poderia estar maior",
    "Nível 4 - Alto, otima quantidade de água reservada",
    "Nível 5 - Muito alto, recomenda-se supervisão"
]

# Função que retorna a cor de acordo com o nível
def cor_nivel(nivel):
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

# Função que converte porcentagem em nível
def calcular_nivel(porcentagem):
    if 0 <= porcentagem <= 20:
        return 1
    elif 20 < porcentagem <= 40:
        return 2
    elif 40 < porcentagem <= 60:
        return 3
    elif 60 < porcentagem <= 80:
        return 4
    elif 80 < porcentagem <= 100:
        return 5
    else:
        return None

# Entrada do usuário
try:
    porcentagem = int(input("Digite a porcentagem do reservatório (0 a 100): "))
    nivel = calcular_nivel(porcentagem)

    if nivel is not None:
        cor = cor_nivel(nivel)
        print(cor + mensagens[nivel - 1] + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "Valor inválido! Digite um número entre 0 e 100." + Style.RESET_ALL)

except ValueError:
    print(Fore.WHITE + "Entrada inválida! Digite apenas números." + Style.RESET_ALL)