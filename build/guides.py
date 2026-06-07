# -*- coding: utf-8 -*-
"""Travel-guide content hub for colonbeachrentals.xyz.
Top-of-funnel pillars that capture Panama beach-tourism research traffic and
funnel it to the rental. Each guide: per-language title/desc/kw/h1/lead + blocks.
A block is (h2, [items]) where an item is a paragraph string or ("ul", [li,...]).
Edit here, then run: python3 build/generate.py
"""

# Order = display order in the guides index and nav.
GUIDE_ORDER = ["panama-caribbean-beaches", "beaches-near-panama-city"]

# Localized labels for the guides hub (nav + index page)
GUIDES_LABEL = {
    "en": {"nav": "Guides", "title": "Panama Caribbean Travel Guides",
           "sub": "Plan your trip to Panama's Caribbean coast — beaches, diving, islands and how to get there. Written from María Chiquita, our home base.",
           "read": "Read guide", "all": "All guides", "back": "Back to guides",
           "cta_title": "Stay where the guides begin", "cta_sub": "Make Bala Beach in María Chiquita your base for the Caribbean coast. Private beach, Starlink WiFi, book direct.",
           "cta_btn": "Check availability", "related": "Keep reading"},
    "es": {"nav": "Guías", "title": "Guías de Viaje del Caribe de Panamá",
           "sub": "Planifica tu viaje a la costa caribeña de Panamá: playas, buceo, islas y cómo llegar. Escrito desde María Chiquita, nuestra base.",
           "read": "Leer guía", "all": "Todas las guías", "back": "Volver a guías",
           "cta_title": "Hospédate donde empiezan las guías", "cta_sub": "Haz de Bala Beach en María Chiquita tu base para la costa caribeña. Playa privada, WiFi Starlink, reserva directa.",
           "cta_btn": "Ver disponibilidad", "related": "Sigue leyendo"},
    "de": {"nav": "Guides", "title": "Reiseführer Karibikküste Panama",
           "sub": "Planen Sie Ihre Reise an Panamas Karibikküste: Strände, Tauchen, Inseln und Anreise. Geschrieben aus María Chiquita, unserer Basis.",
           "read": "Guide lesen", "all": "Alle Guides", "back": "Zurück zu den Guides",
           "cta_title": "Wohnen, wo die Guides beginnen", "cta_sub": "Machen Sie Bala Beach in María Chiquita zu Ihrer Basis für die Karibikküste. Privatstrand, Starlink-WLAN, direkt buchen.",
           "cta_btn": "Verfügbarkeit prüfen", "related": "Weiterlesen"},
    "pt": {"nav": "Guias", "title": "Guias de Viagem do Caribe do Panamá",
           "sub": "Planeje sua viagem à costa caribenha do Panamá: praias, mergulho, ilhas e como chegar. Escrito de María Chiquita, nossa base.",
           "read": "Ler guia", "all": "Todos os guias", "back": "Voltar aos guias",
           "cta_title": "Hospede-se onde os guias começam", "cta_sub": "Faça do Bala Beach em María Chiquita sua base para a costa caribenha. Praia privativa, WiFi Starlink, reserve direto.",
           "cta_btn": "Ver disponibilidade", "related": "Continue lendo"},
    "fr": {"nav": "Guides", "title": "Guides de Voyage Côte Caraïbe du Panama",
           "sub": "Préparez votre voyage sur la côte caraïbe du Panama : plages, plongée, îles et accès. Écrit depuis María Chiquita, notre base.",
           "read": "Lire le guide", "all": "Tous les guides", "back": "Retour aux guides",
           "cta_title": "Séjournez là où commencent les guides", "cta_sub": "Faites du Bala Beach à María Chiquita votre base pour la côte caraïbe. Plage privée, WiFi Starlink, réservez en direct.",
           "cta_btn": "Voir les disponibilités", "related": "À lire aussi"},
}

GUIDES = {}

