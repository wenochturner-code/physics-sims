import numpy as np
import pygame
import sys

class Ball:
    def __init__(self, pos, velo, mass, radius, color):
        self.pos = pos
        self.velo = velo
        self.mass = mass
        self.radius = radius
        self.color = color
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)
        
    def collision(self, other):
        distance = np.sqrt((self.pos[0] - other.pos[0])**2 + (self.pos[1] - other.pos[1])**2)
        if distance <= self.radius + other.radius:
            vf = (self.mass * self.velo + other.mass * other.velo) / (self.mass + other.mass)
            self.velo = vf
            other.velo = vf
            
        if self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= 1280:
            self.velo[0] *= -1
            
        if other.pos[0] - other.radius <= 0 or other.pos[0] + other.radius >= 1280:
            other.velo[0] *= -1


ball1 = Ball(
    pos = np.array([256.0, 360.0]),
    velo = np.array([500,0]),
    mass = 2,
    radius = 15,
    color = (30, 144, 255),
    )

ball2 = Ball(
    pos = np.array([1024.0, 360.0]),
    velo = np.array([-35,0]),
    mass = 3,
    radius = 25,
    color = (30, 144, 255),
    )

        
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)
title = font.render("Perfectly Inelastic Collision", True, "black", "white")
title_rect = title.get_rect()
title_rect.center = (1280 // 2, 120)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    dt = clock.tick(60) / 1000
    
    screen.fill("white")
    
    ball1.draw(screen)
    ball1.pos += ball1.velo * dt
    
    ball2.draw(screen)
    ball2.pos += ball2.velo * dt
    
    ball1.collision(ball2)
    
    text1 = font.render(f"Mass 1: {ball1.mass} kg  Vel 1: {ball1.velo[0]:.1f} px/s", True, "black")
    text2 = font.render(f"Mass 2: {ball2.mass} kg Vel 2: {ball2.velo[0]:.1f} px/s", True, "black")
    screen.blit(text1, (50, 620))
    screen.blit(text2, (50, 660))
    
    screen.blit(title, title_rect)
    
    pygame.display.flip()
pygame.quit()
