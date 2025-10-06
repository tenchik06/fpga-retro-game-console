import pygame
import numpy as np

class SpriteRenderer:
    def __init__(self):
        self.sprites = {}
        self.load_sprites()
    
    def load_sprites(self):
        # Создаем тестовые спрайты
        # Спрайт 1: Квадрат 16x16
        sprite1 = np.zeros((16, 16), dtype=int)
        for i in range(16):
            for j in range(16):
                if 4 <= i < 12 and 4 <= j < 12:
                    sprite1[i, j] = 1
        
        # Спрайт 2: Круг
        sprite2 = np.zeros((16, 16), dtype=int)
        center = (8, 8)
        for i in range(16):
            for j in range(16):
                if (i-8)**2 + (j-8)**2 <= 25:  # радиус 5
                    sprite2[i, j] = 1
        
        self.sprites['square'] = sprite1
        self.sprites['circle'] = sprite2
        self.sprites['dino'] = self.create_dino_sprite()
    
    def create_dino_sprite(self):
        dino = [
            [0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],
            [0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],
            [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0]
        ]
        return np.array(dino)
    
    def draw_sprite(self, surface, x, y, sprite_name, color=(255, 0, 0)):
        sprite = self.sprites.get(sprite_name)
        if sprite is not None:
            for i in range(sprite.shape[0]):
                for j in range(sprite.shape[1]):
                    if sprite[i, j]:
                        surface.set_at((x + j, y + i), color)

class VGASimulatorEnhanced:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Retro Console - Sprite Demo")
        self.clock = pygame.time.Clock()
        self.sprite_renderer = SpriteRenderer()
        self.sprite_x = 100
        self.sprite_y = 150
        
    def draw_text(self, x, y, text, color=(255, 255, 255)):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
        
    def draw_vector_cube(self, x, y, size, angle=0, color=(0, 255, 0)):
        # Вращающийся куб
        points = []
        for i in range(4):
            px = x + size * np.cos(angle + i * np.pi/2)
            py = y + size * np.sin(angle + i * np.pi/2)
            points.append((int(px), int(py)))
        
        # Замыкаем контур
        points.append(points[0])
        
        # Рисуем линии
        for i in range(len(points)-1):
            pygame.draw.line(self.screen, color, points[i], points[i+1], 2)
            
    def update(self, keys):
        self.screen.fill((0, 0, 0))
        
        # Текст
        self.draw_text(50, 50, "Retro Console - Sprite Demo")
        self.draw_text(50, 90, "Use ARROWS to move sprite")
        
        # Спрайты
        self.sprite_renderer.draw_sprite(self.screen, self.sprite_x, self.sprite_y, 'dino', (255, 0, 0))
        self.sprite_renderer.draw_sprite(self.screen, 300, 200, 'square', (0, 255, 255))
        self.sprite_renderer.draw_sprite(self.screen, 400, 250, 'circle', (255, 255, 0))
        
        # Управление спрайтом
        if keys[pygame.K_LEFT]:
            self.sprite_x -= 2
        if keys[pygame.K_RIGHT]:
            self.sprite_x += 2
        if keys[pygame.K_UP]:
            self.sprite_y -= 2
        if keys[pygame.K_DOWN]:
            self.sprite_y += 2
            
        # Вращающийся куб
        import time
        angle = time.time() * 2  # Автоматическое вращение
        self.draw_vector_cube(500, 150, 30, angle)
        
        pygame.display.flip()
        self.clock.tick(60)

def main():
    simulator = VGASimulatorEnhanced()
    running = True
    
    while running:
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        simulator.update(keys)
        
    pygame.quit()

if __name__ == "__main__":
    main()