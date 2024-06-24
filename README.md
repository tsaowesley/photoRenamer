# PhotoRenamer

PhotoRenamer is a simple tool to batch rename your photos based on their EXIF data, such as the date they were taken. This project includes a standalone executable application for easy use.

## Features

- Rename photos based on EXIF data (DateTimeOriginal).
- Add custom prefixes to filenames.
- Include or exclude the date in the new filenames.
- Automatically sort and rename photos.

## Download and Installation

You can download the executable directly from the `dist` folder in this repository.

1. **Download**:
   - [photoRenamer](https://github.com/tsaowesley/photoRenamer/releases/download/v1.0.0/photoRenamer.zip) 

   
2. **Run the executable**:
   - For Windows, double-click the `photoRenamer.exe` file.
   - For Mac, double-click the `photoRenamer` file.

## Usage

1. **Open the PhotoRenamer application**:
   - Double-click the downloaded executable file to open the application.

2. **Select the directory containing your photos**:
   - Click the "Browse" button and choose the folder where your photos are stored.

3. **Set the filename prefix**:
   - Enter a custom prefix for the new filenames.

4. **Include the date**:
   - Check the "Include Date" checkbox if you want the date to be included in the filenames.

5. **Set the starting index**:
   - Enter a starting index for the filenames.

6. **Start the renaming process**:
   - Click the "Start Renaming" button to batch rename your photos.

## Example

1. **Directory**: `C:\Users\YourName\Pictures`
2. **Prefix**: `Holiday`
3. **Include Date**: Checked
4. **Index Start**: `1`

This configuration will rename your photos to something like `Holiday_2021-06-24_1.jpg`.
