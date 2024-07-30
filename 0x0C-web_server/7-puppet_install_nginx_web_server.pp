#A puppet code to install nginx and configure it
package { 'systemctl':
	ensure => installed,	
}
package { 'nginx':
	ensure => installed,
}

package { 'ufw':
	ensure => installed,
}
