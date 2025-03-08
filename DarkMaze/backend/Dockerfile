# 使用 Python 3.11 作為基礎映像
FROM python:3.11

# 設定工作目錄
WORKDIR /app

# 建立非 root 使用者
RUN useradd -m appuser

# 切換至非 root 使用者
USER appuser

# 複製依賴項檔案
COPY --chown=appuser:appuser requirements.txt .

# 安裝後端依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式程式碼
COPY --chown=appuser:appuser . .

# 執行應用程式
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
