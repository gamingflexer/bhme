import sys

book_no = sys.argv[1]

link = "https://drive.google.com/drive/folders/1p-4ghiHJq1W_HVdQMwsQ5EKLo0eydRhJ?usp=share_link"

path_to_download_corpus = "/content/data"

import gdown
gdown.download_folder(link, quiet=True,output=path_to_download_corpus,remaining_ok=True)
print('Starting...\n')

import os
def get_txt_file(number_file,path):
  os_dir = os.listdir(path)
  for i in os_dir:
    if i.endswith("txt"):
      number = i.split("_")[1]
      if int(number) == int(number_file):
        return (os.path.join(path ,i))
    
file_to_open = get_txt_file(book_no,path_to_download_corpus)

os.system(f"mkdir /content/bhme/data")
os.system(f"mv /content/data/chunksmr_{book_no}_.txt /content/bhme/data/")

print('Task Started...\n next task will take time')

os.system("python /content/bhme/dataset_locally.py")

