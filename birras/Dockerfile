FROM python:3.6.7

RUN mkdir -p /home/app
WORKDIR /home/app
COPY requirements.txt /home/app
RUN pip install --upgrade pip
RUN pip install setuptools --upgrade
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/app

# run entrypoint.sh
RUN chmod +x /home/app/entrypoint.sh

ENTRYPOINT ["/home/app/entrypoint.sh"]
