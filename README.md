# Word Counter Application
Flask based HTTP service to consume text and return the number of words.


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
```
Linux system: Ubuntu 16.04 (Xenial) or later
python 3.5.2
pip
```

### Installing
Clone source code from git repo

```
$ git clone https://github.com/fernandorovai/WordCounter.git
```


Setup and activate virtual environment

```
$ virtualenv WordCounter -p python3
$ cd WordCounter
$ source ./bin/activate
```

Install python dependencies via pip

```
$ pip install -r requirements.txt   # python libraries
$ python -m spacy download en       # download english model
```

## Running the Server
Start the webserver
```
$ cd WordCounter 
$ python init.py

# to run webserver in debug mode, set app.debug var in init.py
app.debug = True
```
Expected output
```
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

### Request text processing (API)
Receive the number of words based on user's input text.
Server is expecting to receive a POST message with a determined field.

```
requestUrl    : http://localhost:5000/processText
method        : POST
dataStructure : bagOfText:"This is an example of text"              
```

Expected output:
```
outputStructure : {
                    "errorMsg": null,
                    "wordCounter": "6"
                  }
```

### Request text processing (Web)
Receive the number of words based on form user's input text.

```
1. Go to http://localhost:5000
2. Fill the form with text
3. Press submit button to receive the number of words
```

## Running the tests
The script webServerTestCase.py runs the following tests 
- **test_invalid_request            :** send a post request without form content
- **test_complete_post              :** send a post request with complete form content
- **test_empty_post                 :** send a post request with empty value
- **test_multiple_requests          :** send multi-thread post requests

To start the test case:
```
$ cd WordCounter
$ python webServerTestCase
```
Expected output:
```
Ran 4 tests in 500ms
OK
```

## Deployment

Flask’s built-in server is not suitable for production. Consider deploying the application to a WSGI Server.

For more information, check [Flask Documentation](http://flask.pocoo.org/docs/0.12/deploying/)

## Built With

* [Flask](http://flask.pocoo.org/)           - Microframework for Python
* [spaCY](https://www.spacy.io/)             - Package for Natural Language Processing

## Authors
* **Fernando Rodrigues Jr** - *Initial work* - [Fernando](https://github.com/fernandorovai)
