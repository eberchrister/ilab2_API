CREATE TABLE reminder (
	id INTEGER PRIMARY KEY,
	task TEXT NOT NULL,
	date DATE NOT NULL,
	time TIME
);

CREATE TABLE history (
  	task_id INTEGER NOT NULL,
  	status VARCHAR(255) NOT NULL,
  	date DATE not NULL,
  	time DATE NOT NULL
);

INSERT INTO reminder(task, date, time)
VALUES ('iLab2 - oral attestation 2', '2023-02-01', '14:00');

INSERT INTO reminder(task, date)
VALUES ('iLab2 - YE first draft', '2023-01-31');

INSERT INTO history(task_id, status, date, time)
VALUES (1, 'CREATED', DATE('now'), TIME('now'));

INSERT INTO history(task_id, status, date, time)
VALUES (2, 'CREATED', DATE('now', '+1 day'), TIME('10:20:30','+1 hours','+20 minutes'));

INSERT INTO history(task_id, status, date, time)
VALUES (1, 'EDITED', DATE('now'), TIME('now', '37 minutes'));