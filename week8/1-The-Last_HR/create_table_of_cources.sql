DROP TABLE IF EXISTS cources;
CREATE TABLE cources(id INTEGER PRIMARY KEY, name TEXT);

INSERT INTO cources(name) VALUES('NodeJS');
INSERT INTO cources(name) VALUES("Programming 101 v2");
INSERT INTO cources(name) VALUES("Android");
INSERT INTO cources(name) VALUES("Core Java v2");
INSERT INTO cources(name) VALUES("Core Java");
INSERT INTO cources(name) VALUES("Frontend JavaScript v2");
INSERT INTO cources(name) VALUES("Frontend JavaScript v3");
INSERT INTO cources(name) VALUES("Frontend JavaScript");
INSERT INTO cources(name) VALUES("System C");
INSERT INTO cources(name) VALUES("Programming 101 v3");
INSERT INTO cources(name) VALUES("Ruby on Rails");
INSERT INTO cources(name) VALUES("Core Ruby");
INSERT INTO cources(name) VALUES("Programming 0");

CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT, profile TEXT);

CREATE TABLE IF NOT EXISTS relations(
  student_id INTEGER,
  course_id INTEGER,
  FOREIGN KEY(student_id) REFERENCES students(id),
  FOREIGN KEY(course_id) REFERENCES courses(id));
