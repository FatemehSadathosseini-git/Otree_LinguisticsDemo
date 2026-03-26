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

DEMO_PAGE_INTRO_HTML = '<style>.wave{display:inline-block;transform-origin:70% 70%;animation:wave 1.2s infinite;}@keyframes wave{0%,60%,100%{transform:rotate(0deg);}10%,30%{transform:rotate(14deg);}20%,40%{transform:rotate(-8deg);}50%{transform:rotate(10deg);}}</style><p style="color: purple; font-weight: 700; font-size: 1.05rem;">Welcome to Saba\'s demo session <span class="wave">👋</span></p>'

SECRET_KEY = 'CHANGE_ME_FOR_PRODUCTION'
