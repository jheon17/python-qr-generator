from pathlib import Path
from basic_qr_step1 import OUT_DIR
import qrcode

OUT_VCF = OUT_DIR / f"{Path(__file__).stem}.vcf"
OUT_PNG = OUT_DIR / f"{Path(__file__).stem}.png"

if __name__ == "__main__":
    data = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        "N:정;제헌",
        "FN:정제헌",
        "TEL;type=CELL:+82 10-7400-0033",
        "END:VCARD",
    ]
    vcf = "\n".join(data)

    # vCard 파일 저장
    with open(OUT_VCF, "w", encoding="utf-8") as fp:
        fp.write(vcf)

    # QR 코드 생성 및 저장
    img = qrcode.make(vcf)
    img.save(OUT_PNG)
