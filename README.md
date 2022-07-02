# flipdot-transparenz-reports

Visit http://transparenz.flipdot.org/

## Running locally

Install dependencies:

    $ poetry install

More information on poetry: https://python-poetry.org/docs/#installation

Run the interactive version if you are going to change some python code:

    $ FLASK_DEBUG=1 poetry run src/app.py
    
Or build the static version:

    $ poetry run src/freeze.py
    
The static files are inside `./build/`
