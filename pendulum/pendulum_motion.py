import numpy as np
import pygame

G = 9.81
SCALE = 100

class Pendulum:
    def __init__(self, length, theta, omega):
        self.length = length
        self.theta = theta
        self.omega = omega
    
    def motion(self, dt):
        self.omega += -(G/(self.length/SCALE))*np.sin(self.theta)* dt
        self.theta += self.omega * dt
        
    def draw(self, surface):
        pivot = (1280//2, 720//2)
        end_x = 1280//2 + self.length * np.sin(self.theta)
        end_y = 720//2 + self.length * np.cos(self.theta)
        end_pos = (end_x, end_y)
        pygame.draw.line(surface, (0, 0, 0), pivot, end_pos, 2)
        pygame.draw.circle(surface, (30, 144, 255), end_pos, 20)
        
pendulum = Pendulum(
    length = 200,
    theta = (np.pi/3),
    omega = 0,
    )


        
        
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)
title = font.render("Pendulum Motion", True, "black", "white")
title_rect = title.get_rect()
title_rect.center = (1280 // 2, 120)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    dt = clock.tick(60) / 1000
    
    screen.fill("white")
    pendulum.draw(screen)
    pendulum.motion(dt)
    
    text1 = font.render(f"Theta: {np.degrees(pendulum.theta):.1f}°", True, "black")
    text2 = font.render(f"Angular Vel: {pendulum.omega:.2f} rad/s", True, "black")
    text3 = font.render(f"Period: {2*np.pi*np.sqrt(pendulum.length/SCALE/G):.2f} s", True, "black")
    screen.blit(text1, (50, 580))
    screen.blit(text2, (50, 620))
    screen.blit(text3, (50, 660))
    
    screen.blit(title, title_rect)
    
    pygame.display.flip()
pygame.quit()