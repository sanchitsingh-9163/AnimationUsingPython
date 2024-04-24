
import tkinter as tk
import cv2
class matrix:
    def __init__(self, location,width,length):
        self.location = location
        self.width = width
        self.length = length

    def img_matrix(self):
        image = cv2.imread(self.location)
        image = cv2.resize(image, (self.width,self.length))
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresholded = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
        stick_figure_data=[]
        for y in range(thresholded.shape[0]):
            row = []
            for x in range(thresholded.shape[1]):
                # If the pixel is black (part of the stick figure), set the value in the row to 1, else 0
                row.append(int(thresholded[y, x] == 0))
            stick_figure_data.append(row)
        return stick_figure_data

def create_pixel_grid(rows, cols, pixel_size, figure_data):
    root = tk.Tk()
    root.title("Pixel Grid")

    # Calculate the total size of the grid
    width = cols * pixel_size
    height = rows * pixel_size

    # Create a canvas to display the grid
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    # Draw the grid and fill in the figure data
    for row in range(rows):
        for col in range(cols):
            x1 = col * pixel_size
            y1 = row * pixel_size
            x2 = x1 + pixel_size
            y2 = y1 + pixel_size
            color = "black" if figure_data[row][col] else "white"
            # Change from create_rectangle to create_oval for circular pixels
            canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")

    return root, canvas  # Return both root and canvas for animation

width = 16
length = 12
fig1 = matrix('C:\\Users\\sanch\\OneDrive\\Desktop\\resize1\\frame1.png',width,length)
fig2 = matrix('C:\\Users\\sanch\\OneDrive\\Desktop\\resize1\\frame2.png',width,length)
fig3 = matrix('C:\\Users\\sanch\\OneDrive\\Desktop\\resize1\\frame3.png',width,length)
fig4 = matrix('C:\\Users\\sanch\\OneDrive\\Desktop\\resize1\\frame4.png',width,length)
fig5 = matrix('C:\\Users\\sanch\\OneDrive\\Desktop\\resize1\\frame5.png',width,length)
fig6 = matrix('C:\\Users\\sanch\\OneDrive\\Desktop\\resize1\\frame6.png',width,length)




figure_data_list = [fig1.img_matrix(), fig2.img_matrix(), fig3.img_matrix(), fig4.img_matrix(), fig5.img_matrix(), fig6.img_matrix()]
current_figure_index = 0
pix_sz=10
def update_figure():
    global current_figure_index, root, canvas
    current_figure_data = figure_data_list[current_figure_index]
    canvas.delete("all")
    for row in range(len(fig1.img_matrix())):
        for col in range(len(fig1.img_matrix()[0])):
            x1 = col * pix_sz
            y1 = row * pix_sz
            x2 = x1 + pix_sz
            y2 = y1 + pix_sz
            color = "black" if current_figure_data[row][col] else "white"
            canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black" if current_figure_data[row][col] else "white")
    current_figure_index = (current_figure_index + 1) % len(figure_data_list)
    root.after(42, update_figure)

root, canvas = create_pixel_grid(rows=len(fig1.img_matrix()), cols=len(fig1.img_matrix()[0]), pixel_size=pix_sz, figure_data=fig1.img_matrix())
update_figure()
root.mainloop()

