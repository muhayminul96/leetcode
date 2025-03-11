import os
import json

def main(dir,com, postfix):
    try:
        with open("ctagscript.sh", "w") as br:
            for i in dir:
                br.write(f"\n {com}/{i} {postfix};")
    except Exception as e:
        print(f"Error: {e}")


def get_directory_names(path):
    try:
        dir_names = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        return dir_names
    except Exception as e:
        print(f"Error: {e}")
        return []

# Example Usage

if __name__ == "__main__":

    with open('config.json', "r") as file:
        data = json.load(file)  # Load JSON data

    # Check if the JSON contains a list of paths
    if "path" in data:
        all_directories = get_directory_names(data['path'])
        command=data['command']
        postfix = data['postfix']
        main(all_directories,command,postfix)

        print(all_directories)

    else:
        print("Invalid JSON format! Expected key: 'paths'")

    # path = ""  # Change this to your target directory
    # directories = get_directory_names(path)
    # print(directories)
    # main(directories)