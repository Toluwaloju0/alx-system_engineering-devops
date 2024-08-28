package { 'nginx':
  ensure      => installed,
  configfiles => replace,
}
