import os.path


def get_media_list(folder_path):
    # get all mp4 files in the folder path, verify the files and
    # return a list of tuple of (file_name, file_path)
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(
            f"Error: The specified folder path '{folder_path}' does not exist or is not a directory."
        )
        return

    media_list = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(".mp4"):
            media_list.append((file_name, file_path))

    return media_list
