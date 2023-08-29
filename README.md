# Code_squad-customer_management
This is a aviation customer history and data management system developed with django.
Django provides various features that prevent the injection of mallicious scripts via XSS,CSRF also SQL injection is nearly imposible in Django as it uses ORM.
So one can safely say that this web app is secure and robust.

This app is not for the use of clients rather it is for the sole purpose of managing of via airline service providers to manage customer details.
Also the user accounts for those who manage the site can only be done by the admin.steps to create a admin account is also explained below.

## How to run this?
1)make sure you have git,python,pip and pipenv installed <br />
2)clone this repo into your computer 
  i)you can do that by opening a termial navigate to the directory u want and typing <br />
        ```git clone https://github.com/vimalathithan17/code_squad-customer_management/```  <br />
3)now in the terminal type <br />
        ```cd code_squad-customer_management-main```<br />
4)now type<br />
        ```pipenv install --ignore-pipfile```<br />
this will create a virtual evnironment and download all the dpendnecies.
make sure to copy the location of the virtual evnironment
5)to enter the virtualenvironment type <br />
        ```pipenv shell``` <br />
6)to launch the app type<br />
        ```python manage.py runserver```<br />
this will oper port 8000 at the ip address 127.0.0.1 (localhost)
## How to create a admin account?
inside the virtual environment,type<br />
        ```python manage.py createsuperuser```<br />
this will create a admin user
to access the django admin site in your web browser,
enter  http://127.0.0.1:8000/admin 
or     localhost:8000/admin
now login with the credentials that you have created
now you can create other users by clicking the +Add symbol near the User section.

## Our team 
**code squad**
## Members
Vimalathithan D<br />
Thaarugeshwari K S<br />
Saravana Kumar S<br />
Sanjay A C<br />
