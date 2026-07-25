import asyncio  # 1. Import asyncio di paling atas
import math
import pygame

# 2. Inisialisasi Pygame & Konfigurasi
pygame.init()
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart - I Love You")
clock = pygame.time.Clock()

# Pengatur Kecepatan & Ukuran
SPEED = 0.005
NUM_ITEMS = 50  # Jumlah teks 'I love you'

# Warna
PINK = (234, 128, 176)
WHITE = (255, 255, 255)
BG_COLOR = (0, 0, 0)

# Font Default
font = pygame.font.Font(None, 30)


# Rumus Matematika Hati
def get_heart_pos(t):
  x = 16 * (math.sin(t) ** 3)
  y = -(
      13 * math.cos(t)
      - 5 * math.cos(2 * t)
      - 2 * math.cos(3 * t)
      - math.cos(4 * t)
  )
  return x, y


# 3. Seluruh Game Loop Dimasukkan ke Dalam Fungsi Async
async def main():
  running = True
  time_shift = 0.0

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    screen.fill(BG_COLOR)
    time_shift += SPEED

    for i in range(NUM_ITEMS):
      t = (i / NUM_ITEMS) * 2 * math.pi + time_shift

      x, y = get_heart_pos(t)
      x_next, y_next = get_heart_pos(t + 0.01)

      # Hitung Sudut Kemiringan Teks
      dx = x_next - x
      dy = y_next - y
      angle = math.degrees(math.atan2(-dy, dx)) - 30

      # Skala Ukuran Hati (scale = 14)
      scale = 14
      screen_x = int(WIDTH / 2 + x * scale)
      screen_y = int(HEIGHT / 2 + y * scale)

      # Render Teks & Glow
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

    # WAJIB untuk Pygbag/Browser:
    await asyncio.sleep(0)

  pygame.quit()


# 4. Jalankan Fungsi Utama
asyncio.run(main())