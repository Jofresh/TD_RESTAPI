FROM python:3.10-alpine

RUN pip install --no-cache-dir uvicorn pymongo fastapi

COPY model_egg.py /

COPY immat_parser.py /

COPY app.py /

EXPOSE 3000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]
