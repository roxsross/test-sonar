"# pyapi"

File Structure

API STRUCTURE:

current folder Structure

PYAPI(main folder)
        ()myapp
        ()app
        ()dbsqlite3
        ()manage.py

Our Django API Structure follows:
    myapp(main folder)
        ()myapp
        ()app
                ()category
                ()order
                ()User
                ()product
                ()payment
        ()dbsqlite3
        ()manage.py


               How to run:
Install Dependencies in Terminal:

altgraph==0.17.2
asgiref==3.4.1
Babel==2.9.1
Django==3.2.8
djangorestframework==3.12.4
future==0.18.2
gunicorn==20.1.0
pefile==2021.9.3
Pillow==8.4.0
pyinstaller==4.5.1
pyinstaller-hooks-contrib==2021.3
PyMySQL==1.0.2
pytube==11.0.1
pytz==2021.3
pywin32-ctypes==0.2.0
serializers==0.2.4
sqlparse==0.4.2
tkcalendar==1.6.1
whitenoise==4.0

after installations of dependencies clone the entire repo to your local computer.
run the project with python manage.py
Copy the local host URL and paste in browser: http://127.0.0.1:8000/