FROM nginx:1.27-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY ssl/lab2.crt /etc/nginx/ssl/lab2.crt
COPY ssl/lab2.key /etc/nginx/ssl/lab2.key

COPY templates/default.conf.template /etc/nginx/templates/default.conf.template
