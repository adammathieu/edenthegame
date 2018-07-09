-- Table: states

SET search_path TO edenthegame;
DROP TABLE states;
CREATE TABLE states
(	
	id  integer NOT NULL PRIMARY KEY,							
	name character varying(64) NOT NULL,
	description text
);

COMMENT ON COLUMN states.id IS 'state id';
COMMENT ON COLUMN states.name IS 'name of the state';
COMMENT ON COLUMN states.description IS 'description of the state';
