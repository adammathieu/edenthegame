"""empty message

Revision ID: 3915841292d8
Revises: 3f505406bb1b
Create Date: 2018-06-27 18:56:19.555022

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3915841292d8'
down_revision = '3f505406bb1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profils', sa.Column('profil', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    op.drop_constraint('profils_faction_id_fkey', 'profils', type_='foreignkey')
    op.drop_constraint('profils_profiltype_id_fkey', 'profils', type_='foreignkey')
    op.drop_constraint('profils_stigmate_id_fkey', 'profils', type_='foreignkey')
    op.drop_column('profils', 'profiltype_id')
    op.drop_column('profils', 'faction_id')
    op.drop_column('profils', 'caracteristics')
    op.drop_column('profils', 'stigmate_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profils', sa.Column('stigmate_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('profils', sa.Column('caracteristics', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.add_column('profils', sa.Column('faction_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('profils', sa.Column('profiltype_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('profils_stigmate_id_fkey', 'profils', 'stigmates', ['stigmate_id'], ['id'])
    op.create_foreign_key('profils_profiltype_id_fkey', 'profils', 'profiltype', ['profiltype_id'], ['id'])
    op.create_foreign_key('profils_faction_id_fkey', 'profils', 'factions', ['faction_id'], ['id'])
    op.drop_column('profils', 'profil')
    # ### end Alembic commands ###
