def get_file_type(filename):
    file_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    # Convert the filename to lowercase to make the check case-insensitive
    filename_lower = filename.lower()

    # Loop through the dictionary to find the correct media type
    for ext, media_type in file_types.items():
        if filename_lower.endswith(ext):
            return media_type

    # If no match is found, return the default media type
    return "application/octet-stream"

def main():
    # Prompt the user for the name of the file
    filename = input("Enter the file name: ").strip()

    # Get the media type for the given file name
    file_type = get_file_type(filename)

    # Output the media type
    print(file_type)

main()
