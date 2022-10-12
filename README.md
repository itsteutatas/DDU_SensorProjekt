# DDU-SensorProjekt

## Intro
  The view on the climate is ever changing and therefore 
  we must take extreme messures as power prices are rising higher and higher.
  
  Our product will not only ensure optimal management of temperatures in rooms
  but also gives a visability to the customer while giving them access 
  to the temperatures in the diffrent office and or classrooms
  while still being accessible from everywhere with the correct login

## Scope
- [ ] Frontend dashboard
  - Django?
  - Pull data from database
- [ ] Arduino to collect data
  - Temperature
  - Humidity
  - Graphs
  - Anything else?
- [ ] Documentation
  - User guide


## Userguide
- [ ] Setup
  - Kør filen setup.sql for at lave og sæt databasen op
  - Tilslut Arduino efter Figur 1 og tilslut til computer med USB
  - Eventuelt flash “Arduino setup.txt” hvis det ikke allerede er på
  - Kør “pip install -r requirements.txt” i projektmappen for at installere de påkrævede packages
  - Åben XAMPP og slå MySQL til.
  - Kør “python manage.py createsuperuser” i mappen “/frontend” i projekt mappen for at lave en super user. Efterlad alle andre end “username” og “password” blanke.
  - Kør “python manage.py shell” i samme mappe og kør kommandoerne fra normalUser_setup.txt for at lave en normal bruger.
  - Kør “exit()” for at komme ud af shellet.
  - Kør “python manage.py runserver” i samme mappe for at starte webserveren.
- [ ] Usage
  - Naviger til http://127.0.0.1:8000/ hvor webserveren kører
  - Login med admin:admin eller normalUser:normalUser





## Knowledge usage
<p align="left">
<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>
<a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/html5-colored.svg" width="36" height="36" alt="HTML5" /></a>
<a href="https://www.w3.org/TR/CSS/#css" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/css3-colored.svg" width="36" height="36" alt="CSS3" /></a>
<a href="https://www.mysql.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/mysql-colored.svg" width="36" height="36" alt="MySQL" /></a>
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/django-colored-dark.svg" width="36" height="36" alt="Django" /></a>
</p>
