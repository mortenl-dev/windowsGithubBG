import ctypes
import os

def set_wallpaper(image_path):
    # Check if the file exists
    if not os.path.exists(image_path):
        print("The specified image file does not exist.")
        return

    # Convert the file path to an absolute path
    abs_path = os.path.abspath(image_path)

    # SPI_SETDESKWALLPAPER = 20
    # The third parameter is the path to the image file
    # The fourth parameter specifies how the wallpaper should be changed
    result = ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)

    # Check if the function call was successful
    if result:
        print("Wallpaper successfully changed!")
    else:
        print("Failed to change the wallpaper.")

# Path to the image file you want to set as wallpaper
image_file = "C:\\Users\\morte\\Pictures\\Screenshots\\Screenshot (120).png" # needs to be \\

# Change the wallpaper
set_wallpaper(image_file)
