import os
import shutil
import datetime

# Source directories to backup
source_paths = ["C:\\Path\\To\\Source\\Directory"]

# Destination directory on the external storage device
destination_path = "F:\\Backup"

# Log file path
log_file = "backup_log.txt"

def backup_files(source_paths, destination_path, log_file):
    # Create backup directory if it doesn't exist
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Get current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Open log file in append mode
    with open(log_file, "a") as f:
        f.write(f"Backup started at: {timestamp}\n")

        # Perform backup for each source path
        for source_path in source_paths:
            # Get the base name of the source path
            source_base_name = os.path.basename(source_path)
            # Create the destination directory if it doesn't exist
            destination_dir = os.path.join(destination_path, source_base_name)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            # Copy files from source to destination recursively
            try:
                for root, dirs, files in os.walk(source_path):
                    # Determine the relative path within the source directory
                    relative_path = os.path.relpath(root, source_path)
                    destination_subdir = os.path.join(destination_dir, relative_path)
                    # Create the destination subdirectory if it doesn't exist
                    if not os.path.exists(destination_subdir):
                        os.makedirs(destination_subdir)
                    # Copy files to the destination subdirectory
                    for file in files:
                        source_file_path = os.path.join(root, file)
                        destination_file_path = os.path.join(destination_subdir, file)
                        shutil.copy2(source_file_path, destination_file_path)
                        f.write(f"Copied: {source_file_path} -> {destination_file_path}\n")
            except Exception as e:
                f.write(f"Backup failed for {source_path}: {str(e)}\n")

        f.write("Backup completed.\n\n")

if __name__ == "__main__":
    backup_files(source_paths, destination_path, log_file)
