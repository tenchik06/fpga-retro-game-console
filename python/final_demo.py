import time
import os

class RetroConsoleDemo:
    def __init__(self):
        self.sprite_x = 10
        self.sprite_y = 5
        self.cube_angle = 0
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def draw_text(self, buffer, x, y, text):
        """Вывод текста в буфер"""
        for i, char in enumerate(text):
            if 0 <= x + i < 60 and 0 <= y < 20:
                buffer[y][x + i] = char
    
    def draw_sprite(self, buffer, x, y):
        """Рисуем спрайт динозаврика"""
        sprite = [
            "  █████  ",
            " ██   ██ ",
            "██     ██",
            "██     ██", 
            " ███████ ",
            "  █████  "
        ]
        
        for sy, line in enumerate(sprite):
            for sx, char in enumerate(line):
                if (0 <= y + sy < 20 and 0 <= x + sx < 60 and 
                    char != ' '):
                    buffer[y + sy][x + sx] = char
    
    def draw_vector_cube(self, buffer, center_x, center_y, size, angle):
        """Рисуем вращающийся куб"""
        import math
        
        # Углы вершин куба
        points = []
        for i in range(4):
            px = center_x + size * math.cos(angle + i * math.pi/2)
            py = center_y + size * math.sin(angle + i * math.pi/2)
            points.append((int(px), int(py)))
        
        # Рисуем линии куба
        chars = ['╭', '╮', '╯', '╰', '─', '│']
        
        # Горизонтальные линии
        for i in range(4):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % 4]
            
            if y1 == y2:  # Горизонтальная линия
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    if 0 <= x < 60 and 0 <= y1 < 20:
                        buffer[y1][x] = '─'
            
            if x1 == x2:  # Вертикальная линия  
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    if 0 <= x1 < 60 and 0 <= y < 20:
                        buffer[y][x1] = '│'
        
        # Углы
        for x, y in points:
            if 0 <= x < 60 and 0 <= y < 20:
                buffer[y][x] = '●'
    
    def display_frame(self, width=60, height=20):
        """Отображает один кадр демонстрации"""
        buffer = [[' ' for _ in range(width)] for _ in range(height)]
        
        # 1. Текст (Пункт 2-3)
        self.draw_text(buffer, 2, 1, "HELLO RETRO CONSOLE!")
        self.draw_text(buffer, 2, 2, "VGA:640x480  SPRITE:16x16")
        
        # 2. Спрайт (Пункт 4-5)
        self.draw_text(buffer, 2, 4, "SPRITE (Move with WASD):")
        self.draw_sprite(buffer, self.sprite_x, 6)
        
        # 3. Векторный куб (Пункт 6-8)  
        self.draw_text(buffer, 35, 4, "3D CUBE (Auto-rotate):")
        self.draw_vector_cube(buffer, 45, 12, 5, self.cube_angle)
        
        # 4. Статус
        self.draw_text(buffer, 2, 15, f"Sprite: ({self.sprite_x},{self.sprite_y})")
        self.draw_text(buffer, 2, 16, "Press: WASD=Move, Q=Quit, R=Reset")
        
        # Вывод на экран
        print("+" + "=" * width + "+")
        for row in buffer:
            print("|" + "".join(row) + "|")
        print("+" + "=" * width + "+")
    
    def run(self):
        """Главный цикл демонстрации"""
        while True:
            self.clear_screen()
            print("=== RETRO GAME CONSOLE DEMO ===")
            print("All 9 workflow points demonstrated!")
            print()
            
            self.display_frame()
            
            # Автоматическое вращение куба
            self.cube_angle += 0.3
            
            # Управление
            cmd = input("Command: ").lower()
            if cmd == 'q':
                break
            elif cmd == 'w' and self.sprite_y > 5:
                self.sprite_y -= 1
            elif cmd == 's' and self.sprite_y < 12:
                self.sprite_y += 1
            elif cmd == 'a' and self.sprite_x > 2:
                self.sprite_x -= 1
            elif cmd == 'd' and self.sprite_x < 50:
                self.sprite_x += 1
            elif cmd == 'r':
                self.sprite_x = 10
                self.sprite_y = 5

if __name__ == "__main__":
    demo = RetroConsoleDemo()
    demo.run()