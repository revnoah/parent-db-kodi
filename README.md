# Parent Db for Kodi

## A Web Utility for Kodi

**Parent Db for Kodi** is a program to help manage multiple Kodi databases on a local network. It uses multiple 
MySQL databases to maintain copies of a Kodi database. The primary purpose of this program is to manage a kid-
friendly copy of video catalogue based on the main database. This is managed through a web interface and a 
local database to track the changes.

## Installing The Program

The program requires python to run and is built using the Flask framework.

1. Install python and other prerequisites needed for Flask. [Install Flask](https://flask.palletsprojects.com/en/1.1.x/installation/#dependencies)

## Settings

The program adds a menu item to the Settings menu. It is advisable to review and, if desired, update 
these settings after activating the program.

## Using This Program

This program runs a web application on a particular port, defaulting to 5000 and specified on startup. To access the web application, visit [Web Interface](http://localhost:5000)

$ flask run

## Contributing

Please review the [CONTRIBUTING.md](CONTRIBUTING.md) file if you are interested in helping develop or 
maintain this program. Also, please be aware that contributors are expected to adhere to the 
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and use the [PULL_REQUEST_TEMPLATE.md](PULL_REQUEST_TEMPLATE.md) 
when submitting code.

## About This Program

This program was created by Noah Stewart to help manage multiple Kodi apps on a local network. He wanted a way to separate approved children's programs from the general catalogue, and that way should preferably be through a web interface rather than the Kodi application.

## License

The program **Parent Db for Kodi** is open-sourced software licensed under the ISC license.
