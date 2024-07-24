#A puppet file to configure the client for my ubuntu server
$str = @("EOF")
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
EOF

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => $str,
}

