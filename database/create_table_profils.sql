-- Table: profils
-- DROP TABLE profils;
-- profils Table 

SET search_path TO edenthegame;

CREATE TABLE profils
(	
	id  integer NOT NULL PRIMARY KEY,	
	profil jsonb
);

COMMENT ON COLUMN profils.id IS 'profil id';
COMMENT ON COLUMN profils.name IS 'profil description';
