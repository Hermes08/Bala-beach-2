# -*- coding: utf-8 -*-
"""Content dictionary for Bala Beach / María Chiquita multilingual site."""

SITE = {
    "domain": "https://hermes08.github.io",
    "base": "/Bala-beach-2",
    "brand": "Bala Beach Rentals",
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

# Default language served at root after geo-redirect fails
DEFAULT_LANG = "en"

# Order matters for switcher
LANGS = ["en", "es", "de", "pt", "fr"]

LANG_META = {
    "en": {"name": "English", "flag": "🇺🇸", "locale": "en_US", "hreflang": "en"},
    "es": {"name": "Español", "flag": "🇵🇦", "locale": "es_PA", "hreflang": "es"},
    "de": {"name": "Deutsch", "flag": "🇩🇪", "locale": "de_DE", "hreflang": "de"},
    "pt": {"name": "Português", "flag": "🇧🇷", "locale": "pt_BR", "hreflang": "pt"},
    "fr": {"name": "Français", "flag": "🇫🇷", "locale": "fr_FR", "hreflang": "fr"},
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
        "https://i.ibb.co/KxmKQ4Lc/living-room-2.jpg",
        "https://i.ibb.co/0RbW3B6g/Ocean-View.jpg",
        "https://i.ibb.co/5xrb03gY/bedroom-1.jpg",
        "https://i.ibb.co/kVjVshpM/Pool.jpg",
    ],
    "gallery": [
        ("https://i.ibb.co/KxmKQ4Lc/living-room-2.jpg", "Living room"),
        ("https://i.ibb.co/0RbW3B6g/Ocean-View.jpg", "Ocean view"),
        ("https://i.ibb.co/5xrb03gY/bedroom-1.jpg", "Master bedroom"),
        ("https://i.ibb.co/kVjVshpM/Pool.jpg", "Resort pool"),
        ("https://i.ibb.co/hJv1NcC4/kitchen-3.jpg", "Full kitchen"),
        ("https://i.ibb.co/ZRLRdpCs/balcony.jpg", "Private balcony"),
        ("https://i.ibb.co/Y47qg6Nt/bedroom-2.jpg", "Second bedroom"),
        ("https://i.ibb.co/BHtZsxD8/bathroom-1.jpg", "Modern bathroom"),
        ("https://i.ibb.co/Nk87jjB/building.jpg", "Beachfront building"),
        ("https://i.ibb.co/bgLsNQwV/sofa-bed.jpg", "Sofa bed"),
        ("https://i.ibb.co/NdyZLcmd/gym-2.jpg", "Fitness gym"),
        ("https://i.ibb.co/1fXxZZgH/beach.jpg", "Private beach"),
    ],
    "tours": {
        "diving": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?q=80&w=900&auto=format&fit=crop",
        "portobelo": "https://i.ibb.co/sv9Nz0rS/portobello.jpg",
        "islands": "https://images.unsplash.com/photo-1590523741831-ab7e8b8f9c7f?q=80&w=900&auto=format&fit=crop",
        "jungle": "https://i.ibb.co/WpcbmNG1/jungle.jpg",
    },
    "og": "https://i.ibb.co/0RbW3B6g/Ocean-View.jpg",
}

REVIEWS = [
    ("Sarah", "United States", "🇺🇸", 5,
     "The view is absolutely breathtaking! The apartment looks exactly like the photos — modern and spotless. The Starlink internet was super fast for my work calls and we loved the private beach access."),
    ("Carlos", "Panamá", "🇵🇦", 5,
     "Excelente lugar para desconectarse. El apartamento tiene todo lo necesario y la cocina está muy bien equipada. La piscina del complejo es enorme y muy tranquila. 100% recomendado."),
    ("Michael", "Deutschland", "🇩🇪", 5,
     "Ein wunderschönes Apartment mit direktem Meerblick. Sehr sicher und ruhig. Die Kommunikation mit dem Gastgeber war hervorragend. Wir kommen definitiv wieder!"),
    ("Jessica", "Canada", "🇨🇦", 5,
     "Perfect getaway from the city. The balcony view is to die for! Very comfortable beds and strong AC. It felt much more personal and premium than a hotel stay."),
]

