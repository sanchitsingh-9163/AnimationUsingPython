import tkinter as tk

class PixelArtEditor:
    def _init_(self, master, width, height, pixel_size):
        self.master = master
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.canvas = tk.Canvas(master, width=width*pixel_size, height=height*pixel_size, bg="white")
        self.canvas.pack()

        # Draw grid lines
        for i in range(1, width):
            self.canvas.create_line(i * self.pixel_size, 0, i * self.pixel_size, height * self.pixel_size, fill="gray")
        for j in range(1, height):
            self.canvas.create_line(0, j * self.pixel_size, width * self.pixel_size, j * self.pixel_size, fill="gray")

        # Draw man
        # self.draw_man()
    #
    # def draw_man(self):
    #     # Head
    #     self.canvas.create_oval(5 * self.pixel_size, 2 * self.pixel_size, 7 * self.pixel_size, 4 * self.pixel_size, fill="black")
    #
    #     # Body
    #     self.canvas.create_line(6 * self.pixel_size, 4 * self.pixel_size, 6 * self.pixel_size, 9 * self.pixel_size, fill="black")
    #
    #     # Arms
    #     self.canvas.create_line(3 * self.pixel_size, 6 * self.pixel_size, 6 * self.pixel_size, 6 * self.pixel_size, fill="black")
    #     self.canvas.create_line(9 * self.pixel_size, 6 * self.pixel_size, 6 * self.pixel_size, 6 * self.pixel_size, fill="black")
    #
    #     # Legs
    #     self.canvas.create_line(6 * self.pixel_size, 9 * self.pixel_size, 4 * self.pixel_size, 12 * self.pixel_size, fill="black")
    #     self.canvas.create_line(6 * self.pixel_size, 9 * self.pixel_size, 8 * self.pixel_size, 12 * self.pixel_size, fill="black")

def main():
    root = tk.Tk()
    root.title("Pixel Art Editor")
    width = 20  # Number of pixels horizontally
    height = 20  # Number of pixels vertically
    pixel_size = 20  # Size of each pixel
    editor = PixelArtEditor(root, width, height, pixel_size)
    root.mainloop()

if __name__ == "_main_":
    main()