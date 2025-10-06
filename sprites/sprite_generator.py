def create_sprite_pattern(width=16, height=16):
    """Создает простой спрайт в виде матрицы"""
    sprite = []
    
    # Пример: простой квадрат с узором
    for y in range(height):
        row = []
        for x in range(width):
            # Создаем простой узор - шахматная доска
            if (x // 4 + y // 4) % 2 == 0:
                row.append(1)  # Пиксель включен
            else:
                row.append(0)  # Пиксель выключен
        sprite.append(row)
    
    return sprite

def sprite_to_hex(sprite, filename):
    """Конвертирует спрайт в hex формат"""
    with open(filename, 'w') as f:
        for y in range(0, len(sprite), 2):
            for x in range(0, len(sprite[0]), 8):
                byte1 = 0
                byte2 = 0
                for bit in range(8):
                    if x + bit < len(sprite[0]):
                        if y < len(sprite):
                            byte1 |= sprite[y][x + bit] << (7 - bit)
                        if y + 1 < len(sprite):
                            byte2 |= sprite[y + 1][x + bit] << (7 - bit)
                
                f.write(f"{byte1:02X} {byte2:02X}\n")
            f.write("\n")

# Создаем и сохраняем спрайт
sprite = create_sprite_pattern()
sprite_to_hex(sprite, "sprites/generated_sprite.hex")

# Также создаем спрайт динозаврика
def create_dino_sprite():
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
    return dino

dino_sprite = create_dino_sprite()
sprite_to_hex(dino_sprite, "sprites/dino_sprite.hex")