# ---- Per-language content ----
C = {}

C["en"] = {
    "title": "Beachfront Vacation Rental in María Chiquita, Colón | Bala Beach Panama",
    "meta_desc": "Luxury beachfront vacation rental at Bala Beach, María Chiquita, Colón, Panama. Private Caribbean beach, Starlink WiFi, 24/7 security. Book direct & skip Airbnb fees — from $120/night.",
    "keywords": "maria chiquita rental, bala beach panama, colon panama vacation rental, beachfront house panama, airbnb alternative colon, caribbean beach apartment panama, portobelo diving stay",
    "nav": {"amenities": "Amenities", "gallery": "Gallery", "tours": "Things to do", "reviews": "Reviews", "faq": "FAQ", "book": "Book Direct"},
    "hero": {
        "badge": "Better than Airbnb — No service fees",
        "title": "Beachfront Vacation Rental in María Chiquita",
        "sub": "Your private Caribbean beach house on Panama's Colón coast. The #1 hotel alternative — private beach, 24/7 security and blazing Starlink WiFi.",
        "cta": "Book on WhatsApp",
        "cta2": "View on Airbnb",
        "price": "From $120 / night",
    },
    "trust": ["Private Caribbean beach", "Starlink WiFi 100 Mbps+", "24/7 gated security", "Resort pool & gym"],
    "features": {
        "title": "Everything you need for the perfect stay",
        "sub": "Equipped for total comfort — feel at home with premium amenities.",
        "items": [
            ("wifi", "Fast Starlink WiFi", "100 Mbps+ for remote work"),
            ("ac", "Air Conditioning", "Cool & quiet bedrooms"),
            ("kitchen", "Full Kitchen", "Fully equipped to cook"),
            ("tv", "Smart TV", "Netflix & Prime included"),
            ("parking", "Private Parking", "Secure gated spot"),
            ("bed", "Premium Bedding", "Hotel-quality linens"),
        ],
    },
    "gallery": {"title": "Photo gallery", "sub": "Explore every corner of our beachfront apartment."},
    "why": {
        "title": "Why book direct with us?",
        "sub": "Skip the middleman and save 15–20% on platform service fees.",
        "direct": "Direct booking",
        "ota": "Airbnb / Booking",
        "rows": [
            ("Best rate guaranteed — no service fees", True, False),
            ("Local Colón concierge & personal support", True, False),
            ("Flexible check-in & total privacy", True, False),
            ("Free insider Caribbean coast guide", True, False),
        ],
    },
    "tours": {
        "title": "Discover Costa Arriba, Colón",
        "sub": "Beyond the private beach you are minutes from unforgettable adventures and world-class diving.",
        "items": [
            ("Scuba diving & snorkeling in Portobelo", "Coral reefs and shipwrecks make this one of the best dive spots in Panama — just minutes away.", "diving"),
            ("Historic ruins of Portobelo", "Explore the UNESCO World Heritage pirate forts and the Black Christ church, 15 minutes away.", "portobelo"),
            ("Isla Grande & Isla Mamey tour", "Hop on a nearby boat to the crystal-clear waters of Isla Grande or snorkel at Isla Mamey.", "islands"),
            ("Rainforest adventure", "Hike Sierra Llorona or take a photo safari to spot monkeys and exotic birds in the wild.", "jungle"),
        ],
    },
    "reviews": {"title": "What our guests say", "sub": "Real experiences from travelers around the world.", "source": "Verified on Airbnb"},
    "faq": {
        "title": "Frequently asked questions",
        "sub": "Key information for your stay on the Colón coast.",
        "items": [
            ("Is the property safe in Colón?", "Absolutely. We're inside a private gated resort with 24/7 security. María Chiquita is a calm, family-friendly tourist area."),
            ("How fast is the internet?", "High-speed Starlink (100 Mbps+) — perfect for video calls, streaming and remote work without interruptions."),
            ("Can I book short stays?", "Yes, we accept stays from 2 nights. We also offer special discounts for weekly and monthly stays."),
            ("What do I save by booking direct?", "Booking direct saves you roughly 15–20% in service fees charged by platforms like Airbnb and Booking."),
        ],
    },
    "location": {"title": "A prime Caribbean location", "sub": "Bala Beach resort, María Chiquita — 90 minutes from Panama City, 15 minutes from Portobelo.", "directions": "Get directions"},
    "newsletter": {"title": "Join the Caribbean VIP club", "sub": "Get our secret Colón travel guide and exclusive direct-booking discounts.", "placeholder": "Your email address", "button": "Get the free guide", "disclaimer": "No spam — only real offers and travel tips."},
    "footer": {"about": "Your best vacation rental in María Chiquita, Colón. Luxury and comfort on Panama's Caribbean coast.", "contact": "Contact us", "links": "Explore", "rights": "All rights reserved.", "keywords_title": "Popular searches"},
    "wa_msg": "Hi! I'm interested in renting the beachfront apartment at Bala Beach, María Chiquita.",
}

