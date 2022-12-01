# School REST API
## Video Demo:  https://youtu.be/qPlT3NfJZ70
## Description:

A REST API web-service that allows user to send http requests to work with students, groups or courses.

All CRUD operations are supported and data is stored in PostgreSQL as DBMS and SQLAlchemy as an ORM system to work with data.

The project consists of several files:
* app.py – Creates Flask app and defines API Resources
* api.py – Handles the main job in the project describing CRUD methods for each Resource
* models.py – Declares models for a db and defines relationships between them
* generator.py – Creates dummy data to fill the database
* test_api.py – Unit test for the API

The app has 3 main resources:
* Groups – `/api/<string:version>/groups`
* Students – `/api/<string:version>/students` (the default version should be `v1`)
* Courses – `/api/<string:version>/courses`

In order to send data via POST, PUT, DELETE methods user must provide a json object with required fields. Content-type must be defined and set to 'application/json'. A payload must be included in Body section of a request.

### Groups
____
#### POST method

*Parameters:*
* `name`: a string, required. A new group name

*Returns*: a json object containg created group's information

#### PUT method
*Parameters*:
* `id`: an integer, required. Existing group id
* `name`: a string, required. Group's new name

*Returns*: a json object containg updated group's information

#### DELETE method
*Parameters*:
* `id`: an integer, required. Existing group's id

*Returns*: a json object containg deleted group's information

### Students
____
#### POST method

*Parameters:*
* `first_name`: a string, required. Students first name
* `last_name`: a string, required. Students last name
* `group_id` : an integer, required. Group to which student will be assigned

*Returns*: a json object containg created student's information. By default there are no courses assigned to student, and returning json will contain empty list for 'courses' parameter

#### PUT method
*Parameters*:
* `id`: an integer, required. Existing student's id
* `first_name`: a string, not required. Must be set if changing student's first name
* `last_name`: a string, not required. Must be set if changing student's last name
* `group_id` : an integer,  not required. Must be set if changing student's group

*Returns*: a json object containg updated student's information

#### DELETE method
*Parameters*:
* `id`: an integer, required. Existing student's id

*Returns*: a json object containg deleted student's information

### Courses
____
#### POST method

*Parameters:*
* `name`: a string, required. A new course name
* `description`: a string, not required. A new course description

*Returns*: a json object containg created course's information

#### PUT method
*Parameters*:
* `id`: an integer, required. Existing course id
* `name`: a string, not required. Must be set if changing course's name
* `description`: a string, not required. Must be set if changing course's description

*Returns*: a json object containg updated course's information

#### DELETE method
*Parameters*:
* `id`: an integer, required. Existing course's id

*Returns*: a json object containg deleted course's information

