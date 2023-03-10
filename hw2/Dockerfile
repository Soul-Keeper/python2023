FROM python:3.9

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 libgdiplus texlive dos2unix -y

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/ sidelnikovpicgen

RUN dos2unix run.sh

CMD ["./run.sh"]