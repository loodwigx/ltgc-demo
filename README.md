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
# install requests so we can use the flask server to talk to usps
pip install requests
# install xmltodict because usps uses xml and I've made peace with that
pip install xmltodict
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

### View all addresses
By Default, when you open the web application all addresses in your address book will be shown. If
you don't have any yet, none will be shown.

### Input an address
The same form is used to edit or create an address. In these cases, form validation will indicate
what is required and where errors may exist. The Name, Address, City, State, and Zip are required.
If the zip is provided but the city is empty, the city will be populated with the appropriate zip.

If an inadequate amount of information is provided to usps (such as a partial address), the server
will respond with a 400. This is treated as normal, and the app will simply "stop trying to help"
so long as the data from the server continues to be a 400. Bear in mind that the conditions for help
are either

 - There is a zip code but there is no city
 - There is an address and city

In the latter case, if the address and city are valid, but the zip is invalid (according to USPS),
the zip code will be corrected to what USPS says it should be automatically.

#### Fun Gotcha

Apparently USPS doesn't like the pound / hashtag in the address (123 Fake St. #Y). This is
considered malformed XML. This code handles the exception by just assuming it's inconclusive, and
therefore returns a 400 and does nothing.

### Other uses
TODO handle error for USPS and display it to the user

TODO add index to address table

TODO refactor edit to be smaller

TODO add support for 4 digit zip suffix

TODO persist DB maybe

TODO look into that hashtag USPS issue

## API
If the web app isn't your cup of tea, the following endpoints have been defined and can be consumed by hitting port `5000` directly, or by hitting port `8080/app`. The web server proxies all traffic from /app to the application server at port 5000.

```GET /```

returns a json ping-pong

```GET /address```

returns all addresses sorted by name

```POST /address```

creates a new address and responds with a 201.
expects a JSON payload containing strings for the various address fields
Responds with a 400 - Malformed data if the data supplied cannot make an address

```GET /address/<address_id>```

returns the address at the given integer address id
responds with a 400 if you send it an id that can't find anything

```PUT /address/<address_id>```

updates the address at the given address id and responds with a 204
expects a JSON payload containing strings for the various address fields
responds with a 400 - Malformed data if the data supplied cannot update the address

```DELETE /address/<address_id>```

deletes the address at the given address id and responds with a 204

```GET /city-state/<zip_code>```

attempts to get the city and state given the supplied zip code
responds with a 400 - Results Inconclusive if the zip provided doesn't yield results

```GET /zip/<address>/<city>/<state>```

attempts to get the zip given the supplied address, city, and state
the address is expected to be base64 encoded
responds with a 400 - Results Inconclusive if the zip cannot be determined with the supplied data
