

# Stick Figure Animation

This Python script creates a simple animation of stick figures using the tkinter and OpenCV libraries. Let's break down how it works:

## 1. Initialization

The script defines a `matrix` class that represents an image as a binary matrix of pixels. It also includes a function `create_pixel_grid` to create a pixel grid using tkinter.

## 2. Loading and Processing Images

The `matrix` class loads an image using OpenCV, resizes it, converts it to grayscale, and then applies a binary threshold to obtain a binary matrix representing the stick figure.

## 3. Displaying the Animation

The script creates a tkinter window and displays the stick figure animation by updating the pixel grid with each frame of the stick figure images.

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

## 7. License

This project is licensed under the MIT License. You can find more details in the [LICENSE](LICENSE) file.

---

This README provides an overview of the script's functionality, customization options, usage instructions, and contribution guidelines. Feel free to customize it further to suit your project's requirements!
