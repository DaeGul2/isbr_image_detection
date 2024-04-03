import pytesseract
from PIL import Image
import magic

def check_file_type(file_path):
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    return file_type



image_path = './image2.png'


# Tesseract를 사용해 이미지에서 텍스트 추출

result = pytesseract.image_to_string(Image.open(image_path), lang = 'kor')

print(result)

# print(check_file_type(image_path))

