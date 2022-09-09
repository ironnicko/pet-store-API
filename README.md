# Hey!

## This API uses Django and Djangorestframework for the backend, and SQLite3 for database.
### NOTE: SQLite3 can easily be replaced by other relational Databases since Django has it's own ORM
<p>
This was a fun experience to showcase that I can code with a project.
Let me get started with the credentials needed to run this API:
</p>
1) I have included a requirements.txt so that you can install all dependencies easily

2) you will need the include the username and password in your authentication header 
[admin - both password and username]

3) make sure to makemigrations and migrate before you play around with the Database.
  - <code>python3 manage.py makemigrations</code>
  - <code>python3 manage.py migrate</code>

with all that aside now onto the things that I built:

1) I made a model for exactly what was mentioned - pet_name, pet_ID, pet_owner_name, pet_age, pet_type, and pet_gender. I was tempted to make a relationship between owner and pets, but realised I shouldn't overcomplicate things.

2) end points are - /api/pets
                  - /api/pets/<int:pk>/

    the first end point accepts GET, POST, and DELETE[delete everything] requests, and the second end point accepts GET, PUT, and DELETE. Basically a CRUD application like mentioned.

3) not something I build buit something to keep in mind when trying out the API is that always add "/" at the end of the url. This is really important.

With all that said, there's something I feel like I should let you know. I haven't done development in a while now because I have been busy doing Codeforces. So my skills were dusty before I began this assignment. But thanks to this assignment I was able to brush up on my backend skills.

## API Images:
<img width="1303" alt="image" src="https://user-images.githubusercontent.com/66690978/189388818-e04f44d1-6adb-4f48-9f6c-1ff7ed8ca758.png">
<br>

<img width="1303" alt="image" src="https://user-images.githubusercontent.com/66690978/189389267-4418c05b-4105-4401-84a4-a82ea47afce7.png">
<br>

<img width="1303" alt="image" src="https://user-images.githubusercontent.com/66690978/189389496-74cb45d4-0075-4bfd-8005-679e25fada34.png">

