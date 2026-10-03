import sys
from datetime import datetime, timedelta

import pygame


pygame.init()

WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Countdown")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 72)

countdown_seconds = 10
end_time = datetime.now() + timedelta(seconds=countdown_seconds)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    remaining = max((end_time - datetime.now()).total_seconds(), 0)
    minutes, seconds = divmod(int(remaining), 60)
    time_text = f"{minutes:02d}:{seconds:02d}"

    screen.fill((20, 20, 30))
    label = font.render(time_text, True, (255, 255, 255))
    label_rect = label.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(label, label_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
