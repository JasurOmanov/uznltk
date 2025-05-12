import requests
import zipfile
import io
import os
import shutil

def download_folder(folder_name):
    repo_url = "https://github.com/JasurOmanov/Manbalar"
    repo_zip_url = repo_url.rstrip("/") + "/archive/refs/heads/main.zip"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        print(f"'{folder_name}' papkasi yuklab olinmoqda...")
        response = requests.get(repo_zip_url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Yuklab olishda xatolik: {e}")
        return

    try:
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            main_dir = z.namelist()[0].split('/')[0]
            extract_path = f"{main_dir}/{folder_name}"
            found = False
            extract_to = f"temp_extract_{folder_name}"

            if os.path.exists(extract_to):
                shutil.rmtree(extract_to)
            os.makedirs(extract_to)

            for file in z.namelist():
                if file.startswith(extract_path + "/") and not file.endswith("/"):
                    found = True
                    z.extract(file, extract_to)

            if not found:
                print(f"'{folder_name}' papkasi topilmadi.")
                shutil.rmtree(extract_to)
                return

            if not os.path.exists("Manba"):
                os.makedirs("Manba")

            final_path = os.path.join("Manba", folder_name)
            if os.path.exists(final_path):
                shutil.rmtree(final_path)
            shutil.move(os.path.join(extract_to, main_dir, folder_name), final_path)
            shutil.rmtree(extract_to)
            print(f"'{folder_name}' papkasi 'Manba/' ichiga muvaffaqiyatli yuklandi.")

    except zipfile.BadZipFile:
        print("ZIP faylni ochishda xatolik.")
    except Exception as e:
        print(f"Faylni ajratishda xatolik: {e}")

def Book():
    download_folder("Uzb_kitoblar")

def News():
    download_folder("Yangiliklar")
