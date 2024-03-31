import cv2
import pytesseract
import os
import csv
from pyzbar.pyzbar import decode
from shutil import copyfile, move
from tqdm import tqdm


input_folder = "in"
output_folder = "out"
not_found_folder = "NOTFIND"


if not os.path.exists(input_folder):
    os.makedirs(input_folder)


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # قم بتغيير المسار حسب مكان تثبيت Tesseract OCR على جهازك


folder_counter = 1


for filename in tqdm(os.listdir(input_folder)):  
    if filename.endswith((".jpeg", ".JPG", ".png")):
        image_path = os.path.join(input_folder, filename)


        image = cv2.imread(image_path)


        text_tesseract = pytesseract.image_to_string(image, lang='eng')


        decoded_objects = decode(image)
        text_code128 = ""
        for obj in decoded_objects:
            if obj.type == 'CODE128':
                text_code128 = obj.data.decode('utf-8')
                break


        final_text = f"Tesseract OCR: {text_tesseract}\nCODE 128: {text_code128}"

        if text_code128:

            image_folder = os.path.join(output_folder, f"Folder_{folder_counter}")
            os.makedirs(image_folder, exist_ok=True)


            image_copy_path = os.path.join(image_folder, filename)
            copyfile(image_path, image_copy_path)

            csv_file_path = os.path.join(image_folder, f"Folder_{folder_counter}.csv")
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                fieldnames = ['Text']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

                
                writer.writerow({'Text': final_text})

            
            folder_counter += 1
        else:
         
            not_found_folder_path = os.path.join(output_folder, not_found_folder)
            os.makedirs(not_found_folder_path, exist_ok=True)

            
            not_found_image_path = os.path.join(not_found_folder_path, filename)
            move(image_path, not_found_image_path)

print(f"Done : {output_folder}")