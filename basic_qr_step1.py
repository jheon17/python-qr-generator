#1 폴더 생성
from pathlib import Path

WORK_DIR = Path(__file__).parent
IN_DIR, OUT_DIR = WORK_DIR/"input", WORK_DIR/"output"

if __name__ =="__main__":
    IN_DIR.mkdir(exist_ok=True)
    OUT_DIR.mkdir(exist_ok=True)


#2 QR코드 생성 - 문자열
import qrcode

img = qrcode.make("hello, qrcode!")
img


#3 QR코드 생성 - 유튜브
img_youtube = qrcode.make("https://www.youtube.com/")
img_youtube


#4 QR코드 파일로 저장
img_hello = qrcode.make("hello, qrcode!")
img_hello.save(OUT_DIR/f"{Path(__file__).stem}_hello.png")
img_youtube = qrcode.make("https://www.youtube.com/")
img_youtube.save(OUT_DIR/f"{Path(__file__).stem}_youtube.png")