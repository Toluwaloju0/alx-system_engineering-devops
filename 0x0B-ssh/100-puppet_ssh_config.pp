#A puppet file to configure the client for my ubuntu server
$str = "PasswordAuthentication no
  FileIdentity ~/.ssh/school
  "
file { 'ssh_config':
  ensure => 'present',
  path     => '/etc/ssh/ssh_config',
  content => $str,
}
