from PIL import Image, ImageDraw, ImageFont
import os
import sys


def iterate_files(directory):
    """Iterates through all files in a given directory.

    Args:
        directory: The path to the directory.
    """
    try:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                # Process the file
                print(f"File: {filepath}")
                add_filename_title(filepath)
            elif os.path.isdir(filepath):
              # Optionally process subdirectories
              print(f"Directory: {filepath}")
              iterate_files(filepath) # Recursive call to handle nested directories
    except FileNotFoundError:
      print(f"Error: Directory not found: {directory}")
    except Exception as e:
      print(f"An error occurred: {e}")



def add_filename_title(image_path, font_size=20, font_color=(255, 255, 255), title_position=(10, 10)):
    """
    Adds the filename as a title to an image.

    Args:
        image_path (str): The path to the image file.
        font_size (int, optional): The font size of the title. Defaults to 20.
        font_color (tuple, optional): The color of the title text (RGB). Defaults to (255, 255, 255) - white.
        title_position (tuple, optional): The (x, y) coordinates of the title's top-left corner. Defaults to (10, 10).
    """
    try:
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        
        # split filename and path
        filepath, filename = os.path.split(image_path)
        # split name and extension
        name, extension = os.path.splitext(filename)
        # remove unused text in filename
        namefield = name.split("-")
        # remove spaces around name
        staffname = namefield[1].strip()
        
        print(f"fn={filename} , {staffname}")
        if len(staffname) > 20 :
            font_size = 75
            print(f"font_size=75")
        elif len(staffname) > 14 :
            font_size = 100
            print(f"font_size=100")
        else:
            font_size = 150
            print(f"font_size=150")

           

        # Load a default font or specify a path to a font file
        #font_size=150
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Monaco.ttf", font_size)  # Requires the font file in the same directory, or specify full path
        except IOError:
            font = ImageFont.load_default(font_size)


        new_image_path = filepath +"/" + staffname + "_updated.png" 
        
        draw.text((180,150), staffname, font=font, fill=font_color)
        img.save(new_image_path ) # Save with a new name to avoid overwriting
        print(f"Image saved with title: {new_image_path}")

    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except Exception as e:
         print(f"An error occurred: {e}")

# Example usage:
#image_file_path = "path/to/your/image.jpg"  # Replace with your image path
#add_filename_title(image_file_path)

if len(sys.argv) > 1:
    for arg in sys.argv:
        print("image folder {arg} specified:")
        iterate_files(arg)

else:
    print("No image folder provided.")

