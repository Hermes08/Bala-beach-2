# -*- coding: utf-8 -*-
"""Content for Bala Beach multilingual editorial site.
Mirrors the design handoff (assets/js/content.js) + SEO fields per language.
Edit copy here, then run: python3 build/generate.py
"""

# When you register a custom domain, set custom_domain (e.g. "colonbeachrentals.net").
# generate.py will then emit root-relative paths + a CNAME file and use the apex
# domain for canonical/hreflang/sitemap. Leave "" to keep the GitHub Pages subpath.
SITE = {
    "custom_domain": "colonbeachrentals.xyz",
    "host": "netlify",  # "netlify" (no CNAME) or "github" (writes CNAME)
    "domain": "https://hermes08.github.io",
    "base": "/Bala-beach-2",
    "brand": "Bala Beach",
    "property_name": "Bala Beach Beachfront Rental",
    "locality": "María Chiquita",
    "region": "Colón",
    "country": "PA",
    "country_name": "Panamá",
    "lat": 9.44,
    "lng": -79.75,
    "phone_display": "+507 6761-0315",
    "whatsapp": "50767610315",
    "airbnb": "https://www.airbnb.com/rooms/1409650618945019706",
    "price_low": 120,
    "price_high": 200,
    "rating": "4.9",
    "review_count": "48",
}

DEFAULT_LANG = "en"
LANGS = ["en", "es", "de", "pt", "fr"]

LANG_META = {
    "en": {"name": "English", "flag": "🇺🇸", "short": "EN", "locale": "en_US", "hreflang": "en"},
    "es": {"name": "Español", "flag": "🇵🇦", "short": "ES", "locale": "es_PA", "hreflang": "es"},
    "de": {"name": "Deutsch", "flag": "🇩🇪", "short": "DE", "locale": "de_DE", "hreflang": "de"},
    "pt": {"name": "Português", "flag": "🇧🇷", "short": "PT", "locale": "pt_BR", "hreflang": "pt"},
    "fr": {"name": "Français", "flag": "🇫🇷", "short": "FR", "locale": "fr_FR", "hreflang": "fr"},
}

# Country -> language for IP geolocation mapping
GEO_MAP = {
    "es": ["PA", "ES", "MX", "CO", "AR", "PE", "CL", "VE", "EC", "GT", "CR", "DO", "BO", "HN", "PY", "SV", "NI", "CU", "UY"],
    "de": ["DE", "AT", "CH", "LI"],
    "pt": ["BR", "PT", "AO", "MZ"],
    "fr": ["FR", "BE", "CA", "CH", "LU", "MC", "SN", "CI"],
    "en": ["US", "GB", "CA", "AU", "NZ", "IE", "ZA", "IN", "PH"],
}

IMAGES = {
    "hero": [
        ("https://i.ibb.co/ZRLRdpCs/balcony.jpg", "Private balcony"),
        ("https://i.ibb.co/1fXxZZgH/beach.jpg", "Private beach"),
        ("https://i.ibb.co/kVjVshpM/Pool.jpg", "Resort pool"),
        ("https://i.ibb.co/0RbW3B6g/Ocean-View.jpg", "Ocean view"),
    ],
    "gallery": [
        ("https://i.ibb.co/0RbW3B6g/Ocean-View.jpg", "Ocean view"),
        ("https://i.ibb.co/KxmKQ4Lc/living-room-2.jpg", "Living room"),
        ("https://i.ibb.co/ZRLRdpCs/balcony.jpg", "Private balcony"),
        ("https://i.ibb.co/5xrb03gY/bedroom-1.jpg", "Master bedroom"),
        ("https://i.ibb.co/kVjVshpM/Pool.jpg", "Resort pool"),
        ("https://i.ibb.co/hJv1NcC4/kitchen-3.jpg", "Full kitchen"),
        ("https://i.ibb.co/1fXxZZgH/beach.jpg", "Private beach"),
        ("https://i.ibb.co/Y47qg6Nt/bedroom-2.jpg", "Second bedroom"),
        ("https://i.ibb.co/BHtZsxD8/bathroom-1.jpg", "Modern bathroom"),
        ("https://i.ibb.co/Nk87jjB/building.jpg", "Beachfront building"),
        ("https://i.ibb.co/bgLsNQwV/sofa-bed.jpg", "Sofa bed"),
        ("https://i.ibb.co/NdyZLcmd/gym-2.jpg", "Fitness gym"),
    ],
    "tours": {
        "diving": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?q=80&w=1100&auto=format&fit=crop",
        "portobelo": "https://i.ibb.co/sv9Nz0rS/portobello.jpg",
        "islands": "https://images.unsplash.com/photo-1590523741831-ab7e8b8f9c7f?q=80&w=1100&auto=format&fit=crop",
        "jungle": "https://i.ibb.co/WpcbmNG1/jungle.jpg",
    },
    "og": "https://i.ibb.co/0RbW3B6g/Ocean-View.jpg",
    "film_poster": "https://i.ibb.co/ZRLRdpCs/balcony.jpg",
}

