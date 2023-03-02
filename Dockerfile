FROM python:3.8-slim

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user

RUN apt update && apt install -y python3-dev \
                        build-essential \
                        gcc \
                        libc-dev

COPY requirements.txt ./

RUN pip install --no-cache-dir -r "requirements.txt"

RUN python -m spacy download en_core_web_lg

USER app_user

COPY . .

CMD ["bash"]

#ENTRYPOINT [ "python", "./keyword_extraction_v2_test.py" ]