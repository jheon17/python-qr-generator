# qrcode 패키지로 이미지 삽입
from qrcode.image.styledpil import StyledPilImage
from qrcode.main import QRCode
from basic_qr_step1 import IN_DIR
from contract_to_qr_step2 import OUT_VCF

with open(OUT_VCF, encoding="utf-8") as fp:
    vcf = fp.read()

qr = QRCode()
qr.add_data(vcf)
img = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path= IN_DIR/"phone.png",
)
img

# pillow 패키지로 이미지 삽입
from pathlib import Path
from PIL import Image
from basic_qr_step1 import IN_DIR, OUT_DIR
from contract_to_qr_step2 import OUT_PNG

OUT_STEP_3_2 = OUT_DIR/f"{Path(__file__).stem}.png"

if __name__ == " __main__":
    qr = Image.open(OUT_PNG).convert('RGBA')
    width_qr, height_qr = qr.size
    icon = Image.open(IN_DIR/"phone.png")
    width_icon = int(width_qr*0.3)
    height_icon = int(height_qr*0.3)
    icon_resized = icon.resize((width_qr, height_icon))

    pad = 50
    icon_x = width_qr - width_icon -pad
    icon_y = height_qr - height_icon - pad

    qr.paste(icon_resized, box=(icon_x,icon_y), mask=icon_resized)
    qr.save(OUT_STEP_3_2)