REVIEWS = [
    ("Sarah", "United States", "🇺🇸", 5,
     "The view is absolutely breathtaking. The apartment looks exactly like the photos, modern and spotless. The Starlink internet was super fast for my work calls and we loved the private beach access."),
    ("Carlos", "Panamá", "🇵🇦", 5,
     "Excelente lugar para desconectarse. El apartamento tiene todo lo necesario y la cocina está muy bien equipada. La piscina del complejo es enorme y muy tranquila. 100% recomendado."),
    ("Michael", "Deutschland", "🇩🇪", 5,
     "Ein wunderschönes Apartment mit direktem Meerblick. Sehr sicher und ruhig. Die Kommunikation mit dem Gastgeber war hervorragend. Wir kommen definitiv wieder!"),
    ("Jessica", "Canada", "🇨🇦", 5,
     "Perfect getaway from the city. The balcony view is to die for. Very comfortable beds and strong AC. It felt much more personal and premium than a hotel stay."),
]

FOOTER_KEYWORDS = [
    "María Chiquita Beachfront Rentals", "Bala Beach Panama Rental", "Colón Panama Vacation Homes",
    "Airbnb Alternative María Chiquita", "Scuba Diving Portobelo Panama", "Caribbean Beach House Panama",
    "Ocean View Apartment María Chiquita", "Starlink WiFi Beach Rental Panama", "Direct Booking Beach Rental Panama",
]

SEO = {
    "en": {
        "title": "Beachfront Vacation Rental in María Chiquita, Colón | Bala Beach Panama",
        "desc": "Luxury beachfront vacation rental at Bala Beach, María Chiquita, Colón, Panama. Private Caribbean beach, Starlink WiFi, 24/7 security. Book direct & skip Airbnb fees, from $120/night.",
        "kw": "maria chiquita rental, bala beach panama, colon panama vacation rental, beachfront house panama, airbnb alternative colon, caribbean beach apartment panama, portobelo diving stay",
    },
    "es": {
        "title": "Alquiler Vacacional Frente al Mar en María Chiquita, Colón | Bala Beach Panamá",
        "desc": "Alquiler vacacional de lujo frente al mar en Bala Beach, María Chiquita, Colón, Panamá. Playa caribeña privada, WiFi Starlink, seguridad 24/7. Reserva directo y ahorra las comisiones de Airbnb, desde $120/noche.",
        "kw": "alquiler maria chiquita, bala beach panama, alquiler vacacional colon panama, casa frente al mar panama, alternativa airbnb colon, apartamento playa caribe panama, hospedaje buceo portobelo",
    },
    "de": {
        "title": "Strand-Ferienwohnung in María Chiquita, Colón | Bala Beach Panama",
        "desc": "Luxuriöse Ferienwohnung direkt am Strand im Bala Beach, María Chiquita, Colón, Panama. Privater Karibikstrand, Starlink-WLAN, 24/7-Sicherheit. Direkt buchen & Airbnb-Gebühren sparen, ab 120 $/Nacht.",
        "kw": "ferienwohnung maria chiquita, bala beach panama, ferienhaus colon panama, strandhaus panama karibik, airbnb alternative colon, apartment strand panama, tauchen portobelo unterkunft",
    },
    "pt": {
        "title": "Aluguel de Temporada à Beira-Mar em María Chiquita, Colón | Bala Beach Panamá",
        "desc": "Aluguel de temporada de luxo à beira-mar no Bala Beach, María Chiquita, Colón, Panamá. Praia caribenha privativa, WiFi Starlink, segurança 24/7. Reserve direto e economize as taxas do Airbnb, a partir de US$120/noite.",
        "kw": "aluguel maria chiquita, bala beach panama, casa de temporada colon panama, casa de praia panama caribe, alternativa airbnb colon, apartamento praia panama, mergulho portobelo hospedagem",
    },
    "fr": {
        "title": "Location de Vacances en Bord de Mer à María Chiquita, Colón | Bala Beach Panama",
        "desc": "Location de vacances de luxe en bord de mer au Bala Beach, María Chiquita, Colón, Panama. Plage privée des Caraïbes, WiFi Starlink, sécurité 24/7. Réservez en direct et évitez les frais Airbnb, dès 120 $/nuit.",
        "kw": "location maria chiquita, bala beach panama, location vacances colon panama, maison plage panama caraibes, alternative airbnb colon, appartement plage panama, plongee portobelo hebergement",
    },
}