C["es"] = {
    "title": "Alquiler Vacacional Frente al Mar en María Chiquita, Colón | Bala Beach Panamá",
    "meta_desc": "Alquiler vacacional de lujo frente al mar en Bala Beach, María Chiquita, Colón, Panamá. Playa caribeña privada, WiFi Starlink, seguridad 24/7. Reserva directo y ahorra las comisiones de Airbnb — desde $120/noche.",
    "keywords": "alquiler maria chiquita, bala beach panama, alquiler vacacional colon panama, casa frente al mar panama, alternativa airbnb colon, apartamento playa caribe panama, hospedaje buceo portobelo",
    "nav": {"amenities": "Amenidades", "gallery": "Galería", "tours": "Qué hacer", "reviews": "Reseñas", "faq": "Preguntas", "book": "Reservar Directo"},
    "hero": {
        "badge": "Mejor que Airbnb — Sin comisiones",
        "title": "Alquiler Vacacional Frente al Mar en María Chiquita",
        "sub": "Tu casa de playa privada en el Caribe de Panamá, costa de Colón. La alternativa #1 a los hoteles — playa privada, seguridad 24/7 y WiFi Starlink ultrarrápido.",
        "cta": "Reservar por WhatsApp",
        "cta2": "Ver en Airbnb",
        "price": "Desde $120 / noche",
    },
    "trust": ["Playa privada caribeña", "WiFi Starlink 100 Mbps+", "Seguridad 24/7 con garita", "Piscina y gimnasio"],
    "features": {
        "title": "Todo lo que necesitas para una estadía perfecta",
        "sub": "Equipado para el confort total — siéntete como en casa con amenidades premium.",
        "items": [
            ("wifi", "WiFi Starlink Rápido", "100 Mbps+ para teletrabajo"),
            ("ac", "Aire Acondicionado", "Habitaciones frescas y silenciosas"),
            ("kitchen", "Cocina Completa", "Totalmente equipada"),
            ("tv", "Smart TV", "Netflix y Prime incluidos"),
            ("parking", "Estacionamiento Privado", "Espacio seguro con garita"),
            ("bed", "Ropa de Cama Premium", "Calidad de hotel"),
        ],
    },
    "gallery": {"title": "Galería de fotos", "sub": "Explora cada rincón de nuestro apartamento frente al mar."},
    "why": {
        "title": "¿Por qué reservar directo con nosotros?",
        "sub": "Evita intermediarios y ahorra 15–20% en comisiones de servicio.",
        "direct": "Reserva directa",
        "ota": "Airbnb / Booking",
        "rows": [
            ("Mejor tarifa garantizada — sin comisiones", True, False),
            ("Concierge local de Colón y atención personal", True, False),
            ("Check-in flexible y privacidad total", True, False),
            ("Guía secreta del Caribe panameño gratis", True, False),
        ],
    },
    "tours": {
        "title": "Descubre la Costa Arriba de Colón",
        "sub": "Más allá de la playa privada, estás a minutos de aventuras inolvidables y buceo de clase mundial.",
        "items": [
            ("Buceo y snorkel en Portobelo", "Arrecifes de coral y barcos hundidos hacen de este uno de los mejores destinos de buceo en Panamá — a minutos.", "diving"),
            ("Ruinas históricas de Portobelo", "Explora las fortificaciones piratas Patrimonio de la UNESCO y la Iglesia del Cristo Negro, a 15 minutos.", "portobelo"),
            ("Tour a Isla Grande e Isla Mamey", "Toma un bote cercano hacia las aguas cristalinas de Isla Grande o haz snorkel en Isla Mamey.", "islands"),
            ("Aventura en la selva", "Senderismo en Sierra Llorona o safari fotográfico para ver monos y aves exóticas en su hábitat.", "jungle"),
        ],
    },
    "reviews": {"title": "Lo que dicen nuestros huéspedes", "sub": "Experiencias reales de viajeros de todo el mundo.", "source": "Verificado en Airbnb"},
    "faq": {
        "title": "Preguntas frecuentes",
        "sub": "Información clave para tu estancia en la costa de Colón.",
        "items": [
            ("¿Es segura la propiedad en Colón?", "Totalmente. Estamos dentro de un complejo privado con garita de seguridad 24/7. María Chiquita es una zona turística tranquila y familiar."),
            ("¿Qué tan rápido es el internet?", "Starlink de alta velocidad (100 Mbps+) — perfecto para videollamadas, streaming y trabajo remoto sin interrupciones."),
            ("¿Puedo reservar estancias cortas?", "Sí, aceptamos reservas desde 2 noches. También ofrecemos descuentos para estancias semanales y mensuales."),
            ("¿Qué ahorro al reservar directo?", "Reservar directo te ahorra aproximadamente 15–20% en comisiones que cobran plataformas como Airbnb y Booking."),
        ],
    },
    "location": {"title": "Una ubicación caribeña privilegiada", "sub": "Complejo Bala Beach, María Chiquita — a 90 minutos de Ciudad de Panamá y 15 de Portobelo.", "directions": "Cómo llegar"},
    "newsletter": {"title": "Únete al club VIP del Caribe", "sub": "Recibe nuestra guía secreta de Colón y descuentos exclusivos por reserva directa.", "placeholder": "Tu correo electrónico", "button": "Recibir guía gratis", "disclaimer": "Sin spam — solo ofertas reales y tips de viaje."},
    "footer": {"about": "Tu mejor alquiler vacacional en María Chiquita, Colón. Lujo y confort en el Caribe panameño.", "contact": "Contáctanos", "links": "Explorar", "rights": "Todos los derechos reservados.", "keywords_title": "Búsquedas populares"},
    "wa_msg": "¡Hola! Estoy interesado en alquilar el apartamento frente al mar en Bala Beach, María Chiquita.",
}

