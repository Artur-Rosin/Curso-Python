import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Adivinhação de Palavras")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonte
font = pygame.font.SysFont("Arial", 32)

# Lista de palavras e dicas
palavras = [
    {"palavra": "PYTHON", "dica": "Linguagem de programação"},
    {"palavra": "JOGO", "dica": "Entretenimento interativo"},
    {"palavra": "COMPUTADOR", "dica": "Máquina que processa dados"},
    {"palavra": "PROGRAMA", "dica": "Sequência de instruções"},
    {"palavra": "ALGORITMO", "dica": "Passo a passo para resolver um problema"},
]

# Sorteia uma palavra aleatória
palavra_sorteada = random.choice(palavras)
palavra_secreta = palavra_sorteada["palavra"]
dica = palavra_sorteada["dica"]

# Variáveis do jogo
tentativas = 3
palpite = ""
mensagem = ""
game_over = False

# Loop principal
running = True
while running:
    screen.fill(WHITE)
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if palpite.upper() == palavra_secreta:
                    mensagem = "Parabéns! Você acertou!"
                    game_over = True
                else:
                    tentativas -= 1
                    if tentativas == 0:
                        mensagem = f"Game Over! A palavra era: {palavra_secreta}"
                        game_over = True
                    else:
                        mensagem = f"Errado! Tente novamente. Tentativas restantes: {tentativas}"
                palpite = ""
            elif event.key == pygame.K_BACKSPACE:
                palpite = palpite[:-1]
            else:
                palpite += event.unicode
    
    # Renderização
    titulo = font.render("Adivinhe a Palavra!", True, BLUE)
    screen.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 50))
    
    dica_texto = font.render(f"Dica: {dica}", True, BLACK)
    screen.blit(dica_texto, (WIDTH // 2 - dica_texto.get_width() // 2, 120))
    
    palpite_texto = font.render(f"Seu palpite: {palpite}", True, BLACK)
    screen.blit(palpite_texto, (WIDTH // 2 - palpite_texto.get_width() // 2, 200))
    
    tentativas_texto = font.render(f"Tentativas restantes: {tentativas}", True, RED if tentativas == 1 else BLACK)
    screen.blit(tentativas_texto, (WIDTH // 2 - tentativas_texto.get_width() // 2, 250))
    
    if mensagem:
        mensagem_texto = font.render(mensagem, True, GREEN if "acertou" in mensagem else RED)
        screen.blit(mensagem_texto, (WIDTH // 2 - mensagem_texto.get_width() // 2, 350))
    
    pygame.display.flip()

pygame.quit()
sys.exit()