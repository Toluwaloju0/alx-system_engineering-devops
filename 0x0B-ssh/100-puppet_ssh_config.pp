#A puppet file to configure the client for my ubuntu server
$str = "Host: 503789-web-01
	HostName 100:25:22:54
	PasswordAuthentication no
	FileIdentity ~/.ssh/school
  "
file { 'ssh_config':
  ensure => 'present',
  path     => 'ssh_config',
  content => $str,
}
