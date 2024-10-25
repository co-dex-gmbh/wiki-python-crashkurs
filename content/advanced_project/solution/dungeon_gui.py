import tkinter as tk
from tkinter import messagebox
import random
from typing import Tuple, List
from dataclasses import dataclass
import os
from dungeon_crawler_solution import create_dungeon, move_player

# Dungeon elements
WALL = "█"
FLOOR = " "
PLAYER = "👤" 
MONSTER = "💀"
TREASURE = "💰"
EXIT = "🚪"

class DungeonGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Dungeon Crawler")
        self.cell_size = 50  # Size of each dungeon cell in pixels
        
        # Initialize game state
        self.dungeon = create_dungeon(15, 10)
        self.player_pos = (1, 1)
        
        # Create canvas for dungeon display
        self.canvas = tk.Canvas(
            self, 
            width=len(self.dungeon[0]) * self.cell_size,
            height=len(self.dungeon) * self.cell_size
        )
        self.canvas.pack(pady=10)
        
        # Load images (you'll need to add these image files)
        self.images = {
            'WALL': tk.PhotoImage(file='wall.png'),
            'FLOOR': tk.PhotoImage(file='floor.png'),
            'PLAYER': tk.PhotoImage(file='player.png'),
            'MONSTER': tk.PhotoImage(file='monster.png'),
            'TREASURE': tk.PhotoImage(file='treasure.png'),
            'EXIT': tk.PhotoImage(file='exit.png')
        }
        
        # Bind keyboard events
        self.bind('<Key>', self.handle_keypress)
        
        # Initial draw
        self.draw_dungeon()
        
    def draw_dungeon(self):
        """Draws the current state of the dungeon"""
        self.canvas.delete('all')  # Clear canvas
        
        for y in range(len(self.dungeon)):
            for x in range(len(self.dungeon[0])):
                # Calculate pixel coordinates
                x1 = x * self.cell_size
                y1 = y * self.cell_size
                
                # Draw floor everywhere first
                self.canvas.create_image(
                    x1, y1, 
                    image=self.images['FLOOR'],
                    anchor='nw'
                )
                
                # Draw current cell
                cell = self.dungeon[y][x]
                if cell == WALL:
                    self.canvas.create_image(
                        x1, y1, 
                        image=self.images['WALL'],
                        anchor='nw'
                    )
                elif cell == MONSTER:
                    self.canvas.create_image(
                        x1, y1, 
                        image=self.images['MONSTER'],
                        anchor='nw'
                    )
                elif cell == TREASURE:
                    self.canvas.create_image(
                        x1, y1, 
                        image=self.images['TREASURE'],
                        anchor='nw'
                    )
                elif cell == EXIT:
                    self.canvas.create_image(
                        x1, y1, 
                        image=self.images['EXIT'],
                        anchor='nw'
                    )
                
                # Draw player
                if (x, y) == self.player_pos:
                    self.canvas.create_image(
                        x1, y1, 
                        image=self.images['PLAYER'],
                        anchor='nw'
                    )
    
    def handle_keypress(self, event):
        """Handles keyboard input"""
        direction_map = {
            'w': 'w', 'W': 'w',
            's': 's', 'S': 's',
            'a': 'a', 'A': 'a',
            'd': 'd', 'D': 'd'
        }
        
        if event.char in direction_map:
            new_pos, message = move_player(
                self.dungeon, 
                self.player_pos, 
                direction_map[event.char]
            )
            
            self.player_pos = new_pos
            self.draw_dungeon()
            
            if message == "EXIT":
                messagebox.showinfo(
                    "Congratulations!", 
                    "You escaped the dungeon!"
                )
                self.quit()
            elif message:
                messagebox.showinfo("Event", message)

def main():
    app = DungeonGUI()
    app.mainloop()

if __name__ == "__main__":
    main()