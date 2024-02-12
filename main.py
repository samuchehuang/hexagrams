import pygame
import sys
import math

# 初始化Pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
MARS_COLOR = (255, 100, 50)  # 新增火星的颜色

# 设置屏幕尺寸
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("星系模型")

# 定义太阳、地球、月球和火星的半径和角度
sun_radius = 50
earth_radius = 20
moon_radius = 10
mars_radius = 25  # 新增火星的半径
earth_distance = 150
moon_distance = 50
mars_distance = 250  # 新增火星距离太阳的距离
earth_angle = 0
moon_angle = 0
mars_angle = 0  # 新增火星的初始角度

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 清空屏幕
    screen.fill(BLACK)

    # 画太阳
    pygame.draw.circle(screen, YELLOW, (width // 2, height // 2), sun_radius)

    # 计算地球的位置
    earth_x = width // 2 + earth_distance * math.cos(math.radians(earth_angle))
    earth_y = height // 2 + earth_distance * math.sin(math.radians(earth_angle))

    # 画地球
    pygame.draw.circle(screen, BLUE, (int(earth_x), int(earth_y)), earth_radius)

    # 计算月球的位置
    moon_x = earth_x + moon_distance * math.cos(math.radians(moon_angle))
    moon_y = earth_y + moon_distance * math.sin(math.radians(moon_angle))

    # 画月球
    pygame.draw.circle(screen, RED, (int(moon_x), int(moon_y)), moon_radius)

    # 计算火星的位置
    mars_x = width // 2 + mars_distance * math.cos(math.radians(mars_angle))
    mars_y = height // 2 + mars_distance * math.sin(math.radians(mars_angle))

    # 画火星
    pygame.draw.circle(screen, MARS_COLOR, (int(mars_x), int(mars_y)), mars_radius)

    # 更新角度，模拟旋转
    earth_angle += 1
    moon_angle += 2  # 月球绕地球转速更快一些
    mars_angle += 0.5  # 新增火星的旋转速度

    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(30)
