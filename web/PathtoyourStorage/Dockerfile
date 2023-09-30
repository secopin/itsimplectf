FROM richarvey/nginx-php-fpm:1.10.2

RUN rm -Rf /etc/nginx/sites-enabled/*

ADD PHP/php.ini /usr/local/etc/php/conf.d/40-custom.ini

ADD Nginx/site.conf /etc/nginx/sites-available/site.conf

RUN ln -s /etc/nginx/sites-available/site.conf /etc/nginx/sites-enabled/site.conf

WORKDIR /var/www/task
