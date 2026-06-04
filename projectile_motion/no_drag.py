import numpy as np
import pygame

SCALE = 10
G = 9.81

class Projectile:
    def __init__(self, theta, pos, velo):
        self.theta = theta
        self.initial_pos = pos.copy()
        self.initial_velo = velo
        self.pos = pos.copy()
        self.vx = velo * np.cos(theta)
        self.vy = velo * np.sin(theta)

    def reset(self):
        self.pos = self.initial_pos.copy()
        self.vx = self.initial_velo * np.cos(self.theta)
        self.vy = self.initial_velo * np.sin(self.theta)
    
    def motion(self, dt):
        self.vy -= G * SCALE * dt
        self.pos[0] += self.vx * dt
        self.pos[1] += self.vy * dt
        if self.pos[1] <= 0:
            self.reset()
    
    def draw(self, surface):
         draw_pos = (self.pos[0], 720 - self.pos[1])
         pygame.draw.circle(surface, (30, 144, 255), draw_pos, 5)
        
        
projectile = Projectile(
    theta=np.radians(45),
    pos=np.array([100.0, 200.0]),
    velo=300
)
    

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)
title = font.render("Projectile Motion - no drag", True, "black", "white")
title_rect = title.get_rect()
title_rect.center = (1280 // 2, 120)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    dt = clock.tick(60) / 1000
    
    screen.fill("white")
    projectile.draw(screen)
    projectile.motion(dt)
    
    text1 = font.render(f"X: {projectile.pos[0]:.1f} px", True, "black")
    text2 = font.render(f"Y: {projectile.pos[1]:.1f} px", True, "black")
    text3 = font.render(f"Velo: {np.sqrt(projectile.vx**2 + projectile.vy**2):.1f} px/s", True, "black")
    
    screen.blit(text1, (50, 580))
    screen.blit(text2, (50, 620))
    screen.blit(text3, (50, 660))
    
    screen.blit(title, title_rect)
    
    pygame.display.flip()
pygame.quit()
