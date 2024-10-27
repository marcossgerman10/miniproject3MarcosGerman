DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS series;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  firstname TEXT NOT NULL,
  lastname TEXT NOT NULL
);

CREATE TABLE movies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  rating INTEGER CHECK(rating >= 1 AND rating <= 10),
  review TEXT,
  added_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE series (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  rating INTEGER CHECK(rating >= 1 AND rating <= 10),
  review TEXT,
  episode INTEGER DEFAULT 1,
  status TEXT CHECK(status IN ('watching', 'completed')) DEFAULT 'watching',
  added_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES user (id)
);