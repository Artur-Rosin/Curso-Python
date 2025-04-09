import pygame
import random
import math
import sys
from pygame import gfxdraw

# Inicialização
pygame.init()

# Configurações
LARGURA, ALTURA = 800, 600
VELOCIDADE = 22000
TAMANHO_SEGMENTO = 20

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE_CLARO = (144, 238, 144)
CINZA = (200, 200, 200)
VERMELHO = (255, 50, 50)
MARROM = (139, 69, 19)

# Cores da cobra
CORES_COBRA = {
    'verde': [(0, 255, 0), (0, 200, 0)],
    'azul': [(0, 0, 255), (0, 0, 200)],
    'amarelo': [(255, 255, 0), (200, 200, 0)],
    'preto': [(50, 50, 50), (30, 30, 30)],
    'roxo': [(128, 0, 128), (102, 0, 102)]
}

cor_atual = 'verde'

# Tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Cobrinha com Pause')
relogio = pygame.time.Clock()

def criar_fundo():
    textura = pygame.Surface((LARGURA, ALTURA))
    for y in range(0, ALTURA, 40):
        for x in range(0, LARGURA, 40):
            cor = VERDE_CLARO if (x//40 + y//40) % 2 == 0 else CINZA
            pygame.draw.rect(textura, cor, (x, y, 40, 40))
    return textura

fundo = criar_fundo()

def desenhar_cabeca(pos, direcao, cor):
    x, y = pos
    cor_clara, cor_escura = CORES_COBRA[cor]
    pygame.draw.ellipse(tela, cor_clara, (x-12, y-10, 24, 20))
    pygame.draw.ellipse(tela, cor_escura, (x-10, y-8, 20, 16), 2)
    
    angulo = math.atan2(direcao[1], direcao[0])
    for offset in [-0.3, 0.3]:
        olho_x = x + 10 * math.cos(angulo + offset)
        olho_y = y + 10 * math.sin(angulo + offset)
        pygame.draw.circle(tela, BRANCO, (int(olho_x), int(olho_y)), 4)
        pygame.draw.circle(tela, PRETO, (int(olho_x), int(olho_y)), 2)

def desenhar_segmento(pos, idx, cor):
    x, y = pos
    cor_clara, cor_escura = CORES_COBRA[cor]
    pygame.draw.ellipse(tela, cor_clara, (x-10, y-8, 20, 16))
    if idx % 3 == 0:
        pygame.draw.arc(tela, cor_escura, (x-10, y-8, 20, 16), 0, math.pi, 2)

def desenhar_maca(pos):
    x, y = pos
    pygame.draw.circle(tela, VERMELHO, (x, y), 10)
    pygame.draw.ellipse(tela, MARROM, (x-3, y-12, 6, 8))

def mostrar_menu_cores():
    tela.blit(fundo, (0, 0))
    titulo = pygame.font.SysFont('Arial', 50).render("Escolha a Cor da Cobra", True, PRETO)
    tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 100))
    
    botoes = []
    for i, (nome, cores) in enumerate(CORES_COBRA.items()):
        rect = pygame.Rect(LARGURA//2 - 100, 200 + i*70, 200, 50)
        pygame.draw.rect(tela, cores[0], rect)
        pygame.draw.rect(tela, PRETO, rect, 2)
        
        texto = pygame.font.SysFont('Arial', 24).render(nome.capitalize(), True, PRETO)
        tela.blit(texto, (rect.centerx - texto.get_width()//2, rect.centery - texto.get_height()//2))
        botoes.append((rect, nome))
    
    pygame.display.flip()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for rect, nome in botoes:
                    if rect.collidepoint(evento.pos):
                        return nome

def mostrar_texto_pause():
    overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    tela.blit(overlay, (0, 0))
    
    texto = pygame.font.SysFont('Arial', 60, bold=True).render("PAUSADO", True, BRANCO)
    tela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 - 30))
    
    texto = pygame.font.SysFont('Arial', 30).render("Pressione ESPAÇO para continuar", True, BRANCO)
    tela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 + 30))