# ============================================================
# PILLAR 1 — Panama's Caribbean beaches
# ============================================================
GUIDES["panama-caribbean-beaches"] = {
    "image": "beach",
    "en": {
        "title": "Panama's Caribbean Beaches: The Complete Coast Guide (2026)",
        "desc": "A local guide to the best beaches on Panama's Caribbean coast — from María Chiquita and Portobelo to Isla Grande, Isla Mamey and the San Blas islands. Where to go, when, and how.",
        "kw": "panama beaches, caribbean panama, best beaches in panama, panama caribbean coast, maria chiquita, isla grande panama",
        "h1": "Panama's Caribbean Beaches: The Complete Coast Guide",
        "lead": "Panama has two coastlines, but the Caribbean side is where the postcard turquoise lives. This is a local's guide to the beaches of the Colón province coast and beyond — what each one is good for, and how to string them into one trip.",
        "blocks": [
            ("Why the Caribbean coast beats the Pacific for beaches", [
                "Panama City sits on the Pacific, so most day-trippers default to Pacific beaches like Coronado. But the water there is grey-green and the sand dark. Cross to the Caribbean — only about 90 minutes from the city through the Sierra Llorona rainforest — and the sea turns clear turquoise over pale sand and coral.",
                "The heart of this coast is the Costa Arriba of Colón: María Chiquita, Portobelo, Isla Grande and Isla Mamey, with the wild San Blas archipelago further east. It is calmer, greener and far less developed than the Pacific resort strip.",
            ]),
            ("The beaches, one by one", [
                ("ul", [
                    "<strong>María Chiquita</strong> — the closest Caribbean beach to Panama City and the easiest base. Calm, swimmable water, a long sandy bay and gated beachfront residences (this is where Bala Beach is). Ideal for families and remote workers.",
                    "<strong>Portobelo</strong> — 15 minutes on: a UNESCO World Heritage town of Spanish forts and the Black Christ church, and the launch point for the area's best scuba diving.",
                    "<strong>Isla Grande</strong> — a short boat hop, with reggae beach bars, snorkeling and day-trip energy.",
                    "<strong>Isla Mamey</strong> — a tiny, calm snorkeling island, perfect for a half-day boat trip.",
                    "<strong>San Blas (Guna Yala)</strong> — the bucket-list archipelago of 300+ palm islands, reached further east; doable as a longer excursion.",
                ]),
            ]),
            ("Best time to visit", [
                "The Caribbean coast is green year-round. The driest, sunniest stretch is roughly mid-December to April. The shoulder months still deliver plenty of sun between short tropical showers, and rates are lower. Weekends fill with Panamanian families, so midweek stays are quieter.",
            ]),
            ("How to do it in one trip", [
                "Base yourself on a calm beach with fast internet and a kitchen, then radiate out: a diving day in Portobelo, a boat day to Isla Grande or Isla Mamey, an afternoon exploring the forts. María Chiquita is the natural hub because it is the first proper beach you reach from the city and central to everything above.",
            ]),
        ],
    },
    "es": {
        "title": "Playas del Caribe de Panamá: La Guía Completa de la Costa (2026)",
        "desc": "Guía local de las mejores playas del Caribe panameño: de María Chiquita y Portobelo a Isla Grande, Isla Mamey y San Blas. Dónde ir, cuándo y cómo.",
        "kw": "playas de panama, caribe panama, mejores playas de panama, costa caribe panama, maria chiquita, isla grande panama",
        "h1": "Playas del Caribe de Panamá: La Guía Completa de la Costa",
        "lead": "Panamá tiene dos costas, pero el turquesa de postal vive en el lado caribeño. Esta es una guía de local sobre las playas de la costa de Colón y más allá: para qué sirve cada una y cómo unirlas en un solo viaje.",
        "blocks": [
            ("Por qué el Caribe gana al Pacífico en playas", [
                "La Ciudad de Panamá está en el Pacífico, así que casi todos van por defecto a playas pacíficas como Coronado. Pero ahí el agua es gris-verdosa y la arena oscura. Cruza al Caribe — a solo unos 90 minutos de la ciudad por la selva de Sierra Llorona — y el mar se vuelve turquesa transparente sobre arena clara y coral.",
                "El corazón de esta costa es la Costa Arriba de Colón: María Chiquita, Portobelo, Isla Grande e Isla Mamey, con el archipiélago salvaje de San Blas más al este. Es más tranquila, más verde y mucho menos desarrollada que la franja de resorts del Pacífico.",
            ]),
            ("Las playas, una por una", [
                ("ul", [
                    "<strong>María Chiquita</strong> — la playa caribeña más cercana a la Ciudad de Panamá y la base más fácil. Agua calma y nadable, una bahía larga de arena y residencias privadas frente al mar (aquí está Bala Beach). Ideal para familias y teletrabajo.",
                    "<strong>Portobelo</strong> — a 15 minutos: pueblo Patrimonio de la UNESCO con fuertes españoles y la Iglesia del Cristo Negro, y el punto de partida del mejor buceo de la zona.",
                    "<strong>Isla Grande</strong> — a un corto viaje en bote, con bares de playa, snorkel y ambiente de paseo de día.",
                    "<strong>Isla Mamey</strong> — una islita calma de snorkel, perfecta para medio día en bote.",
                    "<strong>San Blas (Guna Yala)</strong> — el archipiélago soñado de 300+ islas de palmeras, más al este; factible como excursión más larga.",
                ]),
            ]),
            ("Mejor época para visitar", [
                "La costa caribeña está verde todo el año. El tramo más seco y soleado va aproximadamente de mediados de diciembre a abril. Los meses de transición igual dan mucho sol entre lluvias tropicales cortas, y con tarifas más bajas. Los fines de semana se llenan de familias panameñas, así que entre semana es más tranquilo.",
            ]),
            ("Cómo hacerlo en un solo viaje", [
                "Instálate en una playa tranquila con buen internet y cocina, y desde ahí irradia: un día de buceo en Portobelo, un día de bote a Isla Grande o Isla Mamey, una tarde explorando los fuertes. María Chiquita es el centro natural porque es la primera playa de verdad que encuentras desde la ciudad y está céntrica a todo lo anterior.",
            ]),
        ],
    },
    "de": {
        "title": "Karibikstrände von Panama: Der komplette Küstenführer (2026)",
        "desc": "Lokaler Führer zu den besten Stränden an Panamas Karibikküste: von María Chiquita und Portobelo bis Isla Grande, Isla Mamey und San Blas.",
        "kw": "panama strände, karibik panama, beste strände panama, maria chiquita, isla grande panama",
        "h1": "Karibikstrände von Panama: Der komplette Küstenführer",
        "lead": "Panama hat zwei Küsten, aber das Postkarten-Türkis liegt an der Karibikseite. Ein Überblick über die Strände der Colón-Küste und darüber hinaus — und wie man sie zu einer Reise verbindet.",
        "blocks": [
            ("Warum die Karibikküste die besseren Strände hat", [
                "Panama-Stadt liegt am Pazifik, dessen Wasser grau-grün und der Sand dunkel ist. An der Karibik — nur etwa 90 Minuten von der Stadt durch den Regenwald — wird das Meer klar türkis über hellem Sand und Korallen. Das Herz ist die Costa Arriba von Colón: María Chiquita, Portobelo, Isla Grande und Isla Mamey, mit dem San-Blas-Archipel weiter östlich.",
            ]),
            ("Die Strände im Überblick", [
                ("ul", [
                    "<strong>María Chiquita</strong> — der nächstgelegene Karibikstrand zu Panama-Stadt und die einfachste Basis. Ruhiges Badewasser, lange Sandbucht, private Strandanlagen (hier liegt Bala Beach).",
                    "<strong>Portobelo</strong> — 15 Minuten weiter: UNESCO-Welterbe mit spanischen Festungen und Ausgangspunkt für das beste Tauchen.",
                    "<strong>Isla Grande</strong> — kurze Bootsfahrt, Strandbars und Schnorcheln.",
                    "<strong>Isla Mamey</strong> — winzige, ruhige Schnorchelinsel für einen halben Tag.",
                    "<strong>San Blas (Guna Yala)</strong> — das Traumarchipel mit 300+ Palmeninseln, weiter östlich.",
                ]),
            ]),
            ("Beste Reisezeit", [
                "Die Karibikküste ist ganzjährig grün. Am trockensten und sonnigsten ist es etwa von Mitte Dezember bis April. Unter der Woche ist es ruhiger als am Wochenende.",
            ]),
            ("Alles in einer Reise", [
                "Quartier an einem ruhigen Strand mit schnellem Internet und Küche nehmen und von dort aus starten: ein Tauchtag in Portobelo, ein Bootstag nach Isla Grande oder Isla Mamey. María Chiquita ist der natürliche Knotenpunkt.",
            ]),
        ],
    },
    "pt": {
        "title": "Praias do Caribe do Panamá: O Guia Completo da Costa (2026)",
        "desc": "Guia local das melhores praias da costa caribenha do Panamá: de María Chiquita e Portobelo a Isla Grande, Isla Mamey e San Blas.",
        "kw": "praias do panama, caribe panama, melhores praias do panama, maria chiquita, isla grande panama",
        "h1": "Praias do Caribe do Panamá: O Guia Completo da Costa",
        "lead": "O Panamá tem duas costas, mas o turquesa de cartão-postal vive no lado caribenho. Um guia local das praias da costa de Colón e além — e como uni-las em uma só viagem.",
        "blocks": [
            ("Por que o Caribe vence o Pacífico em praias", [
                "A Cidade do Panamá fica no Pacífico, de água cinza-esverdeada e areia escura. No Caribe — a apenas 90 minutos da cidade pela floresta — o mar fica turquesa transparente sobre areia clara e coral. O coração é a Costa Arriba de Colón: María Chiquita, Portobelo, Isla Grande e Isla Mamey, com o arquipélago de San Blas mais a leste.",
            ]),
            ("As praias, uma a uma", [
                ("ul", [
                    "<strong>María Chiquita</strong> — a praia caribenha mais próxima da Cidade do Panamá e a base mais fácil. Água calma, baía longa de areia, residências privativas à beira-mar (aqui fica o Bala Beach).",
                    "<strong>Portobelo</strong> — a 15 minutos: Patrimônio da UNESCO com fortes espanhóis e ponto de partida do melhor mergulho.",
                    "<strong>Isla Grande</strong> — curto trajeto de barco, bares de praia e snorkel.",
                    "<strong>Isla Mamey</strong> — ilhota calma de snorkel, perfeita para meio dia.",
                    "<strong>San Blas (Guna Yala)</strong> — o arquipélago dos sonhos com 300+ ilhas de palmeiras, mais a leste.",
                ]),
            ]),
            ("Melhor época para visitar", [
                "A costa caribenha é verde o ano todo. O período mais seco e ensolarado vai de meados de dezembro a abril. Durante a semana é mais tranquilo que nos fins de semana.",
            ]),
            ("Como fazer em uma só viagem", [
                "Fique numa praia tranquila com bom internet e cozinha, e a partir dali explore: um dia de mergulho em Portobelo, um dia de barco a Isla Grande ou Isla Mamey. María Chiquita é o centro natural.",
            ]),
        ],
    },
    "fr": {
        "title": "Plages des Caraïbes du Panama : Le Guide Complet de la Côte (2026)",
        "desc": "Guide local des plus belles plages de la côte caraïbe du Panama : de María Chiquita et Portobelo à Isla Grande, Isla Mamey et San Blas.",
        "kw": "plages panama, caraibes panama, plus belles plages panama, maria chiquita, isla grande panama",
        "h1": "Plages des Caraïbes du Panama : Le Guide Complet de la Côte",
        "lead": "Le Panama a deux côtes, mais le turquoise de carte postale vit du côté caraïbe. Un guide local des plages de la côte de Colón et au-delà — et comment les enchaîner en un seul voyage.",
        "blocks": [
            ("Pourquoi la côte caraïbe surpasse le Pacifique", [
                "Panama City est sur le Pacifique, à l'eau gris-vert et au sable foncé. Côté Caraïbes — à seulement 90 minutes de la ville à travers la forêt — la mer devient turquoise translucide sur sable clair et corail. Le cœur est la Costa Arriba de Colón : María Chiquita, Portobelo, Isla Grande et Isla Mamey, avec l'archipel de San Blas plus à l'est.",
            ]),
            ("Les plages, une à une", [
                ("ul", [
                    "<strong>María Chiquita</strong> — la plage caraïbe la plus proche de Panama City et la base la plus simple. Eau calme, longue baie de sable, résidences privées en bord de mer (c'est ici qu'est Bala Beach).",
                    "<strong>Portobelo</strong> — à 15 minutes : site UNESCO aux forts espagnols et point de départ de la meilleure plongée.",
                    "<strong>Isla Grande</strong> — courte traversée en bateau, bars de plage et snorkeling.",
                    "<strong>Isla Mamey</strong> — petite île calme de snorkeling, idéale pour une demi-journée.",
                    "<strong>San Blas (Guna Yala)</strong> — l'archipel de rêve aux 300+ îles de palmiers, plus à l'est.",
                ]),
            ]),
            ("Meilleure période", [
                "La côte caraïbe est verte toute l'année. La période la plus sèche et ensoleillée va de mi-décembre à avril. En semaine, c'est plus calme que le week-end.",
            ]),
            ("Tout en un seul voyage", [
                "Installez-vous sur une plage tranquille avec bon internet et cuisine, puis rayonnez : une journée de plongée à Portobelo, une journée en bateau à Isla Grande ou Isla Mamey. María Chiquita est le hub naturel.",
            ]),
        ],
    },
}

