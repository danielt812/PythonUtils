import os
import sys

# Find path to Desktop and Downloads directories
desktop_dir = os.path.expanduser("~/Desktop")
downloads_dir = os.path.expanduser("~/Downloads")


def process_flags(flags):
    if "--help" in flags or "-h" in flags:
        print("Help information:")
        print("- Usage: python script.py [options]")
        print("- Options:")
        print("  --help, -h: Display help information")
        print("          -a: Delete files and directories in Desktop and Downloads")
        print("          -f: Delete only files in Desktop and Downloads")
        print("          -d: Delete only directories in Desktop and Downloads")

        # Add more help information if needed
    elif "-a" in flags:
        print("Deleting all files and directories in Desktop and Downloads")
        cleanFiles(desktop_dir, 'all')
        cleanFiles(downloads_dir, 'all')
    elif "-f" in flags:
        print("Deleting only files in Desktop and Downloads")
        cleanFiles(desktop_dir, 'file')
        cleanFiles(downloads_dir, 'file')
    elif "-d" in flags:
        print("Deleting only directories in Desktop and Downloads")
        cleanFiles(desktop_dir, 'directory')
        cleanFiles(downloads_dir, 'directory')
    else:
        print("No valid flags provided.")


def cleanFiles(dir, filetype):
    # Change directory to desktop
    os.chdir(dir)

    # Get the current working directory
    cwd = os.getcwd()

    # List files in the current working directory
    files = os.listdir(cwd)

    for file in files:
        if filetype == 'file':
            if os.path.isfile(file):
                _, file_extension = os.path.splitext(file)
                # Only delete file if it has an extension
                if file_extension != '':
                    os.remove(file)
                    print(file, 'deleted')
        if filetype == 'directory':
            if os.path.isdir(file):
                os.rmdir(file)
                print(file, 'deleted')
        if filetype == 'all':
            if os.path.isfile(file):
                _, file_extension = os.path.splitext(file)
                # Only delete file if it has an extension
                if file_extension != '':
                    os.remove(file)
                    print(file, 'file deleted')
            if os.path.isdir(file):
                os.rmdir(file)
                print(file, 'directory deleted')


# Get command-line arguments except script name
command_flags = sys.argv[1:]
process_flags(command_flags)
