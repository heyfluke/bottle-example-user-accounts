Minimal site using [Bottle](http://bottlepy.org/) and which supports
user accounts.

Requires sqlite3. On Ubuntu, that's `sudo apt-get install sqlite3`.

To run this webapp:

 1. Clone the repo from github:

        cd ~/temp
        git clone git://github.com/uvtc/bottle-example-user-accounts.git
        cd bottle-example-user-accounts

 2. Acquire the bottle.py and bottle_sqlite.py files, then drop them
    into this directory.

 3. Create the database:

        cd db
        sqlite3 site.db < init-db.sql
        cd ..

 4. Run the site:

        python user-create-login-logout.py

 5. Visit: <http://localhost:8080/> to try it out.

Feedback welcome. `:)`
