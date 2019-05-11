# Quick instructions

**Install requirements:**
* Install python
* Install virtualenv
    ```bazaar
    pip install virtualenv
    ```
* Make new virtualenv
    ```bazaar
    mkvirtualenv --python `which python` venv
    ```
* Activate the virtualenv (this will activate in bash, depending on what os and
 shell you are using you may need to change this to .csh, .fish, .bat)
    ```bazaar
    source venv/bin/activate
    ```
* Install the requirements
    ```bazaar
    pip install -r requirements/base.txt
    ```
 