C = {}

C["en"] = {
    "nav": {"amenities": "Amenities", "gallery": "Gallery", "tours": "Things to do", "reviews": "Reviews", "faq": "FAQ", "book": "Book Direct"},
    "hero": {
        "badge": "Better than Airbnb, no service fees",
        "kicker": "María Chiquita · Colón · Panamá",
        "title": "A private Caribbean beach house, all your own",
        "sub": "Beachfront living on Panama's Colón coast: private sand, 24/7 gated security and blazing Starlink WiFi. The #1 alternative to a hotel.",
        "cta": "Book on WhatsApp", "cta2": "View on Airbnb", "price": "From $120", "per": "/ night",
    },
    "trust": ["Private Caribbean beach", "Starlink WiFi 100 Mbps+", "24/7 gated security", "Resort pool & gym"],
    "features": {
        "kicker": "The residence", "title": "Everything you need, nothing you don't",
        "sub": "Equipped for total comfort: settle in with premium, hotel-grade amenities.",
        "items": [
            ("wifi", "Fast Starlink WiFi", "100 Mbps+ for remote work"),
            ("ac", "Air conditioning", "Cool, quiet bedrooms"),
            ("kitchen", "Full kitchen", "Fully equipped to cook"),
            ("tv", "Smart TV", "Netflix & Prime included"),
            ("parking", "Private parking", "Secure gated spot"),
            ("bed", "Premium bedding", "Hotel-quality linens"),
        ],
    },
    "gallery": {"kicker": "The gallery", "title": "Step inside", "sub": "Explore every corner of the beachfront apartment.", "all": "View all photos"},
    "film": {"kicker": "The film", "title": "See the residence in motion", "sub": "A short glimpse of life at Bala Beach: the light, the water, the calm.", "cta": "Play with sound", "on": "Sound on"},
    "why": {
        "kicker": "Book direct", "title": "Why book direct with us",
        "sub": "Skip the middleman and save 15-20% on platform service fees.",
        "direct": "Direct booking", "ota": "Airbnb / Booking",
        "rows": [
            "Best rate guaranteed, no service fees",
            "Local Colón concierge & personal support",
            "Flexible check-in & total privacy",
            "Free insider Caribbean coast guide",
        ],
    },
    "tours": {
        "kicker": "Beyond the door", "title": "Discover Costa Arriba, Colón",
        "sub": "Minutes from the private beach lie unforgettable adventures and world-class diving.",
        "items": [
            ("Scuba & snorkeling in Portobelo", "Coral reefs and shipwrecks make this one of Panama's best dive spots, minutes away.", "diving"),
            ("Historic ruins of Portobelo", "UNESCO World Heritage pirate forts and the Black Christ church, 15 minutes away.", "portobelo"),
            ("Isla Grande & Isla Mamey", "Hop a nearby boat to the crystal waters of Isla Grande or snorkel at Isla Mamey.", "islands"),
            ("Rainforest adventure", "Hike Sierra Llorona or take a photo safari to spot monkeys and exotic birds.", "jungle"),
        ],
    },
    "reviews": {"kicker": "Guest stories", "title": "Loved by travelers worldwide", "sub": "Real experiences from guests around the world.", "source": "Verified on Airbnb", "superhost": "Superhost", "rated": "rated by"},
    "faq": {
        "kicker": "Good to know", "title": "Frequently asked questions",
        "sub": "Key information for your stay on the Colón coast.",
        "items": [
            ("Is the property safe in Colón?", "Absolutely. We're inside a private gated resort with 24/7 security. María Chiquita is a calm, family-friendly tourist area."),
            ("How fast is the internet?", "High-speed Starlink (100 Mbps+), perfect for video calls, streaming and remote work without interruptions."),
            ("Can I book short stays?", "Yes, we accept stays from 2 nights. We also offer special discounts for weekly and monthly stays."),
            ("What do I save by booking direct?", "Booking direct saves you roughly 15-20% in service fees charged by platforms like Airbnb and Booking."),
        ],
    },
    "location": {"kicker": "The location", "title": "A prime Caribbean address", "sub": "Bala Beach resort, María Chiquita: 90 minutes from Panama City, 15 from Portobelo.", "directions": "Get directions"},
    "newsletter": {"kicker": "VIP club", "title": "Join the Caribbean VIP club", "sub": "Get our secret Colón travel guide and exclusive direct-booking discounts.", "placeholder": "Your email address", "button": "Get the free guide", "disclaimer": "No spam, only real offers and travel tips."},
    "footer": {"about": "Your best vacation rental in María Chiquita, Colón. Luxury and comfort on Panama's Caribbean coast.", "contact": "Contact", "links": "Explore", "rights": "All rights reserved.", "popular": "Popular searches"},
    "wa": "Hi! I'm interested in renting the beachfront apartment at Bala Beach, María Chiquita.",
}

