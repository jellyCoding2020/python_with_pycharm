import pygame
import sys
import math

# Pygame 초기화
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 화면 크기 설정
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("미국 국기")

# 국기 그리기 함수
def draw_us_flag(screen):
    # 하얀 배경
    screen.fill(WHITE)

    # 파란색 영역
    blue_height = screen_height * 7 / 13
    pygame.draw.rect(screen, BLUE, (0, 0, screen_width * 2 / 5, blue_height))

    # 빨간색 가로줄
    red_height = screen_height / 13
    for i in range(0, 7):
        pygame.draw.rect(screen, RED, (0, i * red_height, screen_width, red_height))

    # 별 그리기
    star_size = int(blue_height * 0.76 / 6)  # 별 크기 계산
    gap = 2 * star_size
    start_x = screen_width * 2 / 5
    start_y = red_height
    for row in range(9):
        for col in range(6):
            x = start_x + col * gap + (row % 2) * gap / 2
            y = start_y + row * gap / 2
            draw_star(screen, (x, y), star_size)

def draw_star(screen, center, size):
    x, y = center
    outer_radius = size / 2
    inner_radius = outer_radius / 2
    points = 5
    angle = 4 * math.pi / points
    star_points = []
    for i in range(2 * points):
        radius = inner_radius if i % 2 == 0 else outer_radius
        star_points.append((x + radius * math.cos(i * angle), y - radius * math.sin(i * angle)))
    pygame.draw.polygon(screen, WHITE, star_points)

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 국기 그리기 함수 호출
    draw_us_flag(screen)

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
