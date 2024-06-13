# Increases the amount of traffic and nginx server can handle.

# Increase the ULIMIT of the default file
exec {'fix-for-nginx-configuration':
# modify the ULIMIT value
command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
# specify the path for the sed command
path    => '/usr/local/bin/:/bin/',
}

# restart nginx
exec {'nginx-restart':
# Restart nginx service
command => '/etc/init.d/nginx restart',
# specify the path for the restart command
path    => '/etc/init.d/'
}
