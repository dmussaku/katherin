FROM tutum/nginx
RUN mkdir /logs
RUN mkdir /logs/nginx

RUN rm /etc/nginx/sites-enabled/default
ADD ./nginx.conf /etc/nginx/sites-enabled/django_docker.conf