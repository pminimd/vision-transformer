from PIL import Image
import os

def resize_images_to_640x640(folder_path, size=(640, 640)):
    """
    Resize all images in the specified folder to 640x640 pixels.

    Parameters:
    folder_path (str): Path to the folder containing images.
    size (tuple): Desired size for resizing images (width, height). Default is (640, 640).
    """
    # Ensure the output directory exists
    output_folder = os.path.join(folder_path, "resized")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Construct the full path to the file
        file_path = os.path.join(folder_path, filename)
        
        # Only process image files (you can add more extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            with Image.open(file_path) as img:
                # Resize the image
                resized_img = img.resize(size)
                
                # Save the resized image to the output folder
                resized_img.save(os.path.join(output_folder, filename))
                print(f"Resized and saved {filename}")

# Example usage:
resize_images_to_640x640('/mnt/data8T/wjyue/YQSL_scene/dataset/scene_cls_dataset')
