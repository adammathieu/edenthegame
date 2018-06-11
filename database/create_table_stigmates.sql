-- Table: stigmates
-- DROP TABLE stigmates;
-- stigmates Table 

SET search_path TO edenthegame;

CREATE TABLE stigmates
(	
	id  integer NOT NULL PRIMARY KEY,							
	name character varying(64) NOT NULL
);

INSERT INTO stigmates VALUES (1, 'destruction');
INSERT INTO stigmates VALUES (2, 'ordre');
INSERT INTO stigmates VALUES (3, 'protection');
INSERT INTO stigmates VALUES (4, 'changement');
INSERT INTO stigmates VALUES (5, 'chaos');	

COMMENT ON COLUMN stigmates.id IS 'stigmate id';
COMMENT ON COLUMN stigmates.name IS 'name of the stigmate';
