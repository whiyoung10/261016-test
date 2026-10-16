# 그림으로 배우는 곱셈

초등학생이 사과, 별, 꽃 이모지의 배열을 보면서 곱셈의 의미를 배우는 Streamlit 앱입니다.

한 줄에 놓을 그림 수와 줄 수를 각각 1~9로 입력하면 배열과 계산 결과가 바로 바뀝니다.
**초기화**를 누르면 한 줄에 사과 2개씩 3줄인 처음 상태로 돌아갑니다.

### Codespaces에서 실행하기

Codespaces에서 제공하는 기본 Python 환경을 사용합니다. 가상환경을 만들거나 활성화할 필요가 없습니다.

1. 필요한 패키지를 설치합니다. 이미 설치되어 있다면 생략할 수 있습니다.

   ```bash
   python -m pip install -r requirements.txt
   ```

2. 앱을 실행합니다.

   ```bash
   python -m streamlit run streamlit_app.py
   ```

3. Codespaces의 **포트(Ports)** 탭에서 `8501` 포트의 브라우저 열기를 선택합니다.

### 프로젝트 구성과 개발 기준

- `streamlit_app.py`: 메인 앱 파일입니다. 기능 구현은 이 파일을 중심으로 진행합니다.
- `requirements.txt`: 앱에서 사용하는 외부 패키지만 기록합니다. 현재는 `streamlit`만 사용합니다.
- 그림은 이모지를 사용하므로 별도의 이미지 파일이나 다운로드가 필요하지 않습니다.
- Python 버전과 개발 환경 설정은 임의로 변경하지 않습니다.
- 새 패키지가 필요하면 `python -m pip install 패키지명`으로 설치하고 `requirements.txt`에 추가합니다.
- 불필요하게 파일이나 폴더를 나누지 않습니다.
