# This script Changes the OS configuration so that it
# - is possible to login with the holberton user and open
# - a file without any error message.

# Increase hard file limit for holberton user

exec { 'holberton-hard-nofile':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path   => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for holberton user

exec { 'holberton-soft-nofile':
  command => "sed -i '/^holberton soft/s/5/50000/' /etc/security/limits.conf",
  path   => '/usr/local/bin/:/bin/'
}
