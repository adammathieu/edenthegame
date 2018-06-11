-- Table: tactics
-- DROP TABLE tactics;
-- tactics Table 

SET search_path TO edenthegame;

CREATE TABLE tactics
(	
	id  integer NOT NULL PRIMARY KEY,	
	tactic jsonb
);

COMMENT ON COLUMN tactics.id IS 'tactic id';
COMMENT ON COLUMN tactics.tactic IS 'tactic description';
