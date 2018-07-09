-- Table: profils

SET search_path TO edenthegame;
DROP TABLE profils;
CREATE TABLE profils
(	
	id  integer NOT NULL PRIMARY KEY,	
	profil jsonb
);

COMMENT ON COLUMN profils.id IS 'profil id';
COMMENT ON COLUMN profils.name IS 'profil description';
