#A script to add a custom header to nginx file
$content = "add_header X-served-by $(localhost)"
file { '/etc/nginx/sites-available/default':
  
