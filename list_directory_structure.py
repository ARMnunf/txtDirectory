import os

def list_directory_structure(root_path, output_file, indent_level=0):

    with os.scandir(root_path) as entries:
        for entry in entries:
            prefix = '    ' * indent_level 
            if entry.is_dir():
                output_file.write(f"{prefix}[DIR] {entry.name}\n")
                list_directory_structure(entry.path, output_file, indent_level + 1)
            else:
                output_file.write(f"{prefix}{entry.name}\n")

def save_structure_to_file(directory_path, output_filepath):

    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(f"Directory structure for: {directory_path}\n")
        f.write("-" * 50 + "\n")
        list_directory_structure(directory_path, f)

if __name__ == "__main__":
    # Change Here
    your_directory_path = r"C:\Users"
    output_filename = r"output\directory_structure.txt"
    
    save_structure_to_file(your_directory_path, output_filename)
    print(f"Directory structure saved to {output_filename}")
