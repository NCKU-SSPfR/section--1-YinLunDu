# 使用精簡版 Python 3.11 作為基礎映像
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製當前目錄的內容到容器內
COPY . .

# 安裝所需的 Python 套件（若有 requirements.txt）
RUN pip install --no-cache-dir -r requirements.txt

# 設定預設執行指令
CMD ["python", "main.py"]
