import os
import urllib.request

base_url = "http://posefs1.perception.cs.cmu.edu/OpenPose/models"

files_to_download = {
    "pose/body_25/pose_iter_584000.caffemodel": "pose/body_25/",
    "face/pose_iter_116000.caffemodel": "face/",
    "hand/pose_iter_102000.caffemodel": "hand/"
}

for file, folder in files_to_download.items():
    url = f"{base_url}/{file}"
    out_dir = os.path.join(os.getcwd(), folder)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, os.path.basename(file))

    print(f"Downloading {file}...")
    urllib.request.urlretrieve(url, out_path)
    print(f"Saved to {out_path}")