C["es"] = {
    "nav": {"amenities": "Amenidades", "gallery": "Galería", "tours": "Qué hacer", "reviews": "Reseñas", "faq": "Preguntas", "book": "Reservar"},
    "hero": {
        "badge": "Mejor que Airbnb, sin comisiones",
        "kicker": "María Chiquita · Colón · Panamá",
        "title": "Una casa de playa caribeña, solo para ti",
        "sub": "Vida frente al mar en la costa de Colón: arena privada, seguridad 24/7 y WiFi Starlink ultrarrápido. La alternativa #1 al hotel.",
        "cta": "Reservar por WhatsApp", "cta2": "Ver en Airbnb", "price": "Desde $120", "per": "/ noche",
    },
    "trust": ["Playa privada caribeña", "WiFi Starlink 100 Mbps+", "Seguridad 24/7 con garita", "Piscina y gimnasio"],
    "features": {
        "kicker": "La residencia", "title": "Todo lo que necesitas, nada de más",
        "sub": "Equipado para el confort total: siéntete como en casa con amenidades premium.",
        "items": [
            ("wifi", "WiFi Starlink rápido", "100 Mbps+ para teletrabajo"),
            ("ac", "Aire acondicionado", "Habitaciones frescas y silenciosas"),
            ("kitchen", "Cocina completa", "Totalmente equipada"),
            ("tv", "Smart TV", "Netflix y Prime incluidos"),
            ("parking", "Estacionamiento privado", "Espacio seguro con garita"),
            ("bed", "Ropa de cama premium", "Calidad de hotel"),
        ],
    },
    "gallery": {"kicker": "La galería", "title": "Pasa adentro", "sub": "Explora cada rincón del apartamento frente al mar.", "all": "Ver todas las fotos"},
    "film": {"kicker": "El recorrido", "title": "Vive la residencia en movimiento", "sub": "Un vistazo a la vida en Bala Beach: la luz, el agua, la calma.", "cta": "Reproducir con sonido", "on": "Con sonido"},
    "why": {
        "kicker": "Reserva directa", "title": "Por qué reservar directo con nosotros",
        "sub": "Evita intermediarios y ahorra 15-20% en comisiones de servicio.",
        "direct": "Reserva directa", "ota": "Airbnb / Booking",
        "rows": [
            "Mejor tarifa garantizada, sin comisiones",
            "Concierge local de Colón y atención personal",
            "Check-in flexible y privacidad total",
            "Guía secreta del Caribe panameño gratis",
        ],
    },
    "tours": {
        "kicker": "Más allá de la puerta", "title": "Descubre la Costa Arriba de Colón",
        "sub": "A minutos de la playa privada te esperan aventuras inolvidables y buceo de clase mundial.",
        "items": [
            ("Buceo y snorkel en Portobelo", "Arrecifes de coral y barcos hundidos: uno de los mejores destinos de buceo de Panamá, a minutos.", "diving"),
            ("Ruinas históricas de Portobelo", "Fortificaciones piratas Patrimonio de la UNESCO y la Iglesia del Cristo Negro, a 15 minutos.", "portobelo"),
            ("Isla Grande e Isla Mamey", "Toma un bote cercano a las aguas cristalinas de Isla Grande o haz snorkel en Isla Mamey.", "islands"),
            ("Aventura en la selva", "Senderismo en Sierra Llorona o safari fotográfico para ver monos y aves exóticas.", "jungle"),
        ],
    },
    "reviews": {"kicker": "Historias de huéspedes", "title": "Amado por viajeros del mundo", "sub": "Experiencias reales de viajeros de todo el mundo.", "source": "Verificado en Airbnb", "superhost": "Superanfitrión", "rated": "calificado por"},
    "faq": {
        "kicker": "Bueno saber", "title": "Preguntas frecuentes",
        "sub": "Información clave para tu estancia en la costa de Colón.",
        "items": [
            ("¿Es segura la propiedad en Colón?", "Totalmente. Estamos dentro de un complejo privado con garita de seguridad 24/7. María Chiquita es una zona turística tranquila y familiar."),
            ("¿Qué tan rápido es el internet?", "Starlink de alta velocidad (100 Mbps+), perfecto para videollamadas, streaming y trabajo remoto sin interrupciones."),
            ("¿Puedo reservar estancias cortas?", "Sí, aceptamos reservas desde 2 noches. También ofrecemos descuentos para estancias semanales y mensuales."),
            ("¿Qué ahorro al reservar directo?", "Reservar directo te ahorra aproximadamente 15-20% en comisiones de plataformas como Airbnb y Booking."),
        ],
    },
    "location": {"kicker": "La ubicación", "title": "Una dirección caribeña privilegiada", "sub": "Complejo Bala Beach, María Chiquita: a 90 minutos de Ciudad de Panamá y 15 de Portobelo.", "directions": "Cómo llegar"},
    "newsletter": {"kicker": "Club VIP", "title": "Únete al club VIP del Caribe", "sub": "Recibe nuestra guía secreta de Colón y descuentos exclusivos por reserva directa.", "placeholder": "Tu correo electrónico", "button": "Recibir guía gratis", "disclaimer": "Sin spam, solo ofertas reales y tips de viaje."},
    "footer": {"about": "Tu mejor alquiler vacacional en María Chiquita, Colón. Lujo y confort en el Caribe panameño.", "contact": "Contacto", "links": "Explorar", "rights": "Todos los derechos reservados.", "popular": "Búsquedas populares"},
    "wa": "¡Hola! Estoy interesado en alquilar el apartamento frente al mar en Bala Beach, María Chiquita.",
}