C["de"] = {
    "title": "Strand-Ferienwohnung in María Chiquita, Colón | Bala Beach Panama",
    "meta_desc": "Luxuriöse Ferienwohnung direkt am Strand im Bala Beach, María Chiquita, Colón, Panama. Privater Karibikstrand, Starlink-WLAN, 24/7-Sicherheit. Direkt buchen & Airbnb-Gebühren sparen — ab 120 $/Nacht.",
    "keywords": "ferienwohnung maria chiquita, bala beach panama, ferienhaus colon panama, strandhaus panama karibik, airbnb alternative colon, apartment strand panama, tauchen portobelo unterkunft",
    "nav": {"amenities": "Ausstattung", "gallery": "Galerie", "tours": "Aktivitäten", "reviews": "Bewertungen", "faq": "FAQ", "book": "Direkt buchen"},
    "hero": {
        "badge": "Besser als Airbnb — keine Gebühren",
        "title": "Strand-Ferienwohnung in María Chiquita",
        "sub": "Ihr privates Karibik-Strandhaus an Panamas Colón-Küste. Die Hotel-Alternative Nr. 1 — Privatstrand, 24/7-Sicherheit und schnelles Starlink-WLAN.",
        "cta": "Per WhatsApp buchen",
        "cta2": "Auf Airbnb ansehen",
        "price": "Ab 120 $ / Nacht",
    },
    "trust": ["Privater Karibikstrand", "Starlink-WLAN 100 Mbit/s+", "24/7-Sicherheit", "Pool & Fitnessstudio"],
    "features": {
        "title": "Alles für den perfekten Aufenthalt",
        "sub": "Ausgestattet für vollen Komfort — fühlen Sie sich wie zu Hause mit Premium-Ausstattung.",
        "items": [
            ("wifi", "Schnelles Starlink-WLAN", "100 Mbit/s+ für Homeoffice"),
            ("ac", "Klimaanlage", "Kühle, ruhige Schlafzimmer"),
            ("kitchen", "Voll ausgestattete Küche", "Komplett zum Kochen"),
            ("tv", "Smart-TV", "Netflix & Prime inklusive"),
            ("parking", "Privater Parkplatz", "Sicherer Stellplatz"),
            ("bed", "Premium-Bettwäsche", "Hotelqualität"),
        ],
    },
    "gallery": {"title": "Fotogalerie", "sub": "Entdecken Sie jeden Winkel unserer Strandwohnung."},
    "why": {
        "title": "Warum direkt bei uns buchen?",
        "sub": "Ohne Zwischenhändler sparen Sie 15–20 % an Servicegebühren.",
        "direct": "Direktbuchung",
        "ota": "Airbnb / Booking",
        "rows": [
            ("Bestpreisgarantie — keine Servicegebühren", True, False),
            ("Lokaler Colón-Concierge & persönlicher Service", True, False),
            ("Flexibler Check-in & volle Privatsphäre", True, False),
            ("Kostenloser Karibik-Insider-Reiseführer", True, False),
        ],
    },
    "tours": {
        "title": "Entdecken Sie die Costa Arriba, Colón",
        "sub": "Jenseits des Privatstrands sind Sie nur Minuten von unvergesslichen Abenteuern und Weltklasse-Tauchen entfernt.",
        "items": [
            ("Tauchen & Schnorcheln in Portobelo", "Korallenriffe und Schiffswracks machen dies zu einem der besten Tauchspots Panamas — nur Minuten entfernt.", "diving"),
            ("Historische Ruinen von Portobelo", "Erkunden Sie die UNESCO-Welterbe-Piratenfestungen und die Schwarze-Christus-Kirche, 15 Minuten entfernt.", "portobelo"),
            ("Tour nach Isla Grande & Isla Mamey", "Nehmen Sie ein Boot zu den kristallklaren Gewässern von Isla Grande oder schnorcheln Sie an der Isla Mamey.", "islands"),
            ("Regenwald-Abenteuer", "Wandern Sie in der Sierra Llorona oder gehen Sie auf Fotosafari, um Affen und exotische Vögel zu sehen.", "jungle"),
        ],
    },
    "reviews": {"title": "Was unsere Gäste sagen", "sub": "Echte Erfahrungen von Reisenden aus aller Welt.", "source": "Verifiziert auf Airbnb"},
    "faq": {
        "title": "Häufige Fragen",
        "sub": "Wichtige Informationen für Ihren Aufenthalt an der Colón-Küste.",
        "items": [
            ("Ist die Unterkunft in Colón sicher?", "Absolut. Wir befinden uns in einer privaten Anlage mit 24/7-Sicherheit. María Chiquita ist eine ruhige, familienfreundliche Touristengegend."),
            ("Wie schnell ist das Internet?", "Highspeed-Starlink (100 Mbit/s+) — perfekt für Videoanrufe, Streaming und Homeoffice ohne Unterbrechungen."),
            ("Kann ich Kurzaufenthalte buchen?", "Ja, wir akzeptieren Aufenthalte ab 2 Nächten. Für Wochen- und Monatsaufenthalte bieten wir Sonderrabatte."),
            ("Was spare ich bei Direktbuchung?", "Direktbuchung spart Ihnen rund 15–20 % an Servicegebühren, die Plattformen wie Airbnb und Booking berechnen."),
        ],
    },
    "location": {"title": "Eine erstklassige Karibik-Lage", "sub": "Bala-Beach-Anlage, María Chiquita — 90 Minuten von Panama-Stadt, 15 Minuten von Portobelo.", "directions": "Route anzeigen"},
    "newsletter": {"title": "Treten Sie dem Karibik-VIP-Club bei", "sub": "Erhalten Sie unseren geheimen Colón-Reiseführer und exklusive Direktbuchungs-Rabatte.", "placeholder": "Ihre E-Mail-Adresse", "button": "Gratis-Guide erhalten", "disclaimer": "Kein Spam — nur echte Angebote und Reisetipps."},
    "footer": {"about": "Ihre beste Ferienwohnung in María Chiquita, Colón. Luxus und Komfort an Panamas Karibikküste.", "contact": "Kontakt", "links": "Entdecken", "rights": "Alle Rechte vorbehalten.", "keywords_title": "Beliebte Suchen"},
    "wa_msg": "Hallo! Ich interessiere mich für die Anmietung der Strandwohnung im Bala Beach, María Chiquita.",
}

