# Adding a new hetzner invoice

If you want to add a new monthly report, download the csv and the pdf file from hetzner.
We will use https://pypi.org/project/hetzner-fix-report/ to extract desired information from the pdf file.

Install it via pip (`pip install hetzner-fix-report==0.11.0`) and run it:

    $ hetzner-fix-report <path-to-csv> <path-to-pdf> -o data/running_expenses/hcloud/YYYY-MM-DD.csv
    
Make sure the plot looks correctly and check in the new csv file.
