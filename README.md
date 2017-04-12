# SarprasI

### Programming Language

<ul>
	<li>Python 2.7.x</li>
</ul>

-----

### Frameworks

-----

<ul>
	<li>Django 1.11b1</li>
	<li>AngularJS</li>
</ul>

-----

### Problems and Solutions

-----

**Prob:**
<b>django.db.utils.OperationalError: (1044, "Access denied for user ''@'localhost' to database 'sarpras_peminjamanruang'")</b>

**Solution:**
<ul>
	<li>Go to your project root directory</li>
	<li>Run **python tambahuser.py**</li>
	<li>Go to MySQL prompt (mysql -u root)</li>
	<li>Run **SELECT host,user,password,Grant_priv,Super_priv FROM mysql.user;**</li>
	<li>You should see the new user **admin_penjadwalan** with host **localhost**</li>
	<li>If the value of Grant_priv or Super_priv is set to 'N', run this: **UPDATE mysql.user SET Grant_priv='Y', Super_priv='Y' WHERE User='admin_penjadwalan';**</li>
	<li>Quit from the MySQL prompt. Execute **python manage.py runserver** and everything should be OK</li>
</ul>