FROM python:3.6

RUN echo "Asia/Yekaterinburg" > /etc/timezone && \
      dpkg-reconfigure -f noninteractive tzdata

RUN mkdir -p /app
WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN ls -la

CMD [ "./manage.py", "runserver", "0.0.0.0:8000" ]