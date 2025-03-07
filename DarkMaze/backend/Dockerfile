# 使用 Python 3.11 作為基礎映像
FROM python:3.11

# 設定工作目錄
WORKDIR /app

# 複製依賴項檔案
COPY requirements.txt .

# 安裝後端依賴
RUN pip install --no-cache-dir -r requirements.txt

# 執行應用程式
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]