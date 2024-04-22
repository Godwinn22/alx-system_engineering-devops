# Ensure pip3 is installed
# Install Flask version 2.1.0 using pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.0.3', # Or specify the version compatible with Flask 2.1.0
  provider => 'pip3',
}