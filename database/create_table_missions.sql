-- Table: missions
-- DROP TABLE missions;
-- missions Table 

SET search_path TO edenthegame;

CREATE TABLE missions
(	
	id  integer NOT NULL PRIMARY KEY,	
	mission jsonb
);

COMMENT ON COLUMN missions.id IS 'mission id';
COMMENT ON COLUMN missions.name IS 'mission description';
