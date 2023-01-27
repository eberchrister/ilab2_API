create table light (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    red INTEGER CHECK (red >= 0 AND red <= 255),
  	green INTEGER CHECK (green >= 0 AND green <= 255),
  	blue INTEGER CHECK (blue >= 0 AND blue <= 255),
  	state INTEGER CHECK (state >= 0 and state <=1)
);
INSERT INTO light (red, green, blue, state) VALUES (0,0,0,0);
INSERT INTO light (red, green, blue, state) VALUES (0,0,0,0);
INSERT INTO light (red, green, blue, state) VALUES (0,0,0,0);