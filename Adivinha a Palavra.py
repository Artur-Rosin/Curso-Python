
import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Adivinhação de Palavras")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GRAY = (150, 150, 150)
LIGHT_BLUE = (173, 216, 230)

# Fontes
title_font = pygame.font.SysFont("Arial", 40, bold=True)
main_font = pygame.font.SysFont("Arial", 32)
hint_font = pygame.font.SysFont("Arial", 28)
score_font = pygame.font.SysFont("Arial", 24)

# Lista de palavras e dicas
words = [
    {"word": "python", "hint": "Linguagem de programação popular"},
    {"word": "jogo", "hint": "Forma de entretenimento interativo"},
    {"word": "computador", "hint": "Máquina que processa informações"},
    {"word": "programa", "hint": "Conjunto de instruções para o computador"},
    {"word": "algoritmo", "hint": "Sequência lógica para resolver problemas"},
]

# Variáveis do jogo
current_word = random.choice(words)
secret_word = current_word["word"]
hint = current_word["hint"]
attempts = 3
guess = ""
message = ""
game_over = False
score = 0.0
show_hint = True
game_started = False
case_sensitive = False  # False = não diferencia maiúsc/minúsc

# Função para desenhar botão
def draw_button(text, x, y, width, height, color, hover_color, text_color=WHITE):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height), border_radius=10)
        if click[0] == 1:
            pygame.time.delay(150)  # Pequeno atraso para feedback tátil
            return True
    else:
        pygame.draw.rect(screen, color, (x, y, width, height), border_radius=10)
    
    text_surf = main_font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=(x + width/2, y + height/2))
    screen.blit(text_surf, text_rect)
    return False

# Função para desenhar caixa de texto
def draw_text_box(x, y, width, height, text, active):
    color = LIGHT_BLUE if active else WHITE
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=5)
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2, border_radius=5)
    
    text_surf = main_font.render(text, True, BLACK)
    screen.blit(text_surf, (x + 10, y + 10))

# Função para reiniciar o jogo
def reset_game():
    global current_word, secret_word, hint, attempts, guess, message, game_over, show_hint
    current_word = random.choice(words)
    secret_word = current_word["word"]
    hint = current_word["hint"]
    attempts = 3
    guess = ""
    message = ""
    game_over = False
    show_hint = True

# Loop principal
running = True
text_box_active = False
while running:
    screen.fill(WHITE)
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_started:
            if event.type == pygame.KEYDOWN:
                if text_box_active:
                    if event.key == pygame.K_RETURN:
                        # Lógica de verificação do palpite
                        comparison = guess if case_sensitive else guess.lower()
                        target = secret_word if case_sensitive else secret_word.lower()
                        
                        if comparison == target:
                            score += 1
                            message = "Parabéns! Você acertou!"
                            game_over = True
                        else:
                            attempts -= 1
                            score -= 0.33
                            if attempts == 0:
                                message = f"Game Over! A palavra era: {secret_word}"
                                game_over = True
                            else:
                                message = f"Errado! Tente novamente."
                                show_hint = True
                        guess = ""
                    elif event.key == pygame.K_BACKSPACE:
                        guess = guess[:-1]
                    elif len(guess) < 20:  # Limite de caracteres
                        guess += event.unicode
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se clicou na caixa de texto
                if 250 < event.pos[0] < 550 and 300 < event.pos[1] < 350:
                    text_box_active = True
                else:
                    text_box_active = False
    
    # Tela inicial
    if not game_started:
        # Título
        title = title_font.render("Jogo de Adivinhação", True, BLUE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        
        # Botão Começar
        if draw_button("Começar", WIDTH//2 - 100, 250, 200, 50, GREEN, (0, 150, 0)):
            game_started = True
            reset_game()
        
        # Botão Sair
        if draw_button("Sair", WIDTH//2 - 100, 320, 200, 50, RED, (150, 0, 0)):
            running = False
        
        # Opção de maiúsculas/minúsculas
        case_text = main_font.render("Diferencia maiúsculas/minúsculas:", True, BLACK)
        screen.blit(case_text, (WIDTH//2 - case_text.get_width()//2, 400))
        
        if draw_button("SIM" if case_sensitive else "NÃO", 
                      WIDTH//2 - 50, 450, 100, 40, 
                      BLUE if case_sensitive else GRAY, 
                      (0, 0, 150) if case_sensitive else (100, 100, 100)):
            case_sensitive = not case_sensitive
    
    # Tela do jogo
    else:
        # Título
        title = title_font.render("Adivinhe a Palavra!", True, BLUE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))
        
        # Placar
        score_text = score_font.render(f"Pontuação: {score:.2f}", True, BLACK)
        screen.blit(score_text, (20, 20))
        
        # Dica
        if show_hint:
            hint_title = main_font.render("Dica:", True, BLACK)
            screen.blit(hint_title, (WIDTH // 2 - hint_title.get_width() // 2, 100))
            
            hint_text = hint_font.render(hint, True, GRAY)
            screen.blit(hint_text, (WIDTH // 2 - hint_text.get_width() // 2, 140))
        
        # Tentativas
        attempts_text = main_font.render(f"Tentativas restantes: {attempts}", True, RED if attempts == 1 else BLACK)
        screen.blit(attempts_text, (WIDTH // 2 - attempts_text.get_width() // 2, 190))
        
        # Caixa de texto para palpite
        draw_text_box(250, 300, 300, 50, guess, text_box_active)
        
        # Botão Enviar
        if draw_button("Enviar", 570, 300, 120, 50, GREEN, (0, 150, 0)):
            comparison = guess if case_sensitive else guess.lower()
            target = secret_word if case_sensitive else secret_word.lower()
            
            if comparison == target:
                score += 1
                message = "Parabéns! Você acertou!"
                game_over = True
            else:
                attempts -= 1
                score -= 0.33
                if attempts == 0:
                    message = f"Game Over! A palavra era: {secret_word}"
                    game_over = True
                else:
                    message = f"Errado! Tente novamente."
                    show_hint = True
            guess = ""
        
        # Mensagem
        if message:
            message_color = GREEN if "Parabéns" in message else RED
            message_text = main_font.render(message, True, message_color)
            screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, 380))
        
        # Botão Sair durante o jogo
        if draw_button("Sair", 20, HEIGHT-70, 100, 40, RED, (150, 0, 0)):
            game_started = False
        
        # Reiniciar após game_over
        if game_over:
            if draw_button("Nova Palavra", WIDTH//2 - 100, 450, 200, 50, BLUE, (0, 0, 150)):
                reset_game()
    
    pygame.display.flip()

pygame.quit()
sys.exit()