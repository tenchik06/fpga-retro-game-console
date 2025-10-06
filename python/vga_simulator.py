import pygame
import numpy as np

class VGASimulator:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.buffer = np.zeros((height, width, 3), dtype=np.uint8)
        
    def set_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y, x] = color
            
    def draw_text(self, x, y, text, color=(255, 255, 255)):
        # Простая имитация текстового вывода
        font = pygame.font.Font(None, 24)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
        
    def draw_sprite(self, x, y, sprite_data):
        # Отрисовка спрайта 16x16
        for sy in range(16):
            for sx in range(16):
                if sprite_data[sy * 16 + sx]:
                    self.set_pixel(x + sx, y + sy, (255, 0, 0))
                    
    def draw_vector_shape(self, points, color=(0, 255, 0)):
        # Отрисовка векторной формы
        for i in range(len(points) - 1):
            pygame.draw.line(self.screen, color, points[i], points[i + 1], 1)
                    
    def update(self):
        self.screen.fill((0, 0, 0))
        
        # Создаем RGB данные из буфера
        surf = pygame.surfarray.make_surface(self.buffer)
        self.screen.blit(surf, (0, 0))
        
        # Демонстрационные элементы
        self.draw_text(50, 50, "Retro Console Demo")
        
        # Простой спрайт
        sprite = [1 if i % 3 == 0 else 0 for i in range(256)]
        self.draw_sprite(100, 100, sprite)
        
        # Векторный куб
        cube_points = [
            (200, 200), (250, 200), (250, 250), (200, 250), (200, 200),
            (220, 180), (270, 180), (270, 230), (220, 230), (220, 180)
        ]
        self.draw_vector_shape(cube_points)
        
        pygame.display.flip()
        self.clock.tick(60)

def main():
    simulator = VGASimulator()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        simulator.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()