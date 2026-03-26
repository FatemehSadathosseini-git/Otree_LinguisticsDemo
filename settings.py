from os import environ

SESSION_CONFIGS = [
    dict(
        name='reference_game',
        display_name='Reference Game',
        num_demo_participants=2,
        app_sequence=['reference_game'],
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc='',
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'

# Set this in environment for production; default is convenient for local dev.
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD', 'admin')

DEMO_PAGE_INTRO_HTML = '<p style="color: purple; font-weight: 700;">Welcom to Saba\'s demo session please</p>'

SECRET_KEY = 'CHANGE_ME_FOR_PRODUCTION'
