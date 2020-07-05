# flipdot-transparenz-reports

Visit http://transparenz.flipdot.org/

## Running locally

Install dependencies:

    $ pipenv sync

(You can install pipenv with `pip install pipenv`. More information on pipenv: https://pypi.org/project/pipenv/)

Run the interactive version if you are going to change some python code:

    $ FLASK_DEBUG=1 pipenv run src/app.py
    
Or build the static version:

    $ pipenv run src/freeze.py
    
The static files are inside `./build/`