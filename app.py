import pytesseract
from PIL import Image
import os
from pdf2image import convert_from_path
import shutil


def extract_text_from_image(path): # 이미지에서 텍스트 추출해주는 함수
    result = pytesseract.image_to_string(Image.open(path), lang = 'eng+kor')
    result.replace(" ","")
    result.replace('\n',"")
    return result



def check_file_extension(file_path): # 파일 확장자 확인해주는 함수
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    if ext in ['.pdf']:
        return 'PDF'
    elif ext in ['.hwp']:
        return 'HWP'
    elif ext in ['.png', '.jpg', '.jpeg']:
        return 'Image'
    else:
        return 'Unknown'

def extract_text_from_pdf(path): # pdf에서 텍스트 추출해주는 함수
    images = convert_from_path(path)
    final = ""
    
    for i, image in enumerate(images):
        image.save(f'./temp/temp_{i}.jpg', 'JPEG')
        result = extract_text_from_image(f'./temp/temp_{i}.jpg')
        result = result.replace(" ", "").replace("\n", "")  # 모든 띄어쓰기 및 줄바꿈 제거
        final+=result
    folder_path = 'temp'

# 폴더 내의 각 파일 및 하위 폴더에 대해 반복
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # 파일이면 삭제
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            # 폴더이면, 폴더 내용 삭제
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
    
    
    return final




# PDF 파일 경로
# pdf_path = '민태희_인사바른_경력증명서_20231226.pdf'
pdf_path = '민태희_어학증명서.pdf'
print(extract_text_from_pdf(pdf_path))








