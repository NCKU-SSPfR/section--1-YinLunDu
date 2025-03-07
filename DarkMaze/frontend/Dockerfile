# 使用 Python 3.11 作為基礎映像
FROM python:3.11

# 設定工作目錄
WORKDIR /app

# 複製 Python 依賴需求檔案
COPY requirements.txt .

# 安裝後端依賴
RUN pip install --no-cache-dir -r requirements.txt

# 啟動 FastAPI 應用
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]
