# A file to kill a command
exec { 'kill_process':
  command => '/usr/bin/pkill killmenow',
}
