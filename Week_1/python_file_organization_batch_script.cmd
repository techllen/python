::README
::script for creating folder structure for python
::To use this script just copy where you want your files to be 
::created and open the file python_file_organization_batch_script by clicking it

@echo off

::creating main directory
mkdir python

::move into python directory create child directory ajax for python
cd python
mkdir ajax

::moving into ajax folder and create 2 child directories
cd ajax
mkdir ajax_api
mkdir ajax_flask

::move back to the parent folder and create flask folder
cd ../
mkdir flask

::move into flask folder to create fundamentals folder
cd flask
mkdir fundamentals

::move back to the parent folder and create flask_mysql folder
cd ../
mkdir flask_mysql

::move into flask_mysql folder to create its child folders
cd flask_mysql
mkdir belt_review
mkdir crud
mkdir db_connection
mkdir validation

::move back to the parent folder and create fundamentals folder
cd ../
mkdir fundamentals

::move into fundamentals folder to create its chidren
cd fundamentals
mkdir extras
mkdir fundamentals
mkdir introduction
mkdir oop

::move back to the parent folder and create mysql folder
cd ../
mkdir mysql

::move into mysql folder and create its children folders
cd mysql
mkdir erd
mkdir queries

echo COMPLETE!!!





