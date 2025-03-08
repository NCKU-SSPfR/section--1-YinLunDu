# 使用 Python 3.11 作為基礎映像
FROM python:3.11-slim

# 建立非 root 使用者
RUN useradd -m appuser

# 設定工作目錄
WORKDIR /app

# 複製 Python 依賴需求檔案
COPY requirements.txt .

# 安裝後端依賴
RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt /app/requirements.txt
COPY src/ /app/src

RUN chown -R appuser:appuser /app

# 切換至非 root 使用者
USER appuser

EXPOSE 8088

# 啟動 FastAPI 應用
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]