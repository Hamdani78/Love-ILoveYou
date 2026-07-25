import asyncio
import math
import pygame

# 1. Inisialisasi Pygame dengan mode RESIZABLE
pygame.init()

# Ambil resolusi layar device saat ini
info = pygame.display.Info()
WIDTH = info.current_w if info.current_w > 0 else 700
HEIGHT = info.current_h if info.current_h > 0 else 700

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Heart - I Love You")
clock = pygame.time.Clock()

SPEED = 0.005
NUM_ITEMS = 60

PINK = (234, 128, 176)
WHITE = (255, 255, 255)
BG_COLOR = (0, 0, 0)

font = pygame.font.Font(None, 28)


def get_heart_pos(t):
  x = 16 * (math.sin(t) ** 3)
  y = -(
      13 * math.cos(t)
      - 5 * math.cos(2 * t)
      - 2 * math.cos(3 * t)
      - math.cos(4 * t)
  )
  return x, y


async def main():
  # PENTING: Tambahkan 'screen' di variabel global
  global WIDTH, HEIGHT, screen
  running = True
  time_shift = 0.0

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.VIDEORESIZE:
        WIDTH, HEIGHT = event.w, event.h
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    screen.fill(BG_COLOR)
    time_shift += SPEED

    # Skala otomatis menyesuaikan layar device
    scale = min(WIDTH, HEIGHT) / 45

    for i in range(NUM_ITEMS):
      t = (i / NUM_ITEMS) * 2 * math.pi + time_shift

      x, y = get_heart_pos(t)
      x_next, y_next = get_heart_pos(t + 0.01)

      dx = x_next - x
      dy = y_next - y
      angle = math.degrees(math.atan2(-dy, dx)) - 30

      screen_x = int(WIDTH / 2 + x * scale)
      screen_y = int(HEIGHT / 2 + y * scale)

      text_surf = font.render("I love you", True, PINK)
      rotated_surf = pygame.transform.rotate(text_surf, angle)

      glow_surf = font.render("I love you", True, WHITE)
      glow_surf.set_alpha(120)
      rotated_glow = pygame.transform.rotate(glow_surf, angle)

      rect = rotated_surf.get_rect(center=(screen_x, screen_y))

      screen.blit(rotated_glow, rect.move(1, 1))
      screen.blit(rotated_surf, rect)

    pygame.display.flip()
    clock.tick(60)

    # WAJIB untuk WebAssembly/Pygbag
    await asyncio.sleep(0)

  pygame.quit()


asyncio.run(main())