import tkinter as tk

class PixelArtEditor:
    def __init__(self, master, width, height, pixel_size):
        self.master = master
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.canvas = tk.Canvas(master, width=width*pixel_size, height=height*pixel_size, bg="white")
        self.canvas.pack()

        # Draw circles
        for i in range(width):
            for j in range(height):
                x = i * self.pixel_size + self.pixel_size // 2
                y = j * self.pixel_size + self.pixel_size // 2
                radius = self.pixel_size // 2
                self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="white")

        # Draw the stickman
        self.x = 6
        self.y = 11
        self.color_sequence = ["black", "red", "black", "red", "black", "red"]
        self.frame_index = 0

        # Start animation
        self.animate()

    def animate(self):
        if self.frame_index < len(self.color_sequence):
            # Draw the current frame of the stickman
            color = self.color_sequence[self.frame_index]
            getattr(self, f"draw_man{self.frame_index + 1}")(self.x, self.y, color)

            # Schedule making each circle white after 2 seconds
            self.master.after(2000, self.make_circles_white)

            # Increment frame index for the next frame
            self.frame_index += 1

            # Schedule the next frame after 2 seconds
            self.master.after(2000, self.animate)

    def make_circles_white(self):
        # Clear the previous frame by making each circle white
        for i in range(self.width):
            for j in range(self.height):
                self.draw_circle(i, j, "white")

    def draw_man1(self, x, y, color):
        # Head
        self.draw_circle(x, y, color)

        # Body
        self.draw_circle(x, y + 1, color)
        self.draw_circle(x, y - 1, color)
        self.draw_circle(x, y - 2, color)

        # Arms
        self.draw_circle(x - 1, y, color)
        self.draw_circle(x + 1, y, color)
        self.draw_circle(x - 2, y, color)
        self.draw_circle(x + 2, y, color)

        # Legs
        self.draw_circle(x - 1, y + 2, color)
        self.draw_circle(x + 1, y + 2, color)
        self.draw_circle(x - 2, y + 3, color)
        self.draw_circle(x + 2, y + 3, color)

    # Define draw_man2, draw_man3, draw_man4, draw_man5, draw_man6 similarly

    def draw_circle(self, x, y, color):
        cx = x * self.pixel_size + self.pixel_size // 2
        cy = y * self.pixel_size + self.pixel_size // 2
        radius = self.pixel_size * 2 // 4
        self.canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, fill=color, tags="man")

def main():
    root = tk.Tk()
    root.title("Pixel Art Editor")
    width = 20  # Number of circles horizontally
    height = 20  # Number of circles vertically
    pixel_size = 20  # Size of each circle
    editor = PixelArtEditor(root, width, height, pixel_size)
    root.mainloop()

if __name__ == "__main__":
    main()

