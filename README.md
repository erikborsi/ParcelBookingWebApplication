# Parcel Booking Web Application

Assignment for Advanced Server Development  

A Python install is mandatory! Hopefully, You got Python installed on Your system if You are here on GitHub!  

Installing Django is required to run the development server!  
Unix type operating system terminal: python -m pip install Django  
Windows type operating system terminal: py -m pip install Django  

RUN THE SERVER IN TERMINAL: python manage.py runserver  
Obviously, You need to be in the folder where manage.py is located!

In production environment the debug should be set to False on line 26 in the settings.py file.

The database filled with randomly generated data.

The goal was to create a back-end application with a database, where an authorised user can add customers. Also, the user can add parcel and allocate it to a customer. One specific parcel can only be allocated to one specific customer, but a specific customer can have more than one specific parcels. 

Django built-in Admin page was used to create the system. The assignment's requirements are limited and fullfiled with the current setup. So, the utilisation of Django is limited as well in that regard. There is much more that Django can do.

Official Django documentation: https://www.djangoproject.com/
