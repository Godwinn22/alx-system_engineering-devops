# This script Changes the OS configuration so that it
# - is possible to login with the holberton user and open
# - a file without any error message.

# Increase hard file limit for holberton user

exec { 'change-max-open-files-hard-limit':
  command => "/bin/sed -i /etc/security/limits.conf -e 's/hard nofile [0-9]\+/hard nofile 50000/g'"
}

# Increase soft file limit for holberton user

exec { 'change-max-open-files-soft-limit':
  command => "/bin/sed -i /etc/security/limits.conf -e 's/soft nofile [0-9]\+/soft nofile 50000/g'"
}
