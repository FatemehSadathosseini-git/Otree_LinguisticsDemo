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
    .saba-blossom-layer {
        position: fixed;
        inset: 0;
        pointer-events: none;
        overflow: hidden;
        z-index: 1;
    }
    .saba-blossom {
        position: absolute;
        top: -8vh;
        font-size: 1.15rem;
        opacity: 0.9;
        animation: blossom-fall linear infinite;
    }
    .saba-blossom:nth-child(1) { left: 8%; animation-duration: 9s; animation-delay: 0s; }
    .saba-blossom:nth-child(2) { left: 22%; animation-duration: 12s; animation-delay: 1.2s; }
    .saba-blossom:nth-child(3) { left: 35%; animation-duration: 10s; animation-delay: 2.4s; }
    .saba-blossom:nth-child(4) { left: 48%; animation-duration: 13s; animation-delay: 0.6s; }
    .saba-blossom:nth-child(5) { left: 62%; animation-duration: 11s; animation-delay: 1.8s; }
    .saba-blossom:nth-child(6) { left: 77%; animation-duration: 12.5s; animation-delay: 0.9s; }
    .saba-blossom:nth-child(7) { left: 90%; animation-duration: 9.5s; animation-delay: 2.1s; }

    .saba-demo-wrap {
        position: relative;
        z-index: 3;
        margin: 8px 0 18px;
        padding: 14px 16px;
        border-radius: 14px;
        border: 2px solid #d59be8;
        background: rgba(255, 255, 255, 0.68);
        box-shadow: 0 8px 20px rgba(193, 84, 152, 0.15);
        overflow: hidden;
    }
    .parallax-item {
        will-change: transform;
        transition: transform 120ms ease-out;
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
    @keyframes blossom-fall {
        0% { transform: translate3d(0, -8vh, 0) rotate(0deg); }
        50% { transform: translate3d(16px, 48vh, 0) rotate(180deg); }
        100% { transform: translate3d(-12px, 108vh, 0) rotate(360deg); }
    }
</style>

<div class=\"saba-blossom-layer\" aria-hidden=\"true\">
    <span class=\"saba-blossom\">🌸</span>
    <span class=\"saba-blossom\">🌸</span>
    <span class=\"saba-blossom\">🌸</span>
    <span class=\"saba-blossom\">🌸</span>
    <span class=\"saba-blossom\">🌸</span>
    <span class=\"saba-blossom\">🌸</span>
    <span class=\"saba-blossom\">🌸</span>
</div>

<div class=\"saba-demo-wrap\">
    <p class=\"saba-demo-title parallax-item\" data-depth=\"1.2\">Welcome to Saba's demo session <span class=\"wave\">👋</span></p>
    <img class=\"blossom-image parallax-item\" data-depth=\"0.6\" src=\"https://tse1.mm.bing.net/th/id/OIP.hS7da-1k4pOe_e8h-UyapwHaE1?pid=ImgDet&w=187&h=122&c=7&dpr=1,3&o=7&rm=3\" alt=\"Japanese cherry blossom tree\">
    <div class=\"flowers parallax-item\" data-depth=\"1.5\">🌸 🌷 🌺 🌸 🌷</div>
    <div class=\"ling-badge parallax-item\" data-depth=\"1.1\">Linguistics Mini Page</div>
</div>

<script>
    (function () {
        const wrap = document.querySelector('.saba-demo-wrap');
        if (!wrap) return;

        const parallaxItems = wrap.querySelectorAll('.parallax-item');
        window.addEventListener('mousemove', function (event) {
            const x = (event.clientX / window.innerWidth - 0.5) * 20;
            const y = (event.clientY / window.innerHeight - 0.5) * 16;
            parallaxItems.forEach(function (element) {
                const depth = parseFloat(element.getAttribute('data-depth') || '1');
                const dx = (-x * depth).toFixed(2);
                const dy = (-y * depth).toFixed(2);
                element.style.transform = 'translate(' + dx + 'px, ' + dy + 'px)';
            });
        });
    })();
</script>
"""

SECRET_KEY = 'CHANGE_ME_FOR_PRODUCTION'
