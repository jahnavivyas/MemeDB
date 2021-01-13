drop table era, aesthetic, community_circulates, internet_personality, meme, meme_belongs_to, meme_has_an, meme_in_era, meme_posted_on, meme_text_overlays, memetext, personality_belongs_to_community, personality_belongs_to_subculture, personality_posts, real_life_community, source, subculture cascade;


/* entity sets */

CREATE TABLE meme(
	id int,
	subject varchar(256),
	tags varchar(512),
	format varchar(256),
	category varchar(256),
	content varchar(256),
	PRIMARY KEY (id)
);

CREATE TABLE memetext(
	id int,
	text varchar(256),
	PRIMARY KEY (id)
);

CREATE TABLE source(
	website varchar(512),
	description varchar(256),
	PRIMARY KEY (website)
);

CREATE TABLE subculture(
	name varchar(256),
	description varchar(256),
	popularity varchar(256),
	PRIMARY KEY (name)
);

CREATE TABLE aesthetic(
	name varchar(256),
	description varchar(256),
	colors varchar(256),
	PRIMARY KEY (name)
);

CREATE TABLE internet_personality(
	name varchar(256),
	description varchar(256),
	popularity varchar(256),
	PRIMARY KEY (name)
);

CREATE TABLE real_life_community(
	name varchar(256),
	description varchar(256),
	language varchar(256),
	PRIMARY KEY (name)
);
CREATE TABLE era(
	name varchar(256),
	origin_year int,
	ending_year int,
	description varchar(256),
	PRIMARY KEY (name)
);

/* relationship sets */

CREATE TABLE meme_text_overlays(
	position varchar(256),
	memetext_id int,
	meme_id int,
	FOREIGN KEY (meme_id) REFERENCES meme (id),
	FOREIGN KEY (memetext_id) REFERENCES memetext (id),
	PRIMARY KEY (memetext_id, meme_id)
);
CREATE TABLE meme_posted_on(
	source_website varchar(256) ,
	meme_id int,
	FOREIGN KEY (meme_id) REFERENCES meme (id),
	FOREIGN KEY (source_website) REFERENCES source (website),
	PRIMARY KEY (source_website, meme_id)
);
CREATE TABLE meme_has_an(
	meme_id int UNIQUE,
	aesthetic_name varchar(256),
	FOREIGN KEY (meme_id) REFERENCES meme (id),
	FOREIGN KEY (aesthetic_name) REFERENCES aesthetic (name),
	PRIMARY KEY (meme_id, aesthetic_name)
);
CREATE TABLE meme_belongs_to(
	meme_id int UNIQUE,
	subculture_name varchar(256),
	FOREIGN KEY (meme_id) REFERENCES meme (id),
	FOREIGN KEY (subculture_name) REFERENCES subculture (name),
	PRIMARY KEY (meme_id, subculture_name)
);
CREATE TABLE meme_in_era(
	meme_id int UNIQUE,
	era_name varchar(256),
	FOREIGN KEY (meme_id) REFERENCES meme(id),
	FOREIGN KEY (era_name) REFERENCES era(name),
	PRIMARY KEY (meme_id)
);
CREATE TABLE personality_belongs_to_subculture(
	name varchar(256),
	subculture_name varchar(256),
	FOREIGN KEY (name) REFERENCES internet_personality (name),
	FOREIGN KEY (subculture_name) REFERENCES subculture (name),
	PRIMARY KEY (name, subculture_name)
);
CREATE TABLE personality_belongs_to_community(
	name varchar(256),
	real_life_community_name varchar(256),
	FOREIGN KEY (name) REFERENCES internet_personality (name),
	FOREIGN KEY (real_life_community_name) REFERENCES real_life_community (name),
	PRIMARY KEY (name, real_life_community_name)
);
CREATE TABLE personality_posts(
	meme_id int ,
	name varchar(256),
	FOREIGN KEY (meme_id) REFERENCES meme (id),
	FOREIGN KEY (name) REFERENCES internet_personality (name),
	PRIMARY KEY (meme_id, name)
);
CREATE TABLE community_circulates(
	meme_id int,
	name varchar(256),
	FOREIGN KEY (meme_id) REFERENCES meme (id),
	FOREIGN KEY (name) REFERENCES real_life_community (name),
	PRIMARY KEY (meme_id, name)
);

