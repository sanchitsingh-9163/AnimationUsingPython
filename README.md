

# Stick Figure Animation

This Python script creates a simple animation of stick figures using the tkinter and OpenCV libraries. Let's break down how it works:

## 1. Initialization

The script defines a `matrix` class that represents an image as a binary matrix of pixels. It also includes a function `create_pixel_grid` to create a pixel grid using tkinter.

## 2. Loading and Processing Images

The `matrix` class loads an image using OpenCV, resizes it, converts it to grayscale, and then applies a binary threshold to obtain a binary matrix representing the stick figure.

## 3. Displaying the Animation
The script uses tkinter to create a pixel grid and display the stick figure animation. While tkinter provides a simple way to create graphical user interfaces in Python, it may not be the most efficient option for real-time animation.

Performance Comparison
In some cases, tkinter's performance may be slower compared to other libraries like matplotlib, especially when dealing with complex animations or large datasets. Consider using matplotlib's animation functionalities for improved performance if tkinter's performance becomes a bottleneck for your application.

## 4. Customization

- **Image Size**: You can adjust the `width` and `length` parameters to change the size of the stick figure images.
- **Animation Speed**: The animation speed can be modified by adjusting the delay in the `update_figure` function.
- **Pixel Size**: The size of each pixel in the grid can be customized by changing the `pix_sz` parameter.
- **Pixel Appearance**: You can change the appearance of the pixels (e.g., shape, color) by modifying the canvas drawing methods in the `create_pixel_grid` and `update_figure` functions.

## 5. Usage

1. **Installation**: Install the required libraries (OpenCV and tkinter) using pip.
2. **Setup**: Place your stick figure images in a folder.
3. **Execution**: Update the file paths in the Python script to point to your image folder and run the script.

## 6. Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
---
You can adjust the resolution on by your own easily just go and change width and length parameter in the code

Final Result (Resolution 300 x 534)

https://github.com/sanchitsingh-9163/AnimationUsingPython/assets/72063118/c245fdc4-62b9-45d9-b4bd-f0038467e1b8
