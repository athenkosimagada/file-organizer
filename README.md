# File Organizer

A Python script that monitors a specified download directory and organizes downloaded files based on their file extensions. The script automatically moves files to appropriate folders, ensuring that files are only moved once they are fully downloaded.

## Features
- **File Monitoring**: Continuously monitors a directory (default: `Downloads`) for new files.
- **File Sorting**: Automatically moves files to a target directory based on their file extension (e.g., images, documents, etc.).
- **Handling Large/Slow Files**: Waits indefinitely for files to be fully downloaded before moving them, ensuring even large files are handled correctly.
- **Error Logging**: Logs various events, including file movements, errors, and warnings for easy debugging and monitoring.

## Requirements
- Python 3.7 or higher
- Required Python libraries are listed in the `requirements.txt` file.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/athenkosimagada/file-organizer.git
   ```

2. Install the required dependencies using `pip` and the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the `config/settings.py` file to set your `DOWNLOAD_DIR` and `TARGET_DIR` (default paths are `C:/Users/magad/Downloads` and `C:/path/to/target/folder`).

## Usage

1. Make sure the script is correctly configured with your desired download and target directories.

2. Run the script:
   ```bash
   python src/main.py
   ```
   The script will begin monitoring the `DOWNLOAD_DIR` for new files.

3. It will wait for each file to finish downloading, then move it to the appropriate subdirectory in `TARGET_DIR` based on the file extension.

## How It Works

1. **File Detection**: The script uses `watchdog` to monitor the download directory. When a new file is created, the script checks whether it's finished downloading.
2. **File Validation**: The file is validated using the `is_file_downloaded` function, and only once it’s confirmed that the file is no longer a temporary file, is it moved to the target directory.
3. **Organizing Files**: Files are sorted into folders based on their file extension (e.g., images, documents). If the file extension is not recognized, it's moved to an "Others" folder.

## Folder Structure

The target directory will have subdirectories based on the file types as defined in the `file_types.py` module. Each file is moved to its respective folder.

Example:

```
TARGET_DIR/
├── Images/
│   ├── photo1.jpg
│   └── image.png
├── Documents/
│   ├── report.pdf
│   └── resume.docx
└── Others/
    ├── unknownfile.xyz
```

## Logs

The script uses a custom logger to log all activity, warnings, and errors. These logs can be found in the output directory or specified in the `logger.py` settings.

## Contribution

Feel free to fork this project and submit pull requests. Please make sure to write tests for any new features you add and follow the conventional commits for commit messages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [watchdog](https://pypi.org/project/watchdog/) - For monitoring the file system events.
- [shutil](https://docs.python.org/3/library/shutil.html) - For file handling utilities like moving and copying.
- [Python Logging](https://docs.python.org/3/library/logging.html) - For activity and error logging.

### Explanation of the Sections:
- **File Monitoring** and **Features** explain the capabilities and behavior of the script.
- **Requirements** outlines the necessary dependencies (as listed in `requirements.txt`).
- **Setup** provides a quick guide to get the project running, with installation instructions.
- **Usage** explains how the script works and the flow of its execution.
- **How It Works** section goes into the details of file detection, validation, and sorting.
- **Folder Structure** shows an example of how files are organized into folders based on their types.
- **Logs** outlines the logging mechanism for tracking activity and errors.
- **Contribution** encourages collaboration with guidelines on commits.
- **License** provides a reference to the MIT License, but you can replace it with your actual license if it's different.