def jogo(cor_selecionada):
    cobra = [[LARGURA//2, ALTURA//2]]
    direcao = [0, 0]
    maca = [random.randint(40, LARGURA-40), random.randint(40, ALTURA-40)]
    pontos = 0
    game_over = False
    pausado = False  # Novo estado de pause
    
    tempo_ultimo_movimento = 0
    intervalo_movimento = 50
    
    while True:
        tempo_atual = pygame.time.get_ticks()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                # Tecla ESPAÇO para pausar/continuar (funciona sempre)
                if evento.key == pygame.K_SPACE:
                    pausado = not pausado
                
                # Outros controles só funcionam se não estiver pausado
                if not pausado:
                    if evento.key in (pygame.K_LEFT, pygame.K_a) and direcao[0] <= 0:
                        direcao = [-TAMANHO_SEGMENTO//2, 0]
                    elif evento.key in (pygame.K_RIGHT, pygame.K_d) and direcao[0] >= 0:
                        direcao = [TAMANHO_SEGMENTO//2, 0]
                    elif evento.key in (pygame.K_UP, pygame.K_w) and direcao[1] <= 0:
                        direcao = [0, -TAMANHO_SEGMENTO//2]
                    elif evento.key in (pygame.K_DOWN, pygame.K_s) and direcao[1] >= 0:
                        direcao = [0, TAMANHO_SEGMENTO//2]
                    elif evento.key == pygame.K_r and game_over:
                        return
                    elif evento.key == pygame.K_c:
                        return "mudar_cor"
        
        # Lógica do jogo só roda se não estiver pausado e não estiver em game over
        if not pausado and not game_over and tempo_atual - tempo_ultimo_movimento > intervalo_movimento:
            tempo_ultimo_movimento = tempo_atual
            
            if direcao != [0, 0]:
                nova_cabeca = [cobra[0][0] + direcao[0], cobra[0][1] + direcao[1]]
                cobra.insert(0, nova_cabeca)
                
                if math.hypot(nova_cabeca[0]-maca[0], nova_cabeca[1]-maca[1]) < 15:
                    pontos += 1
                    maca = [random.randint(40, LARGURA-40), random.randint(40, ALTURA-40)]
                    intervalo_movimento = max(20, intervalo_movimento - 2)
                else:
                    cobra.pop()
                
                if (nova_cabeca[0] < 0 or nova_cabeca[0] >= LARGURA or
                    nova_cabeca[1] < 0 or nova_cabeca[1] >= ALTURA or
                    nova_cabeca in cobra[1:]):
                    game_over = True
        
        # Renderização
        tela.blit(fundo, (0, 0))
        desenhar_maca(maca)
        
        for i, segmento in enumerate(cobra):
            if i == 0:
                desenhar_cabeca(segmento, direcao, cor_selecionada)
            else:
                desenhar_segmento(segmento, i, cor_selecionada)
        
        texto = pygame.font.SysFont('Arial', 30).render(f"Pontos: {pontos}", True, PRETO)
        tela.blit(texto, (20, 20))
        
        if pausado:
            mostrar_texto_pause()
        elif game_over:
            overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            tela.blit(overlay, (0, 0))
            
            texto = pygame.font.SysFont('Arial', 50).render("GAME OVER", True, VERMELHO)
            tela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 - 60))
            
            texto = pygame.font.SysFont('Arial', 30).render("Pressione R para reiniciar", True, BRANCO)
            tela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 + 30))
            
            texto = pygame.font.SysFont('Arial', 30).render("Pressione C para mudar cor", True, BRANCO)
            tela.blit(texto, (LARGURA//2 - texto.get_width()//2, ALTURA//2 + 70))
        
        pygame.display.flip()
        relogio.tick(VELOCIDADE)

# Loop principal
cor_jogador = mostrar_menu_cores()
while True:
    resultado = jogo(cor_jogador)
    if resultado == "mudar_cor":
        cor_jogador = mostrar_menu_cores()