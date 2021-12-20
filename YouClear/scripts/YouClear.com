server {
        listen 80;
        server_name 54.180.150.134;

        location = /favicon.ico { access_log off; log_not_found off; }

        location /static {
                alias /home/ubuntu/env/YouClear/static_files;
        }

        location /media {
                alias /home/ubuntu/env/YouClear/media;
        }

        location / {
                include proxy_params;
                proxy_pass http://127.0.0.1:8000;
        }
}