C["pt"] = {
    "title": "Aluguel de Temporada à Beira-Mar em María Chiquita, Colón | Bala Beach Panamá",
    "meta_desc": "Aluguel de temporada de luxo à beira-mar no Bala Beach, María Chiquita, Colón, Panamá. Praia caribenha privativa, WiFi Starlink, segurança 24/7. Reserve direto e economize as taxas do Airbnb — a partir de US$120/noite.",
    "keywords": "aluguel maria chiquita, bala beach panama, casa de temporada colon panama, casa de praia panama caribe, alternativa airbnb colon, apartamento praia panama, mergulho portobelo hospedagem",
    "nav": {"amenities": "Comodidades", "gallery": "Galeria", "tours": "O que fazer", "reviews": "Avaliações", "faq": "Perguntas", "book": "Reservar Direto"},
    "hero": {
        "badge": "Melhor que Airbnb — sem taxas",
        "title": "Aluguel de Temporada à Beira-Mar em María Chiquita",
        "sub": "Sua casa de praia privativa no Caribe do Panamá, costa de Colón. A alternativa nº 1 aos hotéis — praia privativa, segurança 24/7 e WiFi Starlink ultrarrápido.",
        "cta": "Reservar pelo WhatsApp",
        "cta2": "Ver no Airbnb",
        "price": "A partir de US$120 / noite",
    },
    "trust": ["Praia caribenha privativa", "WiFi Starlink 100 Mbps+", "Segurança 24/7", "Piscina e academia"],
    "features": {
        "title": "Tudo o que você precisa para uma estadia perfeita",
        "sub": "Equipado para o conforto total — sinta-se em casa com comodidades premium.",
        "items": [
            ("wifi", "WiFi Starlink Rápido", "100 Mbps+ para trabalho remoto"),
            ("ac", "Ar-condicionado", "Quartos frescos e silenciosos"),
            ("kitchen", "Cozinha Completa", "Totalmente equipada"),
            ("tv", "Smart TV", "Netflix e Prime inclusos"),
            ("parking", "Estacionamento Privativo", "Vaga segura"),
            ("bed", "Roupa de Cama Premium", "Qualidade de hotel"),
        ],
    },
    "gallery": {"title": "Galeria de fotos", "sub": "Explore cada canto do nosso apartamento à beira-mar."},
    "why": {
        "title": "Por que reservar direto conosco?",
        "sub": "Evite intermediários e economize 15–20% em taxas de serviço.",
        "direct": "Reserva direta",
        "ota": "Airbnb / Booking",
        "rows": [
            ("Melhor tarifa garantida — sem taxas de serviço", True, False),
            ("Concierge local de Colón e suporte pessoal", True, False),
            ("Check-in flexível e privacidade total", True, False),
            ("Guia secreto do Caribe panamenho grátis", True, False),
        ],
    },
    "tours": {
        "title": "Descubra a Costa Arriba, Colón",
        "sub": "Além da praia privativa, você está a minutos de aventuras inesquecíveis e mergulho de classe mundial.",
        "items": [
            ("Mergulho e snorkel em Portobelo", "Recifes de coral e naufrágios fazem deste um dos melhores pontos de mergulho do Panamá — a minutos.", "diving"),
            ("Ruínas históricas de Portobelo", "Explore as fortificações piratas Patrimônio da UNESCO e a Igreja do Cristo Negro, a 15 minutos.", "portobelo"),
            ("Passeio a Isla Grande e Isla Mamey", "Pegue um barco próximo até as águas cristalinas de Isla Grande ou faça snorkel na Isla Mamey.", "islands"),
            ("Aventura na floresta", "Faça trilhas na Sierra Llorona ou um safári fotográfico para ver macacos e aves exóticas.", "jungle"),
        ],
    },
    "reviews": {"title": "O que dizem nossos hóspedes", "sub": "Experiências reais de viajantes do mundo todo.", "source": "Verificado no Airbnb"},
    "faq": {
        "title": "Perguntas frequentes",
        "sub": "Informações essenciais para sua estadia na costa de Colón.",
        "items": [
            ("A propriedade é segura em Colón?", "Totalmente. Estamos em um condomínio privativo com segurança 24/7. María Chiquita é uma área turística tranquila e familiar."),
            ("Qual a velocidade da internet?", "Starlink de alta velocidade (100 Mbps+) — perfeito para videochamadas, streaming e trabalho remoto sem interrupções."),
            ("Posso reservar estadias curtas?", "Sim, aceitamos estadias a partir de 2 noites. Também oferecemos descontos para estadias semanais e mensais."),
            ("O que economizo reservando direto?", "Reservar direto economiza cerca de 15–20% em taxas cobradas por plataformas como Airbnb e Booking."),
        ],
    },
    "location": {"title": "Uma localização caribenha privilegiada", "sub": "Condomínio Bala Beach, María Chiquita — a 90 minutos da Cidade do Panamá e 15 de Portobelo.", "directions": "Como chegar"},
    "newsletter": {"title": "Entre no clube VIP do Caribe", "sub": "Receba nosso guia secreto de Colón e descontos exclusivos por reserva direta.", "placeholder": "Seu e-mail", "button": "Receber guia grátis", "disclaimer": "Sem spam — apenas ofertas reais e dicas de viagem."},
    "footer": {"about": "Seu melhor aluguel de temporada em María Chiquita, Colón. Luxo e conforto no Caribe panamenho.", "contact": "Fale conosco", "links": "Explorar", "rights": "Todos os direitos reservados.", "keywords_title": "Buscas populares"},
    "wa_msg": "Olá! Tenho interesse em alugar o apartamento à beira-mar no Bala Beach, María Chiquita.",
}

