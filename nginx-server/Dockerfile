FROM nginx:latest

# копирую статические файлы, которые энджинкс будет отслеживать 
COPY static /usr/share/nginx/html

# копирую мою конфигурацию
COPY nginx.conf /etc/nginx/conf.d/default.conf