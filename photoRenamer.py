import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from PIL.ExifTags import TAGS

def get_photo_datetime(filepath):
    try:
        image = Image.open(filepath)
        exif_data = image._getexif()
        if exif_data is not None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == 'DateTimeOriginal':
                    return value.replace(':', '-').replace(' ', '_')
    except Exception as e:
        print(f"Error retrieving date from {filepath}: {e}")
    return None

def rename_photos(directory, prefix, include_date, index_start):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    files = os.listdir(directory)
    photo_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    photo_info = []
    for filename in photo_files:
        old_path = os.path.join(directory, filename)
        datetime = get_photo_datetime(old_path) or "unknown_date_time"
        photo_info.append((datetime, old_path, filename))

    # 按拍照時間排序
    photo_info.sort()

    # 重新命名照片
    date_counters = {}
    for datetime, old_path, filename in photo_info:
        date = datetime.split('_')[0] if include_date else ''
        if date not in date_counters:
            date_counters[date] = index_start
        else:
            date_counters[date] += 1

        new_filename = f"{prefix}_{date}_{date_counters[date]}{os.path.splitext(filename)[1]}"
        new_path = os.path.join(directory, new_filename)

        # 檢查新檔名是否已存在，避免覆蓋
        if os.path.exists(new_path):
            print(f"Error: {new_path} already exists. Skipping rename for {old_path}.")
            continue

        os.rename(old_path, new_path)
        print(f"Renamed {old_path} to {new_path}")

    messagebox.showinfo("Batch Renaming Completed", "All photos have been renamed successfully.")

def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory_path)

def start_renaming():
    directory = directory_entry.get()
    prefix = prefix_entry.get()
    include_date = date_var.get()
    try:
        index_start = int(index_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the index start.")
        return

    rename_photos(directory, prefix, include_date, index_start)

# 建立主視窗
root = tk.Tk()
root.title("Photo Renamer")

# 資料夾路徑
tk.Label(root, text="Directory:").grid(row=0, column=0, padx=10, pady=10)
directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=0, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# 檔名前綴
tk.Label(root, text="Prefix:").grid(row=1, column=0, padx=10, pady=10)
prefix_entry = tk.Entry(root, width=50)
prefix_entry.grid(row=1, column=1, padx=10, pady=10)

# 是否包含日期
date_var = tk.BooleanVar()
date_check = tk.Checkbutton(root, text="Include Date", variable=date_var)
date_check.grid(row=2, columnspan=3, padx=10, pady=10)

# 索引起始值
tk.Label(root, text="Index Start:").grid(row=3, column=0, padx=10, pady=10)
index_entry = tk.Entry(root, width=50)
index_entry.grid(row=3, column=1, padx=10, pady=10)

# 開始重新命名按鈕
rename_button = tk.Button(root, text="Start Renaming", command=start_renaming)
rename_button.grid(row=4, columnspan=3, pady=20)

root.mainloop()
