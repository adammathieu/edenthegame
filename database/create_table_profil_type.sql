-- Table: profil_types

SET search_path TO edenthegame;
DROP TABLE profil_types;
CREATE TABLE profil_types
(	
	id  integer NOT NULL PRIMARY KEY,	
	name character varying(64) NOT NULL
);

INSERT INTO profil_types VALUES (1, 'humain');
INSERT INTO profil_types VALUES (2, 'mutant');
INSERT INTO profil_types VALUES (3, 'janissaire');
INSERT INTO profil_types VALUES (4, 'beteferoce');
INSERT INTO profil_types VALUES (5, 'chaka');	
INSERT INTO profil_types VALUES (6, 'sorcier');
INSERT INTO profil_types VALUES (7, 'dompteur');
INSERT INTO profil_types VALUES (8, 'degenere');
INSERT INTO profil_types VALUES (9, 'robot');
INSERT INTO profil_types VALUES (10, 'familier');	
INSERT INTO profil_types VALUES (11, 'escorteur');
INSERT INTO profil_types VALUES (12, 'pisteur');
INSERT INTO profil_types VALUES (13, 'convoyeur');
INSERT INTO profil_types VALUES (14, 'pasteur');
INSERT INTO profil_types VALUES (15, 'seraphin');
INSERT INTO profil_types VALUES (16, 'hierophante');
INSERT INTO profil_types VALUES (17, 'dominant');
INSERT INTO profil_types VALUES (18, 'krampus');
INSERT INTO profil_types VALUES (19, 'cyber');
INSERT INTO profil_types VALUES (20, 'controleur');
INSERT INTO profil_types VALUES (21, 'drone');
INSERT INTO profil_types VALUES (22, 'bot');
INSERT INTO profil_types VALUES (23, 'pyromane');
INSERT INTO profil_types VALUES (24, 'soeur');
INSERT INTO profil_types VALUES (25, 'esclave');
INSERT INTO profil_types VALUES (26, 'inquisitrice');
INSERT INTO profil_types VALUES (27, 'ordrenoire');
INSERT INTO profil_types VALUES (28, 'ordrerouge');
INSERT INTO profil_types VALUES (29, 'ordrevert');
INSERT INTO profil_types VALUES (30, 'templiere');
INSERT INTO profil_types VALUES (31, 'hospitaliere');
INSERT INTO profil_types VALUES (32, 'apatride');
INSERT INTO profil_types VALUES (33, 'surhomme');
INSERT INTO profil_types VALUES (34, 'stigmatise');
INSERT INTO profil_types VALUES (35, 'alien');
INSERT INTO profil_types VALUES (36, 'mort');
INSERT INTO profil_types VALUES (37, 'pilote');

COMMENT ON COLUMN profil_types.id IS 'profil_type id';
COMMENT ON COLUMN profil_types.name IS 'name of the profil type';
