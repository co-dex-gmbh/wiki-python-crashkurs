from PIL import Image, ImageDraw
import os

def create_sprite(color, filename, size=50):
    """Create a simple sprite with the given color"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw different shapes based on the sprite type
    if filename == 'wall.png':
        # Solid brick pattern
        draw.rectangle([0, 0, size-1, size-1], fill='#8B4513')
        # Brick pattern
        for y in range(0, size, 10):
            draw.line([(0, y), (size, y)], fill='#654321', width=1)
        for x in range(0, size, 10):
            draw.line([(x, 0), (x, size)], fill='#654321', width=1)
            
    elif filename == 'floor.png':
        # Checkered pattern
        draw.rectangle([0, 0, size-1, size-1], fill='#696969')
        for y in range(0, size, 10):
            for x in range(0, size, 10):
                if (x + y) % 20 == 0:
                    draw.rectangle([x, y, x+9, y+9], fill='#808080')
                    
    elif filename == 'player.png':
        # Simple character
        draw.ellipse([10, 10, size-10, size-10], fill='#4169E1')
        # Add eyes
        draw.ellipse([20, 20, 25, 25], fill='white')
        draw.ellipse([35, 20, 40, 25], fill='white')
        
    elif filename == 'monster.png':
        # Scary monster
        draw.ellipse([10, 10, size-10, size-10], fill='#DC143C')
        # Add eyes
        draw.ellipse([15, 15, 25, 25], fill='yellow')
        draw.ellipse([35, 15, 45, 25], fill='yellow')
        
    elif filename == 'treasure.png':
        # Treasure chest
        draw.rectangle([5, 15, size-5, size-15], fill='#DAA520')
        draw.rectangle([20, 5, 30, 15], fill='#B8860B')  # Lock
        
    elif filename == 'exit.png':
        # Door
        draw.rectangle([5, 0, size-5, size-1], fill='#8B4513')
        draw.ellipse([35, 25, 45, 35], fill='#FFD700')  # Doorknob

    # Save the sprite
    img.save(filename)

def create_all_sprites():
    """Create all necessary sprites for the game"""
    sprites = {
        'wall.png': '#8B4513',    # Saddle Brown
        'floor.png': '#696969',   # Dim Gray
        'player.png': '#4169E1',  # Royal Blue
        'monster.png': '#DC143C', # Crimson
        'treasure.png': '#DAA520', # Goldenrod
        'exit.png': '#8B4513'     # Saddle Brown
    }
    
    for filename, color in sprites.items():
        create_sprite(color, filename)
        print(f"Created {filename}")

if __name__ == "__main__":
    create_all_sprites()