C["de"] = {
    "nav": {"amenities": "Ausstattung", "gallery": "Galerie", "tours": "Aktivitäten", "reviews": "Bewertungen", "faq": "FAQ", "book": "Buchen"},
    "hero": {
        "badge": "Besser als Airbnb, keine Gebühren",
        "kicker": "María Chiquita · Colón · Panama",
        "title": "Ein privates Strandhaus in der Karibik, ganz für Sie",
        "sub": "Leben am Meer an Panamas Colón-Küste: privater Strand, 24/7-Sicherheit und schnelles Starlink-WLAN. Die Hotel-Alternative Nr. 1.",
        "cta": "Per WhatsApp buchen", "cta2": "Auf Airbnb ansehen", "price": "Ab 120 $", "per": "/ Nacht",
    },
    "trust": ["Privater Karibikstrand", "Starlink-WLAN 100 Mbit/s+", "24/7-Sicherheit", "Pool & Fitnessstudio"],
    "features": {
        "kicker": "Die Residenz", "title": "Alles, was Sie brauchen, nichts überflüssig",
        "sub": "Ausgestattet für vollen Komfort: fühlen Sie sich wie zu Hause mit Premium-Ausstattung.",
        "items": [
            ("wifi", "Schnelles Starlink-WLAN", "100 Mbit/s+ fürs Homeoffice"),
            ("ac", "Klimaanlage", "Kühle, ruhige Schlafzimmer"),
            ("kitchen", "Voll ausgestattete Küche", "Komplett zum Kochen"),
            ("tv", "Smart-TV", "Netflix & Prime inklusive"),
            ("parking", "Privater Parkplatz", "Sicherer Stellplatz"),
            ("bed", "Premium-Bettwäsche", "Hotelqualität"),
        ],
    },
    "gallery": {"kicker": "Die Galerie", "title": "Treten Sie ein", "sub": "Entdecken Sie jeden Winkel der Strandwohnung.", "all": "Alle Fotos ansehen"},
    "film": {"kicker": "Der Film", "title": "Die Residenz in Bewegung", "sub": "Ein kurzer Blick auf das Leben am Bala Beach: das Licht, das Wasser, die Ruhe.", "cta": "Mit Ton abspielen", "on": "Ton an"},
    "why": {
        "kicker": "Direkt buchen", "title": "Warum direkt bei uns buchen",
        "sub": "Ohne Zwischenhändler sparen Sie 15-20 % an Servicegebühren.",
        "direct": "Direktbuchung", "ota": "Airbnb / Booking",
        "rows": [
            "Bestpreisgarantie, keine Servicegebühren",
            "Lokaler Colón-Concierge & persönlicher Service",
            "Flexibler Check-in & volle Privatsphäre",
            "Kostenloser Karibik-Insider-Reiseführer",
        ],
    },
    "tours": {
        "kicker": "Vor der Tür", "title": "Entdecken Sie die Costa Arriba, Colón",
        "sub": "Nur Minuten vom Privatstrand entfernt warten unvergessliche Abenteuer und Weltklasse-Tauchen.",
        "items": [
            ("Tauchen & Schnorcheln in Portobelo", "Korallenriffe und Wracks: einer der besten Tauchspots Panamas, nur Minuten entfernt.", "diving"),
            ("Historische Ruinen von Portobelo", "UNESCO-Welterbe-Piratenfestungen und die Schwarze-Christus-Kirche, 15 Minuten entfernt.", "portobelo"),
            ("Isla Grande & Isla Mamey", "Mit dem Boot zu den kristallklaren Gewässern von Isla Grande oder Schnorcheln an der Isla Mamey.", "islands"),
            ("Regenwald-Abenteuer", "Wandern in der Sierra Llorona oder Fotosafari, um Affen und exotische Vögel zu sehen.", "jungle"),
        ],
    },
    "reviews": {"kicker": "Gästegeschichten", "title": "Von Reisenden weltweit geliebt", "sub": "Echte Erfahrungen von Reisenden aus aller Welt.", "source": "Verifiziert auf Airbnb", "superhost": "Superhost", "rated": "bewertet von"},
    "faq": {
        "kicker": "Gut zu wissen", "title": "Häufige Fragen",
        "sub": "Wichtige Informationen für Ihren Aufenthalt an der Colón-Küste.",
        "items": [
            ("Ist die Unterkunft in Colón sicher?", "Absolut. Wir befinden uns in einer privaten Anlage mit 24/7-Sicherheit. María Chiquita ist eine ruhige, familienfreundliche Touristengegend."),
            ("Wie schnell ist das Internet?", "Highspeed-Starlink (100 Mbit/s+), perfekt für Videoanrufe, Streaming und Homeoffice ohne Unterbrechungen."),
            ("Kann ich Kurzaufenthalte buchen?", "Ja, wir akzeptieren Aufenthalte ab 2 Nächten. Für Wochen- und Monatsaufenthalte bieten wir Sonderrabatte."),
            ("Was spare ich bei Direktbuchung?", "Direktbuchung spart Ihnen rund 15-20 % an Servicegebühren von Plattformen wie Airbnb und Booking."),
        ],
    },
    "location": {"kicker": "Die Lage", "title": "Eine erstklassige Karibik-Adresse", "sub": "Bala-Beach-Anlage, María Chiquita: 90 Minuten von Panama-Stadt, 15 von Portobelo.", "directions": "Route anzeigen"},
    "newsletter": {"kicker": "VIP-Club", "title": "Treten Sie dem Karibik-VIP-Club bei", "sub": "Erhalten Sie unseren geheimen Colón-Reiseführer und exklusive Direktbuchungs-Rabatte.", "placeholder": "Ihre E-Mail-Adresse", "button": "Gratis-Guide erhalten", "disclaimer": "Kein Spam, nur echte Angebote und Reisetipps."},
    "footer": {"about": "Ihre beste Ferienwohnung in María Chiquita, Colón. Luxus und Komfort an Panamas Karibikküste.", "contact": "Kontakt", "links": "Entdecken", "rights": "Alle Rechte vorbehalten.", "popular": "Beliebte Suchen"},
    "wa": "Hallo! Ich interessiere mich für die Anmietung der Strandwohnung im Bala Beach, María Chiquita.",
}

