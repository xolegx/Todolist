FROM python:3.12
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .

CMD python ./todolist/manage.py migrate
CMD python ./todolist/manage.py runserver 0.0.0.0:8000