from PIL import Image
import os
print("Current working directory:", os.getcwd())

def dir_check(dir_location):
    isExist = os.path.exists(dir_location)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(dir_location)
        print("The new directory is created!")
    else:
        print("directory already exists!")

def load_image(img_url):
    try:
        if img_url.startswith("http"):
            import requests
            from io import BytesIO
            response = requests.get(img_url)
            if response.status_code != 200:
                print("HTTP error:", response.status_code)
                return None
            img = Image.open(BytesIO(response.content))
        else:
            print("Trying to open:", img_url)
            if not os.path.exists(img_url):
                print("File does not exist:", img_url)
                return None
            img = Image.open(img_url)
        img = img.convert("RGB")
        return img
    except Exception as e:
        print("Exception in load_image:", e)
        return None
