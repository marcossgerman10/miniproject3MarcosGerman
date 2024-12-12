# INF601 - Advanced Programming in Python
# Marcos German
# Mini Project 3

# Media Tracker Web App

This project is a web application to track movies and series you have watched. Users can add movies with ratings and reviews and manage their progress in TV series by tracking the season and episode they are on. The application includes login/logout functionality, and each user’s data is private and personalized.

## Description

The Media Tracker Web App allows users to:

- Add movies with details like title, rating, and review.

- Add TV series with details like title, rating, season, episode, and status (watching/completed).

- View lists of movies and series sorted by user.

- Securely log in and out, ensuring each user’s data is private.

## Dependencies
- Python 3.x

#### Libraries:

- flask

- jinja2

- werkzeug

- sqlite3

## Installing

1. Clone the repository: 
```
  git clone https://github.com/marcossgerman10/miniproject3MarcosGerman.git
```
2. Navigate to the Project Directory:
```
    cd miniproject3MarcosGerman
```
3. Install the Required Python Packages:
```
    pip install -r requirements.txt
```
4. Initialize the Database:
```
    flask init-db
```

## Executing program

1. Ensure all dependencies are installed and you are in the project directory.
2. Run the Flask development server:
```
    flask run
```
3. Open a web browser and navigate to:
```
    http://127.0.0.1:5000
```
4. Register a new account, log in, and start tracking your movies and series!

## Help 
If you encounter issues, ensure the following:

- Flask and all required libraries are installed properly.

- You have initialized the database with the flask init-db command.

- The application is running on the specified port (default: 5000).

## Authors
Marcos German

## Version History 

- 0.1

    - Initial release with basic functionality for adding and viewing movies and series.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
Inspiration, code snippets, etc.

- Flask
- SQLite