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

ROOMS = [
    dict(
        name='linguistics_lab',
        display_name='Linguistics Lab',
    ),
]

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'

# Set this in environment for production; default is convenient for local dev.
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD', 'admin')

DEMO_PAGE_INTRO_HTML = """
<style>
    body {
        background: linear-gradient(180deg, #ffe8f6 0%, #ffdff1 100%);
    }
    .saba-demo-wrap {
        margin: 8px 0 18px;
        padding: 14px 16px;
        border-radius: 14px;
        border: 2px solid #d59be8;
        background: rgba(255, 255, 255, 0.68);
        box-shadow: 0 8px 20px rgba(193, 84, 152, 0.15);
    }
    .saba-demo-title {
        color: #7a1fa2;
        font-weight: 800;
        font-size: 1.12rem;
        margin: 0;
        letter-spacing: 0.1px;
    }
    .wave {
        display: inline-block;
        transform-origin: 70% 70%;
        animation: wave 1.2s infinite;
    }
    .flowers {
        margin-top: 8px;
        color: #a100c3;
        font-size: 1.1rem;
        opacity: 0.96;
    }
    .blossom-image {
        margin-top: 10px;
        width: 100%;
        max-width: 420px;
        border-radius: 12px;
        border: 2px solid #d9a6e8;
        box-shadow: 0 6px 18px rgba(168, 88, 149, 0.22);
    }
    .ling-badge {
        display: inline-block;
        margin-top: 10px;
        padding: 4px 10px;
        border-radius: 999px;
        background: #ffe0f4;
        border: 1px solid #d18cd8;
        color: #7a1fa2;
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }
    @keyframes wave {
        0%, 60%, 100% { transform: rotate(0deg); }
        10%, 30% { transform: rotate(14deg); }
        20%, 40% { transform: rotate(-8deg); }
        50% { transform: rotate(10deg); }
    }
</style>

<div class=\"saba-demo-wrap\">
    <p class=\"saba-demo-title\">Welcome to Saba's demo session <span class=\"wave\">👋</span></p>
    <img class=\"blossom-image\" src=\"https://tse1.mm.bing.net/th/id/OIP.hS7da-1k4pOe_e8h-UyapwHaE1?pid=ImgDet&w=187&h=122&c=7&dpr=1,3&o=7&rm=3\" alt=\"Japanese cherry blossom tree\">
    <div class=\"flowers\">🌸 🌷 🌺 🌸 🌷</div>
    <div class=\"ling-badge\">Linguistics Mini Page</div>
</div>
"""

SECRET_KEY = 'CHANGE_ME_FOR_PRODUCTION'