C["pt"] = {
    "nav": {"amenities": "Comodidades", "gallery": "Galeria", "tours": "O que fazer", "reviews": "Avaliações", "faq": "Perguntas", "book": "Reservar"},
    "hero": {
        "badge": "Melhor que Airbnb, sem taxas",
        "kicker": "María Chiquita · Colón · Panamá",
        "title": "Uma casa de praia caribenha só sua",
        "sub": "Vida à beira-mar na costa de Colón: areia privativa, segurança 24/7 e WiFi Starlink ultrarrápido. A alternativa nº 1 ao hotel.",
        "cta": "Reservar pelo WhatsApp", "cta2": "Ver no Airbnb", "price": "A partir de US$120", "per": "/ noite",
    },
    "trust": ["Praia caribenha privativa", "WiFi Starlink 100 Mbps+", "Segurança 24/7", "Piscina e academia"],
    "features": {
        "kicker": "A residência", "title": "Tudo o que você precisa, nada além",
        "sub": "Equipado para o conforto total: sinta-se em casa com comodidades premium.",
        "items": [
            ("wifi", "WiFi Starlink rápido", "100 Mbps+ para trabalho remoto"),
            ("ac", "Ar-condicionado", "Quartos frescos e silenciosos"),
            ("kitchen", "Cozinha completa", "Totalmente equipada"),
            ("tv", "Smart TV", "Netflix e Prime inclusos"),
            ("parking", "Estacionamento privativo", "Vaga segura"),
            ("bed", "Roupa de cama premium", "Qualidade de hotel"),
        ],
    },
    "gallery": {"kicker": "A galeria", "title": "Entre e veja", "sub": "Explore cada canto do apartamento à beira-mar.", "all": "Ver todas as fotos"},
    "film": {"kicker": "O tour", "title": "Veja a residência em movimento", "sub": "Um breve olhar sobre a vida no Bala Beach: a luz, a água, a calma.", "cta": "Reproduzir com som", "on": "Com som"},
    "why": {
        "kicker": "Reserva direta", "title": "Por que reservar direto conosco",
        "sub": "Evite intermediários e economize 15-20% em taxas de serviço.",
        "direct": "Reserva direta", "ota": "Airbnb / Booking",
        "rows": [
            "Melhor tarifa garantida, sem taxas de serviço",
            "Concierge local de Colón e suporte pessoal",
            "Check-in flexível e privacidade total",
            "Guia secreto do Caribe panamenho grátis",
        ],
    },
    "tours": {
        "kicker": "Além da porta", "title": "Descubra a Costa Arriba, Colón",
        "sub": "A minutos da praia privativa estão aventuras inesquecíveis e mergulho de classe mundial.",
        "items": [
            ("Mergulho e snorkel em Portobelo", "Recifes de coral e naufrágios: um dos melhores pontos de mergulho do Panamá, a minutos.", "diving"),
            ("Ruínas históricas de Portobelo", "Fortificações piratas Patrimônio da UNESCO e a Igreja do Cristo Negro, a 15 minutos.", "portobelo"),
            ("Isla Grande e Isla Mamey", "Pegue um barco próximo às águas cristalinas de Isla Grande ou faça snorkel na Isla Mamey.", "islands"),
            ("Aventura na floresta", "Trilhas na Sierra Llorona ou safári fotográfico para ver macacos e aves exóticas.", "jungle"),
        ],
    },
    "reviews": {"kicker": "Histórias de hóspedes", "title": "Amado por viajantes do mundo todo", "sub": "Experiências reais de viajantes do mundo todo.", "source": "Verificado no Airbnb", "superhost": "Superhost", "rated": "avaliado por"},
    "faq": {
        "kicker": "Bom saber", "title": "Perguntas frequentes",
        "sub": "Informações essenciais para sua estadia na costa de Colón.",
        "items": [
            ("A propriedade é segura em Colón?", "Totalmente. Estamos em um condomínio privativo com segurança 24/7. María Chiquita é uma área turística tranquila e familiar."),
            ("Qual a velocidade da internet?", "Starlink de alta velocidade (100 Mbps+), perfeito para videochamadas, streaming e trabalho remoto sem interrupções."),
            ("Posso reservar estadias curtas?", "Sim, aceitamos estadias a partir de 2 noites. Também oferecemos descontos para estadias semanais e mensais."),
            ("O que economizo reservando direto?", "Reservar direto economiza cerca de 15-20% em taxas de plataformas como Airbnb e Booking."),
        ],
    },
    "location": {"kicker": "A localização", "title": "Um endereço caribenho privilegiado", "sub": "Condomínio Bala Beach, María Chiquita: a 90 minutos da Cidade do Panamá e 15 de Portobelo.", "directions": "Como chegar"},
    "newsletter": {"kicker": "Clube VIP", "title": "Entre no clube VIP do Caribe", "sub": "Receba nosso guia secreto de Colón e descontos exclusivos por reserva direta.", "placeholder": "Seu e-mail", "button": "Receber guia grátis", "disclaimer": "Sem spam, apenas ofertas reais e dicas de viagem."},
    "footer": {"about": "Seu melhor aluguel de temporada em María Chiquita, Colón. Luxo e conforto no Caribe panamenho.", "contact": "Contato", "links": "Explorar", "rights": "Todos os direitos reservados.", "popular": "Buscas populares"},
    "wa": "Olá! Tenho interesse em alugar o apartamento à beira-mar no Bala Beach, María Chiquita.",
}

