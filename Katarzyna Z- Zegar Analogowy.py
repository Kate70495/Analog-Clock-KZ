import pygame
import pygame.gfxdraw
import math
import time
import calendar

WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 200

# Kolory
BG_COLOR   = (6, 15, 26)
HOUR_COLOR = (108, 110, 117)
MIN_COLOR  = (147, 153, 173)
SEC_COLOR  = (255, 0, 0)
RING_COLOR = (180, 180, 180)
CENTER_COLOR = (240, 240, 240)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Katarzyna Z - Zegar Analogowy")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 25, bold=True)

def draw_clock():
    screen.fill(BG_COLOR)

    # Tarcza zegara
    pygame.gfxdraw.filled_circle(screen, CENTER[0], CENTER[1], RADIUS, (0, 0, 0))
    for r in range(RADIUS, RADIUS-4, -1):
         pygame.gfxdraw.aacircle(screen, CENTER[0], CENTER[1], r, RING_COLOR)

    # Dodatkowy okrąg
    pygame.gfxdraw.aacircle(screen, CENTER[0], CENTER[1], RADIUS-185, (100, 100, 100))


    # Kreski godzinowe
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = CENTER[0] + (RADIUS - 10) * math.cos(angle)
        y1 = CENTER[1] + (RADIUS - 10) * math.sin(angle)
        x2 = CENTER[0] + (RADIUS - 30) * math.cos(angle)
        y2 = CENTER[1] + (RADIUS - 30) * math.sin(angle)
        pygame.draw.line(screen, (200, 200, 200), (x1, y1), (x2, y2), 4)

    # Kreski minutowe
    for i in range(60):
        angle = math.radians(i * 6)
        x1 = CENTER[0] + (RADIUS - 10) * math.cos(angle)
        y1 = CENTER[1] + (RADIUS - 10) * math.sin(angle)
        x2 = CENTER[0] + (RADIUS - 20) * math.cos(angle)
        y2 = CENTER[1] + (RADIUS - 20) * math.sin(angle)
        pygame.draw.line(screen, (200, 200, 200), (x1, y1), (x2, y2), 1)

    # Cyfry
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = CENTER[0] + (RADIUS - 55) * math.cos(angle)
        y = CENTER[1] + (RADIUS - 55) * math.sin(angle)
        text = font.render(str(i), True, (240, 240, 240))
        rect = text.get_rect(center=(x, y))
        screen.blit(text, rect)

def draw_hands():
    now = time.localtime()
    hours = now.tm_hour % 12
    minutes = now.tm_min
    seconds = now.tm_sec

    # Kąty wskazówek
    sec_angle = math.radians(6 * seconds - 90)
    min_angle = math.radians(6 * minutes - 90)
    hour_angle = math.radians(30 * hours + minutes / 2 - 90)

    # Wskazówka godzinowa
    hx = CENTER[0] + 100 * math.cos(hour_angle)
    hy = CENTER[1] + 100 * math.sin(hour_angle)
    pygame.draw.line(screen, HOUR_COLOR, CENTER, (hx, hy), 8)

    # Wskazówka minutowa
    mx = CENTER[0] + 140 * math.cos(min_angle)
    my = CENTER[1] + 140 * math.sin(min_angle)
    pygame.draw.line(screen, MIN_COLOR, CENTER, (mx, my), 5)

    # Wskazówka sekundowa
    sx = CENTER[0] + 160 * math.cos(sec_angle)
    sy = CENTER[1] + 160 * math.sin(sec_angle)
    pygame.draw.line(screen, SEC_COLOR, CENTER, (sx, sy), 2)

    # Środek zegara
    pygame.gfxdraw.filled_circle(screen, CENTER[0], CENTER[1], 10, CENTER_COLOR)
    pygame.gfxdraw.aacircle(screen, CENTER[0], CENTER[1], 10, CENTER_COLOR)

# Zegar cyfrowy
def draw_date_boxes_diagonal_horizontal():
    now = time.localtime()
    day_of_week = calendar.day_abbr[now.tm_wday]  # np. 'Frid'
    day = now.tm_mday                               # np. 8
    month = calendar.month_abbr[now.tm_mon]        # np. 'AUG'
    year = now.tm_year                              # np. 2025

    # Czcionka
    small_font = pygame.font.SysFont("Times New Roman", 15, bold=True)

    # Kolory
    box_color = (30, 30, 30)
    border_color = (80, 80, 80)
    text_color = (150, 150, 150)

    # Prostokąty
    box_width, box_height = 70, 25
    spacing = 250  # odstęp między prostokątami

    x_start = CENTER[0] - 195
    y_start = CENTER[1] + 160

    # Co wyświetlamy
    data_list = [f"{day_of_week} {day}", f"{month} {year}"]

    for i, data in enumerate(data_list):
        x = x_start + i * (box_width + spacing)
        y = y_start 
        rect = pygame.Rect(x, y, box_width, box_height)
        pygame.gfxdraw.box(screen, rect, box_color)          # wypełnienie
        pygame.gfxdraw.rectangle(screen, rect, border_color) # obwódka

        # Tekst na środku prostokąta
        text_surface = small_font.render(data, True, text_color)
        screen.blit(text_surface, text_surface.get_rect(center=rect.center))

# Inicjały
def draw_logo_center():
    # Czcionka
    logo_font = pygame.font.SysFont("Edwardian Script ITC", 47, italic=True)

    # Tekst
    logo_text = "K Z"
    
    # Kolor
    text_color = (240, 240, 240)  # biały

    # Pozycja
    logo_pos = (CENTER[0], CENTER[1] + 40)  


    # Wyświetlenie
    text_surface = logo_font.render(logo_text, True, text_color)

    scale_x = 1.5  # rozciągnięcie poziome 150%
    scale_y = 1.2  # rozciągnięcie pionowe 120%
    new_size = (int(text_surface.get_width() * scale_x),
                int(text_surface.get_height() * scale_y))
    text_surface = pygame.transform.smoothscale(text_surface, new_size)
    rect = text_surface.get_rect(center=(CENTER[0], CENTER[1]+40))
    screen.blit(text_surface, text_surface.get_rect(center=logo_pos))





# Pętla główna
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_clock()
    draw_logo_center()
    draw_hands()
    draw_date_boxes_diagonal_horizontal()

    pygame.display.flip()
    clock.tick(1)

pygame.quit()
