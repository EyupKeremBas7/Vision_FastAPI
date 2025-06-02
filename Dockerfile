FROM python:3-buster
RUN pip install --upgrade pip
WORKDIR /src
ENV PYTHONPATH=/src
RUN pip install Pillow
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./src ./src/
COPY ./src/pred/models/Trafic_signs_model.keras Trafic_signs_model.keras
COPY ./src/utils/DigiNova_Ornekler /DigiNova_Ornekler
CMD ["uvicorn", "src.app.app:app", "--host", "0.0.0.0", "--port", "7001"]