C["fr"] = {
    "nav": {"amenities": "Équipements", "gallery": "Galerie", "tours": "À faire", "reviews": "Avis", "faq": "FAQ", "book": "Réserver"},
    "hero": {
        "badge": "Mieux qu'Airbnb, sans frais",
        "kicker": "María Chiquita · Colón · Panama",
        "title": "Une maison de plage caraïbe, rien que pour vous",
        "sub": "La vie en bord de mer sur la côte de Colón: sable privé, sécurité 24/7 et WiFi Starlink ultra-rapide. L'alternative nº 1 à l'hôtel.",
        "cta": "Réserver sur WhatsApp", "cta2": "Voir sur Airbnb", "price": "Dès 120 $", "per": "/ nuit",
    },
    "trust": ["Plage privée des Caraïbes", "WiFi Starlink 100 Mbps+", "Sécurité 24/7", "Piscine & salle de sport"],
    "features": {
        "kicker": "La résidence", "title": "Tout le nécessaire, rien de superflu",
        "sub": "Équipé pour un confort total: sentez-vous chez vous avec des prestations premium.",
        "items": [
            ("wifi", "WiFi Starlink rapide", "100 Mbps+ pour le télétravail"),
            ("ac", "Climatisation", "Chambres fraîches et calmes"),
            ("kitchen", "Cuisine complète", "Entièrement équipée"),
            ("tv", "Smart TV", "Netflix & Prime inclus"),
            ("parking", "Parking privé", "Place sécurisée"),
            ("bed", "Linge de lit premium", "Qualité hôtelière"),
        ],
    },
    "gallery": {"kicker": "La galerie", "title": "Entrez", "sub": "Explorez chaque recoin de l'appartement en bord de mer.", "all": "Voir toutes les photos"},
    "film": {"kicker": "Le film", "title": "La résidence en mouvement", "sub": "Un bref aperçu de la vie au Bala Beach: la lumière, l'eau, le calme.", "cta": "Lire avec le son", "on": "Son activé"},
    "why": {
        "kicker": "Réserver en direct", "title": "Pourquoi réserver en direct avec nous",
        "sub": "Évitez les intermédiaires et économisez 15 à 20 % de frais de service.",
        "direct": "Réservation directe", "ota": "Airbnb / Booking",
        "rows": [
            "Meilleur tarif garanti, sans frais de service",
            "Conciergerie locale de Colón & service personnel",
            "Check-in flexible & intimité totale",
            "Guide secret des Caraïbes offert",
        ],
    },
    "tours": {
        "kicker": "Au-delà de la porte", "title": "Découvrez la Costa Arriba, Colón",
        "sub": "À quelques minutes de la plage privée vous attendent des aventures inoubliables et de la plongée de classe mondiale.",
        "items": [
            ("Plongée & snorkeling à Portobelo", "Récifs et épaves: l'un des meilleurs spots de plongée du Panama, à quelques minutes.", "diving"),
            ("Ruines historiques de Portobelo", "Forts pirates classés UNESCO et l'église du Christ Noir, à 15 minutes.", "portobelo"),
            ("Isla Grande & Isla Mamey", "Prenez un bateau vers les eaux cristallines d'Isla Grande ou snorkeling à Isla Mamey.", "islands"),
            ("Aventure en forêt tropicale", "Randonnée à la Sierra Llorona ou safari photo pour observer singes et oiseaux exotiques.", "jungle"),
        ],
    },
    "reviews": {"kicker": "Histoires de voyageurs", "title": "Adoré par les voyageurs du monde entier", "sub": "Expériences réelles de voyageurs du monde entier.", "source": "Vérifié sur Airbnb", "superhost": "Superhost", "rated": "noté par"},
    "faq": {
        "kicker": "Bon à savoir", "title": "Questions fréquentes",
        "sub": "Informations clés pour votre séjour sur la côte de Colón.",
        "items": [
            ("La propriété est-elle sûre à Colón ?", "Absolument. Nous sommes dans une résidence privée avec sécurité 24/7. María Chiquita est une zone touristique calme et familiale."),
            ("Quelle est la vitesse d'internet ?", "Starlink haut débit (100 Mbps+), parfait pour les visioconférences, le streaming et le télétravail sans interruption."),
            ("Puis-je réserver de courts séjours ?", "Oui, nous acceptons les séjours à partir de 2 nuits. Nous proposons aussi des réductions pour les séjours hebdomadaires et mensuels."),
            ("Qu'est-ce que j'économise en réservant en direct ?", "Réserver en direct vous fait économiser environ 15 à 20 % de frais facturés par des plateformes comme Airbnb et Booking."),
        ],
    },
    "location": {"kicker": "L'emplacement", "title": "Une adresse caraïbe d'exception", "sub": "Résidence Bala Beach, María Chiquita: à 90 minutes de Panama City et 15 de Portobelo.", "directions": "Itinéraire"},
    "newsletter": {"kicker": "Club VIP", "title": "Rejoignez le club VIP des Caraïbes", "sub": "Recevez notre guide secret de Colón et des réductions exclusives en réservation directe.", "placeholder": "Votre adresse e-mail", "button": "Recevoir le guide gratuit", "disclaimer": "Pas de spam, uniquement de vraies offres et conseils de voyage."},
    "footer": {"about": "Votre meilleure location de vacances à María Chiquita, Colón. Luxe et confort sur la côte caraïbe du Panama.", "contact": "Contact", "links": "Explorer", "rights": "Tous droits réservés.", "popular": "Recherches populaires"},
    "wa": "Bonjour ! Je suis intéressé(e) par la location de l'appartement en bord de mer au Bala Beach, María Chiquita.",
}
