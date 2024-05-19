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

## How to import new invoices

- Login to console.hetzner.cloud with an owner account of flipdot
    - It's not enough if you have admin permissions on your personal account.
      Invoices are just issued to the account owner
- On the top right, navigate to "Invoices"
- Download all CSV files that are not yet included in this repo
- Move them into some directory
- Execute `./import_hetzner_invoices.sh <YOUR-DIRECTORY>`
- Verify everything looks fine by running the application
    - See above
- `git add data/running_expenses/hcloud/`
- commit and push
