/****************** starting *******************/
# install postgresql:
    $ sudo apt update
    $ sudo apt install -y postgresql postgresql-contrib

# Start PostgreSQL server:
    $ sudo service start postgresql

# Check connections to Database:
    $ sudo -i -u postgres

# After log in to postgres, run this:
    $ psql

# To list Database avalable, run this:
    postgres=# \l
# To display list of relations in Database:
    postgres=# \d

# To exit, run this:
    postgres=# \q

/****************** BASIC OPERATIONS *******************/
# see in '.sql' files
  Creating a table
  Inserting data into a table
  Reading data from a table
  Updating data in a table
  Deleting data from a table
