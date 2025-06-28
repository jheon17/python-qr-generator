# 파이썬을 활용한 QR 코드 생성 프로젝트

이 프로젝트는 파이썬의 `qrcode` 와 `Pillow` 라이브러리를 사용하여 다양한 종류의 QR 코드를 생성하는 방법을 단계별로 학습하고 구현한 결과물입니다.

## 🚀 주요 기능

-   단순 텍스트 및 URL을 포함하는 기본 QR 코드 생성
-   vCard(연락처 정보)를 포함하는 QR 코드 생성 및 `.vcf` 파일 저장
-   `qrcode` 라이브러리의 내장 기능을 사용한 QR 코드 중앙에 이미지 삽입
-   `Pillow` 라이브러리를 사용하여 QR 코드의 특정 위치에 이미지 삽입

## 📂 디렉토리 구조

```
.
├── input/
│   └── phone.png           # QR 코드에 삽입할 아이콘 이미지
├── output/
│   └── (생성된 QR 코드 결과물)
├── basic_qr_step1.py     # Step 1: 기본 QR 코드 생성
├── contract_to_qr_step2.py # Step 2: 연락처 QR 코드 생성
├── image_to_qr_step3.py  # Step 3: 이미지 삽입 QR 코드 생성
├── requirements.txt      # 프로젝트 의존성 라이브러리 목록
└── README.md             # 프로젝트 설명서
```

## 🛠️ 설치 및 환경 설정

1.  **프로젝트 복제**
    ```bash
    git clone [https://github.com/](https://github.com/){사용자_이름}/{저장소_이름}.git
    cd {저장소_이름}
    ```

2.  **필요 라이브러리 설치**
    프로젝트 실행에 필요한 라이브러리들이 `requirements.txt`에 명시되어 있습니다. 아래 명령어로 한 번에 설치할 수 있습니다.
    ```bash
    pip install -r requirements.txt
    ```
    > **[참고]** `requirements.txt` 파일 내용은 다음과 같습니다.
    > ```
    > qrcode
    > Pillow
    > ```

3.  **`input` 폴더 준비**
    `input` 폴더를 생성하고, QR 코드에 삽입할 `phone.png` 이미지 파일을 위치시킵니다.

## 🏃‍♀️ 실행 방법

각 스크립트는 독립적으로 실행할 수 있으며, 순서대로 실행하며 QR 코드가 발전하는 과정을 확인할 수 있습니다.

1.  **Step 1: 기본 QR 코드 생성 (`basic_qr_step1.py`)**
    `output` 폴더를 생성하고, 단순 텍스트와 URL이 담긴 두 종류의 기본 QR 코드를 생성하여 저장합니다.
    ```bash
    python basic_qr_step1.py
    ```

2.  **Step 2: 연락처 QR 코드 생성 (`contract_to_qr_step2.py`)**
    vCard 형식의 연락처 정보를 담은 `.vcf` 파일과 QR 코드를 `output` 폴더에 생성합니다.
    ```bash
    python contract_to_qr_step2.py
    ```

3.  **Step 3: 이미지 삽입 QR 코드 생성 (`image_to_qr_step3.py`)**
    Step 2에서 생성된 연락처 QR 코드에 이미지를 삽입합니다. 두 가지 방법을 보여줍니다.
    -   `qrcode` 라이브러리의 `StyledPilImage`를 사용하여 QR 코드 중앙에 이미지를 삽입합니다.
    -   `Pillow` 라이브러리를 사용하여 QR 코드 우측 하단에 이미지를 삽입합니다.
    ```bash
    python image_to_qr_step3.py
    ```

## 🧐 코드 주요 포인트 및 분석

### `pathlib` 사용
-   `Path(__file__).parent` 와 같은 코드를 통해 스크립트의 위치를 기준으로 경로를 설정했습니다. 이는 운영체제(Windows, macOS, Linux)에 상관없이 경로를 올바르게 처리할 수 있는 현대적이고 안정적인 방법입니다.

### `if __name__ == "__main__"` 의 중요성
-   모든 스크립트의 실행 코드가 `if __name__ == "__main__"` 블록 안에 있습니다. 이는 다른 스크립트에서 해당 파일의 특정 변수(`OUT_DIR` 등)나 함수를 `import`할 때, 실행 코드가 자동으로 동작하는 것을 방지합니다. 이는 코드의 재사용성과 모듈화를 위해 매우 중요한 습관입니다.

### 이미지 삽입 방법 비교
-   `image_to_qr_step3.py` 에서는 두 가지 이미지 삽입 방법을 사용합니다.
    1.  **`qrcode.image.styledpil.StyledPilImage`**: `qrcode` 라이브러리에서 공식적으로 지원하는 기능입니다. QR 코드의 인식률을 해치지 않는 선에서 중앙에 이미지를 쉽게 삽입할 수 있도록 도와줍니다. 하지만 위치나 크기 조절의 유연성은 다소 떨어집니다.
    2.  **`Pillow`**: QR 코드 자체를 이미지 객체로 불러와 다른 이미지(아이콘)를 `paste` 하는 방식입니다. 픽셀 단위의 정밀한 위치(x, y 좌표) 및 크기 조절이 가능하여 자유도가 매우 높습니다. 다만, 이미지를 너무 크게 삽입하거나 QR 코드의 중요 영역(모서리의 Finder 패턴 등)을 가릴 경우 인식률이 저하될 수 있으므로 주의가 필요합니다. 본 코드에서는 `icon_x`, `icon_y` 좌표 계산을 통해 우측 하단에 배치했습니다.

## 📈 향후 개선 과제

-   **사용자 입력 처리**: 터미널에서 직접 QR 코드로 만들 텍스트, URL, 연락처 정보 등을 입력받는 CLI(Command-Line Interface) 기능 추가
-   **에러 핸들링**: `input` 폴더나 이미지 파일이 없을 경우 발생하는 `FileNotFoundError` 등에 대한 예외 처리 코드 추가
-   **코드 리팩토링**: 중복되는 코드나 설정을 별도의 설정 파일(`config.py` 또는 `.yaml`)로 분리하여 관리 효율성 증대