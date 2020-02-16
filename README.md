# USPS

This is a demo application for LTGC that is a proof of concept using Vue and Flask

## Prerequisites
This project was built with python 3.8.1, but will likely work with other versions. This project makes use of npm version 6.13.7 and node 12.16.0, but will likely work with other versions.

## Setup
This code was built in windows 10, but should be able to run in any environment with appropriate adjustments (changing \ to /, for example). The application server and web server run in two separate command line instances, and operate on ports 5000 (app) and 8080 (web). As such, these ports will need to be available in order to run this.

### Application Server setup

```bash
# perform all of this in the app folder
cd app
# build the environment
py -m venv env
# activate the environment
env\Scripts\activate
# install flask
pip install flask
# set file to run
set FLASK_APP=app.py
# start the application server
flask run

```

### Web Server Setup

```bash
# perform all of this in the web folder
cd web
# build the environment
npm install
# start the web server
npm start

```

### Running the application server
```bash
# start the application server
flask run

```

To test, navigate a browser to
```
http://localhost:5000
```
to see the app code running. For more information, see the api definition below.

### Running the web server

```bash
# start the web server
npm start

```
To use, navigate a browser to
```
http://localhost:8080
```

## Usage
The address book can be used in a variety of ways:

### Load an address book from CSV file
TODO probably won't do this, looking into server state & local storage

TODO validate on input

TODO overwrite

TODO merge

### Save the address book to a CSV file
TODO probably won't do this, looking into server state & local storage

TODO write to fs via browser

### View all addresses
By Default, when you open the web application all addresses in your address book will be shown. If
you don't have any yet, none will be shown.

### Input an address
The same form is used to edit or create an address. In these cases, form validation will indicate
what is required and where errors may exist. The Name, Address, City, State, and Zip are required.
Additionally, it is required that the zip be located within the city and state. If the zip is
provided but the city is empty, the city will be populated with the appropriate zip (if only one
city is provided by USPS).

TODO auto-lookup zip code for city / state

TODO auto-lookup city / state

### Other API uses
TODO find all cities within zip

TODO unit tests?

TODO offline support

## API
If the web app isn't your cup of tea, the following endpoints have been defined and can be consumed by hitting port `5000` directly, or by hitting port `8080/app`. The web server proxies all traffic from /app to the application server at port 5000.

TODO - add all api endpoints defined here
