import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
         self.kill()
         if self.radius <= ASTEROID_MIN_RADIUS:
              return
         else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_vec_1 = self.velocity.rotate(angle)
            new_vec_2 = self.velocity.rotate(-angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS

            ast_1 = Asteroid(self.position.x, self.position.y, new_rad)
            ast_2 = Asteroid(self.position.x, self.position.y, new_rad)
            
            ast_1.velocity = new_vec_1 *1.2
            ast_2.velocity = new_vec_2 *1.2
              
