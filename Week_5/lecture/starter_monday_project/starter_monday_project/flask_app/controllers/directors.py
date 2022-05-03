from flask_app import app # Import the app
from flask import render_template, redirect, session, request
# Import your models here!
from flask_app.models import director, movie

# Where we will define our routes - we'll identify them in Monday's office hour