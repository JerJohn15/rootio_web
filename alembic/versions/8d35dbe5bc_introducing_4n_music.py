"""introducing_4n_music

Revision ID: 8d35dbe5bc
Revises: 18c638d45ed2
Create Date: 2016-11-24 20:13:40.967523

"""

# revision identifiers, used by Alembic.
revision = '8d35dbe5bc'
down_revision = '18c638d45ed2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content_musicplaylistitemtype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('content_musicalbum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('station_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['station_id'], ['radio_station.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('content_musicartist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('station_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['station_id'], ['radio_station.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('content_musicplaylist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('station_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['station_id'], ['radio_station.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('content_music',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('station_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['content_musicalbum.id'], ),
    sa.ForeignKeyConstraint(['station_id'], ['radio_station.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('content_musicplaylistitem',
    sa.Column('playlist_id', sa.Integer(), nullable=True),
    sa.Column('playlist_item_id', sa.Integer(), nullable=True),
    sa.Column('playlist_item_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['playlist_id'], ['content_musicplaylist.id'], ),
    sa.ForeignKeyConstraint(['playlist_item_type_id'], ['content_musicplaylistitemtype.id'], ),
    sa.PrimaryKeyConstraint()
    )
    op.create_table('content_music_musicartist',
    sa.Column('music_id', sa.Integer(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['content_musicartist.id'], ),
    sa.ForeignKeyConstraint(['music_id'], ['content_music.id'], ),
    sa.PrimaryKeyConstraint()
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('content_music_musicartist')
    op.drop_table('content_musicplaylistitem')
    op.drop_table('content_music')
    op.drop_table('content_musicplaylist')
    op.drop_table('content_musicartist')
    op.drop_table('content_musicalbum')
    op.drop_table('content_musicplaylistitemtype')
    ### end Alembic commands ###
