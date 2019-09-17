#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

from app import settings
from app import util
from app import routes
from app import mysql_connect
