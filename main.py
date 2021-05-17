import os
import shutil
import inquirer


# Determine the users home path
user_dir = os.path.expanduser('~')
available_directories = [dI for dI in os.listdir(user_dir) if dI[0] != '.' if os.path.isdir(os.path.join(user_dir,dI))]


# Prompt for the desired source directory
dirs = [
  inquirer.List('dir',
                message="Which directory would you like to move PDF files from?",
                choices=available_directories,
            ),
]
answers = inquirer.prompt(dirs)
selected_dir = user_dir + '/' + answers["dir"]

# Prompt for the desired destination directory
dirs = [
  inquirer.List('dir',
                message="Which directory would you like to move PDF files to?",
                choices=available_directories,
            ),
]
answers = inquirer.prompt(dirs)
destination_dir = user_dir + '/' + answers["dir"]

# Move pdf files from the source directory to the destination directory
for filename in os.listdir(selected_dir):
    if filename.endswith(".pdf"):
        source = os.path.join(selected_dir, filename)
        destination = os.path.join(destination_dir, filename)
        dest = shutil.move(source, destination)