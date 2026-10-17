import _data as D
from _components import esc, facts_grid, features, figure, faq_html
from _icons import icon

PATH = "/en/"

FAQ = [
    ("Where is Chácara Império?",
     "In Uberaba, Minas Gerais, Brazil — inside the city's urban perimeter, with paved access and an electronic gate. The exact location is shared by WhatsApp."),
    ("How many people can stay overnight?",
     "Up to 40 guests in 6 en-suite bedrooms with air conditioning (40 beds, 8 bathrooms). Check-in from 3 pm, check-out by 11 am."),
    ("How many guests for events?",
     "Up to 250 guests, with a covered hall, a gourmet area with barbecue grill and wood-fired stove, gardens, two pools and parking for 40 cars."),
    ("How do I book?",
     "Bookings are made only by phone or WhatsApp: +55 34 99169-0139."),
    ("Is it a good base for Expozebu?",
     "Yes. Expozebu, the large zebu cattle fair held by ABCZ at Parque Fernando Costa in Uberaba (usually late April to early May), fills the city. The chácara hosts groups of up to 40 people with on-site parking."),
]

wa = D.wa_url("en")

BODY = f'''
<section class="section section--tight">
<div class="wrap">
<div class="answer"><span class="answer-label">In short</span><p><strong>Chácara Império</strong> is a private country house for events and group stays in <strong>Uberaba, Minas Gerais, Brazil</strong>. It hosts events of up to <strong>250 guests</strong> and sleeps up to <strong>40 people in 6 en-suite bedrooms</strong>. The 2,500 m² property has an adult pool and a kids' pool, a covered gourmet area with barbecue grill and wood-fired stove, a covered party hall, a grass soccer field, a playground and parking for 40 cars. Pets are welcome. Bookings by phone or WhatsApp: +55 34 99169-0139.</p></div>
{facts_grid().replace("convidados em eventos", "event guests").replace("hóspedes para dormir", "overnight guests").replace("suítes", "en-suite bedrooms").replace("banheiros", "bathrooms").replace("m² de área", "m² property").replace("vagas de estacionamento", "parking spaces").replace('aria-label="A chácara em números"', 'aria-label="Key numbers"')}
</div>
</section>

<section class="section section--paper">
<div class="wrap split">
<div>
<p class="eyebrow">The property</p>
<h2>Events and group stays in Uberaba</h2>
<p>Weddings, birthdays, company gatherings and family reunions — and the whole house for weekends, holidays or work teams. Hosts <strong>{esc(D.HOSTS_PHRASE)}</strong> handle every booking personally.</p>
{features([("waves", "Adult pool and kids' pool"), ("flame", "Barbecue grill and wood-fired stove"), ("home", "Covered party hall"), ("ball", "Grass soccer field"), ("smile", "Playground"), ("bed", "6 en-suite bedrooms, 40 beds"), ("wifi", "Wi-Fi and workspace"), ("car", "Parking for 40 cars"), ("shield", "Electronic gate and outdoor cameras"), ("paw", "Pets welcome")])}
<div class="btn-row mt-2"><a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener" data-wa="en">{icon("whatsapp")}<span>Message us on WhatsApp</span></a><a class="btn btn-ghost" href="{D.TEL_URL}">{icon("phone")}<span>Call +55 34 99169-0139</span></a></div>
</div>
<div>{figure("piscinas-vista", "Adult pool and kids' pool", "(min-width: 900px) 560px, 100vw")}</div>
</div>
</section>

<section class="section">
<div class="wrap narrow">
{faq_html(FAQ, "Questions")}
<p class="mt-2"><a href="/">Versão em português</a> · <a href="/galeria/">Photo gallery</a> · <a href="/tour-em-video/">Video tour</a></p>
</div>
</section>
'''

PAGE = dict(
    path=PATH,
    lang="en",
    title="Chácara Império: Event Venue & Group Stays in Uberaba, Brazil",
    description="Country house in Uberaba, Brazil, for events up to 250 guests and group stays up to 40 people in 6 en-suite rooms, with pools and barbecue. Book via WhatsApp.",
    h1="Event venue and group stays in Uberaba, Brazil",
    lead="A private country house for weddings, parties and group stays — up to 250 event guests and 40 overnight guests.",
    eyebrow="Chácara Império · Uberaba, MG, Brazil",
    hero="piscina-banco",
    crumbs=[("Home", "/en/")],
    hero_ctas=f'<div class="btn-row"><a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{icon("whatsapp")}<span>WhatsApp</span></a></div>',
    wa_key="en",
    faq=FAQ,
    alternates=[("pt-BR", "/"), ("en", "/en/"), ("x-default", "/")],
    body=BODY,
)
