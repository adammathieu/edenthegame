-- Table: factions

SET search_path TO edenthegame;
DROP TABLE factions;

CREATE TABLE factions
(	
	id  integer NOT NULL PRIMARY KEY,							
	name character varying(64) NOT NULL
);

INSERT INTO factions VALUES (1, 'jokers');
INSERT INTO factions VALUES (2, 'bamaka');
INSERT INTO factions VALUES (3, 'matriarcat');
INSERT INTO factions VALUES (4, 'convoi');
INSERT INTO factions VALUES (5, 'isc');
INSERT INTO factions VALUES (6, 'horde');
INSERT INTO factions VALUES (7, 'resistance');
INSERT INTO factions VALUES (8, 'askaris');
INSERT INTO factions VALUES (9, 'nephilim');
INSERT INTO factions VALUES (10, 'angesdedante');
INSERT INTO factions VALUES (11, 'cnj');

COMMENT ON COLUMN factions.id IS 'faction id';
COMMENT ON COLUMN factions.name IS 'name of the faction';
