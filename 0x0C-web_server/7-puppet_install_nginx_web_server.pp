# 5. Install Nginx web server (w/ Puppet)

exec {'/usr/bin/env apt-get update':}
exec {'/usr/bin/env apt-get -y install nginx':}
exec {'/usr/bin/env ufw allow "Nginx HTTP"':}
exec {'/usr/bin/env echo "Hello World!" > /var/www/html/index.nginx-debian.html':}
exec {'/usr/bin/env sed -i "/listen 80 default_server/a rewrite ^/redirect_me https://github.com/godwinn22 permanent;" /etc/nginx/sites-available/default':}
exec {'/usr/bin/env service nginx start':}