C["fr"] = {
    "title": "Location de Vacances en Bord de Mer à María Chiquita, Colón | Bala Beach Panama",
    "meta_desc": "Location de vacances de luxe en bord de mer au Bala Beach, María Chiquita, Colón, Panama. Plage privée des Caraïbes, WiFi Starlink, sécurité 24/7. Réservez en direct et évitez les frais Airbnb — dès 120 $/nuit.",
    "keywords": "location maria chiquita, bala beach panama, location vacances colon panama, maison plage panama caraibes, alternative airbnb colon, appartement plage panama, plongee portobelo hebergement",
    "nav": {"amenities": "Équipements", "gallery": "Galerie", "tours": "À faire", "reviews": "Avis", "faq": "FAQ", "book": "Réserver en direct"},
    "hero": {
        "badge": "Mieux qu'Airbnb — sans frais",
        "title": "Location de Vacances en Bord de Mer à María Chiquita",
        "sub": "Votre maison de plage privée sur la côte caraïbe de Colón, au Panama. L'alternative nº 1 à l'hôtel — plage privée, sécurité 24/7 et WiFi Starlink ultra-rapide.",
        "cta": "Réserver sur WhatsApp",
        "cta2": "Voir sur Airbnb",
        "price": "Dès 120 $ / nuit",
    },
    "trust": ["Plage privée des Caraïbes", "WiFi Starlink 100 Mbps+", "Sécurité 24/7", "Piscine & salle de sport"],
    "features": {
        "title": "Tout ce qu'il faut pour un séjour parfait",
        "sub": "Équipé pour un confort total — sentez-vous chez vous avec des prestations premium.",
        "items": [
            ("wifi", "WiFi Starlink rapide", "100 Mbps+ pour le télétravail"),
            ("ac", "Climatisation", "Chambres fraîches et calmes"),
            ("kitchen", "Cuisine complète", "Entièrement équipée"),
            ("tv", "Smart TV", "Netflix & Prime inclus"),
            ("parking", "Parking privé", "Place sécurisée"),
            ("bed", "Linge de lit premium", "Qualité hôtelière"),
        ],
    },
    "gallery": {"title": "Galerie photo", "sub": "Explorez chaque recoin de notre appartement en bord de mer."},
    "why": {
        "title": "Pourquoi réserver en direct avec nous ?",
        "sub": "Évitez les intermédiaires et économisez 15 à 20 % de frais de service.",
        "direct": "Réservation directe",
        "ota": "Airbnb / Booking",
        "rows": [
            ("Meilleur tarif garanti — sans frais de service", True, False),
            ("Conciergerie locale de Colón & service personnel", True, False),
            ("Check-in flexible & intimité totale", True, False),
            ("Guide secret des Caraïbes offert", True, False),
        ],
    },
    "tours": {
        "title": "Découvrez la Costa Arriba, Colón",
        "sub": "Au-delà de la plage privée, vous êtes à quelques minutes d'aventures inoubliables et de plongée de classe mondiale.",
        "items": [
            ("Plongée & snorkeling à Portobelo", "Récifs coralliens et épaves font de ce site l'un des meilleurs spots de plongée du Panama — à quelques minutes.", "diving"),
            ("Ruines historiques de Portobelo", "Explorez les forts pirates classés UNESCO et l'église du Christ Noir, à 15 minutes.", "portobelo"),
            ("Excursion à Isla Grande & Isla Mamey", "Prenez un bateau vers les eaux cristallines d'Isla Grande ou faites du snorkeling à Isla Mamey.", "islands"),
            ("Aventure en forêt tropicale", "Randonnée à la Sierra Llorona ou safari photo pour observer singes et oiseaux exotiques.", "jungle"),
        ],
    },
    "reviews": {"title": "Ce que disent nos hôtes", "sub": "Expériences réelles de voyageurs du monde entier.", "source": "Vérifié sur Airbnb"},
    "faq": {
        "title": "Questions fréquentes",
        "sub": "Informations clés pour votre séjour sur la côte de Colón.",
        "items": [
            ("La propriété est-elle sûre à Colón ?", "Absolument. Nous sommes dans une résidence privée avec sécurité 24/7. María Chiquita est une zone touristique calme et familiale."),
            ("Quelle est la vitesse d'internet ?", "Starlink haut débit (100 Mbps+) — parfait pour les visioconférences, le streaming et le télétravail sans interruption."),
            ("Puis-je réserver de courts séjours ?", "Oui, nous acceptons les séjours à partir de 2 nuits. Nous proposons aussi des réductions pour les séjours hebdomadaires et mensuels."),
            ("Qu'est-ce que j'économise en réservant en direct ?", "Réserver en direct vous fait économiser environ 15 à 20 % de frais facturés par des plateformes comme Airbnb et Booking."),
        ],
    },
    "location": {"title": "Un emplacement caraïbe d'exception", "sub": "Résidence Bala Beach, María Chiquita — à 90 minutes de Panama City et 15 de Portobelo.", "directions": "Itinéraire"},
    "newsletter": {"title": "Rejoignez le club VIP des Caraïbes", "sub": "Recevez notre guide secret de Colón et des réductions exclusives en réservation directe.", "placeholder": "Votre adresse e-mail", "button": "Recevoir le guide gratuit", "disclaimer": "Pas de spam — uniquement de vraies offres et des conseils de voyage."},
    "footer": {"about": "Votre meilleure location de vacances à María Chiquita, Colón. Luxe et confort sur la côte caraïbe du Panama.", "contact": "Contactez-nous", "links": "Explorer", "rights": "Tous droits réservés.", "keywords_title": "Recherches populaires"},
    "wa_msg": "Bonjour ! Je suis intéressé(e) par la location de l'appartement en bord de mer au Bala Beach, María Chiquita.",
}

# Footer SEO keyword cloud (shared, English-leaning long-tail — good for all)
FOOTER_KEYWORDS = [
    "María Chiquita Beachfront Rentals", "Bala Beach Panama Rental", "Colón Panama Vacation Homes",
    "Airbnb Alternative María Chiquita", "Scuba Diving Portobelo Panama", "Caribbean Beach House Panama",
    "Short Term Rental Colón", "Ocean View Apartment María Chiquita", "Starlink WiFi Beach Rental Panama",
    "Family Beach House Colón", "Romantic Getaway Panama Caribbean", "Direct Booking Beach Rental Panama",
    "Vacation Rental near Portobelo", "Pet Friendly Beach Rental Panama", "Weekend Getaway from Panama City",
]
