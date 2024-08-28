#A puppet code to install nginx and configure it
package { 'systemctl':
    ensure => installed,
}

package { 'nginx':
    ensure => installed,
}

file { '/etc/nginx/sites-available/default':
    ensure => present,
}

file {'/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
}

$content = @("EOF")
\tlocation /redirect_me;
\t{
\t\treturn 301 index.html;
\t}
EOF

file_line { 'insert_after':
    path  => '/etc/nginx/sites-available/default',
    line  => $content,
    match => 'server_name _;',
    after => 'server_name _;',
}


