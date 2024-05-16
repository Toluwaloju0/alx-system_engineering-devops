# A file to kill a command
exec { 'kill_killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep killmenow',
}
