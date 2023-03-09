# builder stage (temp)
FROM python:3.8-slim as builder

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends python3-dev \
                        build-essential \
                        gcc

COPY requirements.txt ./

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt \
                        docanalysis

#final stage
FROM python:3.8-slim

WORKDIR /home/app

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*


# RUN python -m spacy download en_core_web_lg

RUN apt-get update && apt-get install tk -y && apt-get install git -y

#RUN useradd --create-home --shell /bin/bash app_user

#USER app_user

COPY . .

RUN docanalysis --help

CMD ["bash"]

#ENTRYPOINT [ "python", "./keyword_extraction_v2_test.py" ]