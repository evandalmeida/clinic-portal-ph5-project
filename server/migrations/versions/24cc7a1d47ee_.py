"""empty message

Revision ID: 24cc7a1d47ee
Revises: 
Create Date: 2023-10-13 15:18:45.952679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24cc7a1d47ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clinics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('zip_code', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('forms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('document_type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('DL_image', sa.LargeBinary(), nullable=True),
    sa.Column('rx', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('form_signatures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('form_id', sa.Integer(), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('envelope_id', sa.String(), nullable=True),
    sa.Column('signature_id', sa.String(), nullable=True),
    sa.Column('signed_status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['form_id'], ['forms.id'], name=op.f('fk_form_signatures_form_id_forms')),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], name=op.f('fk_form_signatures_patient_id_patients')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient_clinics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('clinic_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['clinic_id'], ['clinics.id'], name=op.f('fk_patient_clinics_clinic_id_clinics')),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], name=op.f('fk_patient_clinics_patient_id_patients')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient_forms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('form_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['form_id'], ['forms.id'], name=op.f('fk_patient_forms_form_id_forms')),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], name=op.f('fk_patient_forms_patient_id_patients')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('providers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('provider_type', sa.String(), nullable=False),
    sa.Column('clinic_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['clinic_id'], ['clinics.id'], name=op.f('fk_providers_clinic_id_clinics')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('provider_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], name=op.f('fk_appointments_patient_id_patients')),
    sa.ForeignKeyConstraint(['provider_id'], ['providers.id'], name=op.f('fk_appointments_provider_id_providers')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('document_files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(), nullable=False),
    sa.Column('file_path', sa.String(), nullable=True),
    sa.Column('form_id', sa.Integer(), nullable=True),
    sa.Column('form_signature_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['form_id'], ['forms.id'], name=op.f('fk_document_files_form_id_forms')),
    sa.ForeignKeyConstraint(['form_signature_id'], ['form_signatures.id'], name=op.f('fk_document_files_form_signature_id_form_signatures')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('document_files')
    op.drop_table('appointments')
    op.drop_table('providers')
    op.drop_table('patient_forms')
    op.drop_table('patient_clinics')
    op.drop_table('form_signatures')
    op.drop_table('users')
    op.drop_table('patients')
    op.drop_table('forms')
    op.drop_table('clinics')
    # ### end Alembic commands ###
