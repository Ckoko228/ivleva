INSERT INTO languages(name) VALUES ('English');
INSERT INTO languages(name) VALUES ('Estonian');
INSERT INTO languages(name) VALUES ('Russian');
INSERT INTO authors(first_name, last_name) VALUES('Christian','Ullenboom');
INSERT INTO authors(first_name, last_name) VALUES('Devlin Basilan','Duldulao');
INSERT INTO authors(first_name, last_name) VALUES('Seiji','Ralph');
INSERT INTO books(title, language_id) VALUES ('Spring Boot 3 and Spring Framework 6',
1);
INSERT INTO books(title, language_id) VALUES ('Spring Boot and Angular: Hands-on full
stack web development with Java, Spring, and Angular', 1);
INSERT INTO book_author(book_id, author_id) VALUES (1, 1);
INSERT INTO book_author(book_id, author_id) VALUES (2, 2);
INSERT INTO book_author(book_id, author_id) VALUES (2, 3);
