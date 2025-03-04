import glob
import os

directory = "" #絶対パス入力時は\\を使用してね


files = glob.glob(f"{directory}\\*.webm")
len = len(files)
files_name = []
for f in range(len):
    files_name.append(os.path.basename(files[f]))
    print(f"第{f+1}曲：『　{files_name[f]}　』\n")

