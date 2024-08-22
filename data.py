import os

def rename_images_in_folder(folder_path, prefix="shelf_"):
    """
    Rename all image files in the specified folder with the given prefix.

    Parameters:
    folder_path (str): Path to the folder containing images.
    prefix (str): Prefix for the new filenames. Default is "binggui_".
    """
    # Initialize a counter
    i = 1

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Construct the full path to the file
        file_path = os.path.join(folder_path, filename)

        # Only process image files (you can add more extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            # Construct the new filename
            new_filename = f"{prefix}{i}.jpg"
            new_file_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")

            # Increment the counter
            i += 1

# Example usage:
rename_images_in_folder('/mnt/data8T/wjyue/YQSL_scene/dataset/场景训练集/货架')
