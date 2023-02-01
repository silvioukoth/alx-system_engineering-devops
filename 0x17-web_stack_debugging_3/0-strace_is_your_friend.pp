#Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

file {'/var/www/html/wp-settings.php':
  ensure => present
}
exec { 'wordpress':
  command => "sed -i s/phpp/php/g /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin/'
}
