import glob
import os

directory = "C:\\Users\\eitom\\OneDrive\\Desktop\\ganba" #os.path.expanduser("~/Desktop")


files = glob.glob(f"{directory}\\*.webm")
len = len(files)
files_name = []
for f in range(len):
    files_name.append(os.path.basename(files[f]))
    print(f"第{f+1}曲：『　{files_name[f]}　』\n")