# ============================================================
# PILLAR 2 — Beaches near Panama City
# ============================================================
GUIDES["beaches-near-panama-city"] = {
    "image": "ocean-view",
    "en": {
        "title": "Beaches Near Panama City: The Best Caribbean Day Trip & Weekend",
        "desc": "Looking for a beach near Panama City? María Chiquita on the Caribbean coast is ~90 minutes away — clear turquoise water, how to get there, and where to stay.",
        "kw": "beaches near panama city, day trip from panama city, weekend getaway panama, maria chiquita, caribbean beach near panama city",
        "h1": "Beaches Near Panama City: The Caribbean Escape",
        "lead": "You can be on a calm, clear Caribbean beach in about an hour and a half from Panama City — without flying. Here is exactly where to go, how to get there, and how to turn it into a day trip or a weekend.",
        "blocks": [
            ("The closest real beach to the city", [
                "Most people head to the Pacific beaches west of the city, but the water is murky and the sand dark. The better-kept secret is to drive north to the Caribbean. <strong>María Chiquita</strong>, in the Costa Arriba of Colón, is the first true Caribbean beach you reach — roughly 90 minutes door to door — with turquoise water, pale sand and a calm, swimmable bay.",
            ]),
            ("How to get there from Panama City", [
                ("ul", [
                    "<strong>By car:</strong> take the Panama–Colón highway, then the Portobelo road east. About 1h20–1h40 depending on traffic leaving the city.",
                    "<strong>Route:</strong> you cross the Sierra Llorona rainforest — a scenic drive in itself, with monkeys and birds along the way.",
                    "<strong>Tip:</strong> leave early on weekends; the road is quiet midweek.",
                ]),
            ]),
            ("Day trip vs. weekend", [
                "A day trip works, but the Caribbean coast rewards an overnight. Stay one or two nights and you can add a Portobelo diving morning, a boat to Isla Grande, or just a slow sunrise on the balcony. A gated beachfront apartment with a kitchen and fast WiFi turns it into a proper reset rather than a rushed drive.",
            ]),
            ("Where to stay", [
                "María Chiquita has gated beachfront residences right on the sand. <strong>Bala Beach</strong> is one of them — a private Caribbean apartment with a pool, 24/7 security and Starlink WiFi, bookable direct (no platform fees). It is the easy answer to \"a beach near Panama City\" that you will actually want to stay at.",
            ]),
        ],
    },
    "es": {
        "title": "Playas Cerca de la Ciudad de Panamá: La Escapada al Caribe",
        "desc": "¿Buscas playa cerca de la Ciudad de Panamá? María Chiquita, en el Caribe, está a ~90 minutos: agua turquesa, cómo llegar y dónde hospedarte.",
        "kw": "playas cerca de la ciudad de panama, escapada de fin de semana panama, maria chiquita, playa caribe cerca de panama, paseo de un dia panama",
        "h1": "Playas Cerca de la Ciudad de Panamá: La Escapada al Caribe",
        "lead": "Puedes estar en una playa caribeña tranquila y cristalina en una hora y media desde la Ciudad de Panamá — sin tomar un avión. Aquí va exactamente a dónde ir, cómo llegar, y cómo volverlo un paseo de día o un fin de semana.",
        "blocks": [
            ("La playa de verdad más cercana a la ciudad", [
                "Casi todos van a las playas del Pacífico al oeste de la ciudad, pero el agua es turbia y la arena oscura. El secreto mejor guardado es manejar al norte, al Caribe. <strong>María Chiquita</strong>, en la Costa Arriba de Colón, es la primera playa caribeña de verdad que encuentras — a unos 90 minutos puerta a puerta — con agua turquesa, arena clara y una bahía calma y nadable.",
            ]),
            ("Cómo llegar desde la Ciudad de Panamá", [
                ("ul", [
                    "<strong>En carro:</strong> toma la autopista Panamá–Colón y luego la vía a Portobelo hacia el este. Entre 1h20 y 1h40 según el tráfico de salida.",
                    "<strong>Ruta:</strong> cruzas la selva de Sierra Llorona — un trayecto escénico, con monos y aves en el camino.",
                    "<strong>Tip:</strong> sal temprano los fines de semana; entre semana la vía está tranquila.",
                ]),
            ]),
            ("Paseo de día vs. fin de semana", [
                "Un paseo de día funciona, pero la costa caribeña premia quedarse a dormir. Una o dos noches y le sumas una mañana de buceo en Portobelo, un bote a Isla Grande, o simplemente un amanecer lento en el balcón. Un apartamento frente al mar con garita, cocina y WiFi rápido lo convierte en un verdadero reinicio y no en un manejón apurado.",
            ]),
            ("Dónde hospedarte", [
                "María Chiquita tiene residencias privadas frente al mar, sobre la arena. <strong>Bala Beach</strong> es una de ellas: un apartamento caribeño privado con piscina, seguridad 24/7 y WiFi Starlink, reservable directo (sin comisiones de plataforma). Es la respuesta fácil a \"una playa cerca de la ciudad\" en la que de verdad querrás quedarte.",
            ]),
        ],
    },
    "de": {
        "title": "Strände nahe Panama-Stadt: Der Karibik-Kurztrip",
        "desc": "Strand in der Nähe von Panama-Stadt? María Chiquita an der Karibik ist ~90 Minuten entfernt: klares Türkis, Anreise und Unterkunft.",
        "kw": "strände nahe panama stadt, wochenendausflug panama, maria chiquita, karibikstrand panama",
        "h1": "Strände nahe Panama-Stadt: Der Karibik-Kurztrip",
        "lead": "In rund anderthalb Stunden ab Panama-Stadt erreichen Sie einen ruhigen, klaren Karibikstrand — ganz ohne Flug. So kommen Sie hin und machen einen Tagesausflug oder ein Wochenende daraus.",
        "blocks": [
            ("Der nächste echte Strand", [
                "Die meisten fahren zu den Pazifikstränden westlich der Stadt, doch das Wasser ist trüb und der Sand dunkel. Besser fährt man nach Norden an die Karibik. <strong>María Chiquita</strong> in der Costa Arriba von Colón ist der erste echte Karibikstrand — etwa 90 Minuten — mit türkisem Wasser und ruhiger Badebucht.",
            ]),
            ("Anreise von Panama-Stadt", [
                ("ul", [
                    "<strong>Mit dem Auto:</strong> Autobahn Panama–Colón, dann die Straße nach Portobelo Richtung Osten. Etwa 1:20–1:40 Std. je nach Verkehr.",
                    "<strong>Strecke:</strong> durch den Sierra-Llorona-Regenwald — landschaftlich schön.",
                    "<strong>Tipp:</strong> am Wochenende früh losfahren; unter der Woche ruhig.",
                ]),
            ]),
            ("Tagesausflug oder Wochenende", [
                "Ein Tagesausflug geht, doch eine Übernachtung lohnt sich: dazu ein Tauchvormittag in Portobelo oder ein Boot nach Isla Grande. Ein Strandapartment mit Küche und schnellem WLAN macht daraus einen echten Reset.",
            ]),
            ("Wo übernachten", [
                "María Chiquita hat private Strandanlagen direkt am Sand. <strong>Bala Beach</strong> ist eine davon — privates Karibikapartment mit Pool, 24/7-Sicherheit und Starlink-WLAN, direkt buchbar (ohne Plattformgebühren).",
            ]),
        ],
    },
    "pt": {
        "title": "Praias Perto da Cidade do Panamá: A Escapada ao Caribe",
        "desc": "Praia perto da Cidade do Panamá? María Chiquita, no Caribe, fica a ~90 minutos: água turquesa, como chegar e onde ficar.",
        "kw": "praias perto da cidade do panama, escapada de fim de semana panama, maria chiquita, praia caribe panama",
        "h1": "Praias Perto da Cidade do Panamá: A Escapada ao Caribe",
        "lead": "Você pode estar numa praia caribenha calma e cristalina em cerca de uma hora e meia da Cidade do Panamá — sem voar. Veja para onde ir, como chegar e como transformar em passeio de um dia ou fim de semana.",
        "blocks": [
            ("A praia de verdade mais próxima", [
                "Quase todos vão às praias do Pacífico a oeste da cidade, mas a água é turva e a areia escura. O segredo é ir ao norte, ao Caribe. <strong>María Chiquita</strong>, na Costa Arriba de Colón, é a primeira praia caribenha de verdade — a cerca de 90 minutos — com água turquesa e baía calma.",
            ]),
            ("Como chegar da Cidade do Panamá", [
                ("ul", [
                    "<strong>De carro:</strong> rodovia Panamá–Colón e depois a via a Portobelo, a leste. Entre 1h20 e 1h40 conforme o trânsito.",
                    "<strong>Rota:</strong> você cruza a floresta de Sierra Llorona — um trajeto cênico.",
                    "<strong>Dica:</strong> saia cedo nos fins de semana; durante a semana é tranquilo.",
                ]),
            ]),
            ("Passeio de um dia vs. fim de semana", [
                "Um dia funciona, mas vale dormir: some uma manhã de mergulho em Portobelo ou um barco a Isla Grande. Um apartamento à beira-mar com cozinha e WiFi rápido transforma tudo num verdadeiro descanso.",
            ]),
            ("Onde ficar", [
                "María Chiquita tem residências privativas à beira-mar. <strong>Bala Beach</strong> é uma delas — apartamento caribenho privativo com piscina, segurança 24/7 e WiFi Starlink, reservável direto (sem taxas de plataforma).",
            ]),
        ],
    },
    "fr": {
        "title": "Plages Près de Panama City : L'Escapade aux Caraïbes",
        "desc": "Une plage près de Panama City ? María Chiquita, côté Caraïbes, est à ~90 minutes : eau turquoise, accès et hébergement.",
        "kw": "plages près de panama city, escapade week-end panama, maria chiquita, plage caraibe panama",
        "h1": "Plages Près de Panama City : L'Escapade aux Caraïbes",
        "lead": "Vous pouvez être sur une plage caraïbe calme et claire en une heure et demie depuis Panama City — sans prendre l'avion. Voici où aller, comment s'y rendre, et comment en faire une journée ou un week-end.",
        "blocks": [
            ("La vraie plage la plus proche", [
                "La plupart vont vers les plages du Pacifique à l'ouest, mais l'eau y est trouble et le sable foncé. Mieux vaut filer au nord, vers les Caraïbes. <strong>María Chiquita</strong>, dans la Costa Arriba de Colón, est la première vraie plage caraïbe — à environ 90 minutes — eau turquoise et baie calme.",
            ]),
            ("Comment s'y rendre depuis Panama City", [
                ("ul", [
                    "<strong>En voiture :</strong> autoroute Panama–Colón puis la route de Portobelo vers l'est. Environ 1h20–1h40 selon le trafic.",
                    "<strong>Itinéraire :</strong> vous traversez la forêt de Sierra Llorona — une route panoramique.",
                    "<strong>Astuce :</strong> partez tôt le week-end ; en semaine c'est calme.",
                ]),
            ]),
            ("Journée ou week-end", [
                "Une journée suffit, mais une nuit sur place vaut le détour : ajoutez une matinée de plongée à Portobelo ou un bateau vers Isla Grande. Un appartement en bord de mer avec cuisine et WiFi rapide en fait une vraie pause.",
            ]),
            ("Où loger", [
                "María Chiquita compte des résidences privées en bord de mer. <strong>Bala Beach</strong> en fait partie — appartement caraïbe privé avec piscine, sécurité 24/7 et WiFi Starlink, réservable en direct (sans frais de plateforme).",
            ]),
        ],
    },
}
