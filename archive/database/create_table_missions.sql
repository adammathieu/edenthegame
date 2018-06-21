-- Table: missions

SET search_path TO edenthegame;
DROP TABLE missions;
CREATE TABLE missions
(	
	id  integer NOT NULL PRIMARY KEY,	
	mission jsonb
);

COMMENT ON COLUMN missions.id IS 'mission id';
COMMENT ON COLUMN missions.name IS 'mission description';
