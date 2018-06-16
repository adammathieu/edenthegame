-- Table: tactics

SET search_path TO edenthegame;
DROP TABLE tactics;
ALTER SEQUENCE tactics_id_seq RESTART WITH 1;
CREATE TABLE tactics
(	
	id SERIAL PRIMARY KEY NOT NULL,	
	tactic jsonb
);

COMMENT ON COLUMN tactics.id IS 'tactic id';
COMMENT ON COLUMN tactics.tactic IS 'tactic description';
