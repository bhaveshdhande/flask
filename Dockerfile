FROM python

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:80 main:app --reload --threads 8
