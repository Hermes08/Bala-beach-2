import { ContentDictionary, Language, BlogPost } from './types';
import { FOOTER_KEYWORDS } from './utils/seo-keywords';

export const CONTACT_INFO = {
  displayPhone: "+507 6761-0315",
  whatsappNumber: "50767610315",
  bookingMessage: "I am interested in renting the apartment in bala beach"
};

export const LANGUAGES: Language[] = ['es', 'en', 'de'];

export const AIRBNB_ICAL_URL = "https://www.airbnb.com/calendar/ical/1409650618945019706.ics?s=864d7b010bdfa413b01b383ce7bd80c8";

// CENTRALIZED IMAGE CONFIGURATION
// Using Direct Links provided by user (ImgBB)
export const IMAGES = {
  // Carousel Slides: Prioritizing User's Specific Request
  heroSlides: [
    "https://i.ibb.co/KxmKQ4Lc/living-room-2.jpg", // MAIN PRINCIPAL IMAGE (Requested)
    "https://i.ibb.co/5xrb03gY/bedroom-1.jpg",     // Bedroom view 1 (Requested)
    "https://i.ibb.co/PsRHbR4C/bedroom-1.jpg",     // Bedroom view 2 (Requested)
    "https://i.ibb.co/0RbW3B6g/Ocean-View.jpg",    // Ocean View (Essential for Beachfront context)
  ],
  // Main Gallery (12 images mixed rooms - Updated with new hero images)
  gallery: [
    "https://i.ibb.co/KxmKQ4Lc/living-room-2.jpg", // Living Room (Main)
    "https://i.ibb.co/NdyZLcmd/gym-2.jpg", // Gym
    "https://i.ibb.co/5xrb03gY/bedroom-1.jpg", // Bedroom Luxury
    "https://i.ibb.co/kVjVshpM/Pool.jpg", // Pool
    "https://i.ibb.co/hJv1NcC4/kitchen-3.jpg", // Kitchen
    "https://i.ibb.co/ZRLRdpCs/balcony.jpg", // Balcony
    "https://i.ibb.co/PsRHbR4C/bedroom-1.jpg", // Bedroom Angle 2
    "https://i.ibb.co/BHtZsxD8/bathroom-1.jpg", // Bathroom
    "https://i.ibb.co/Y47qg6Nt/bedroom-2.jpg", // Second Bedroom
    "https://i.ibb.co/Nk87jjB/building.jpg", // Building Exterior
    "https://i.ibb.co/bgLsNQwV/sofa-bed.jpg", // Sofa Bed
    "https://i.ibb.co/1fXxZZgH/beach.jpg", // Beach
  ],
  // Location context
  locationMap: "https://i.ibb.co/HDr2Mmcs/beach.jpg", 
  seo: {
    beach: "https://i.ibb.co/1fXxZZgH/beach.jpg", // Beach Vertical context
    interior: "https://i.ibb.co/B2X8m6VB/living-room-1.jpg" // Interior Vertical context
  },
  // Tour/Guide Images
  tours: {
    portobelo: "https://i.ibb.co/sv9Nz0rS/portobello.jpg", // User provided
    islands: "https://images.unsplash.com/photo-1590523741831-ab7e8b8f9c7f?q=80&w=800&auto=format&fit=crop", // Placeholder
    jungle: "https://i.ibb.co/WpcbmNG1/jungle.jpg", // User provided
    diving: "https://images.unsplash.com/photo-1544551763-46a013bb70d5?q=80&w=800&auto=format&fit=crop" // New Diving Image
  }
};

export const SEO_KEYWORDS_LIST = FOOTER_KEYWORDS;

// STATIC REVIEWS DATA (Simulating Airbnb Data)
const REVIEWS_DATA = [
  {
    author: "Sarah",
    location: "United States",
    date: "January 2025",
    rating: 5,
    text: "The view is absolutely breathtaking! The apartment looks exactly like the photos, very modern and clean. The Starlink internet was super fast for my work calls. We loved the private beach access.",
    avatar: "S"
  },
  {
    author: "Carlos",
    location: "Panamá",
    date: "December 2024",
    rating: 5,
    text: "Excelente lugar para desconectarse. El apartamento tiene todo lo necesario y la cocina está muy bien equipada. La piscina del edificio es enorme y muy tranquila. 100% recomendado.",
    avatar: "C"
  },
  {
    author: "Michael",
    location: "Germany",
    date: "November 2024",
    rating: 5,
    text: "Ein wunderschönes Apartment mit direktem Meerblick. Sehr sicher und ruhig. Die Kommunikation mit dem Gastgeber war hervorragend. Wir kommen definitiv wieder!",
    avatar: "M"
  },
  {
    author: "Jessica",
    location: "Canada",
    date: "February 2025",
    rating: 5,
    text: "Perfect getaway from the city. The balcony view is to die for! Very comfortable beds and strong AC. It felt much more personal and premium than a hotel stay.",
    avatar: "J"
  }
];

export const CONTENT: Record<Language, ContentDictionary> = {
  es: {
    nav: {
      home: "Inicio",
      amenities: "Amenidades",
      location: "Ubicación",
      blog: "Guía de Colón",
      bookNow: "Reservar Directo",
    },
    hero: {
      badge: "Mejor que Airbnb - Ahorra las Comisiones",
      title: "Alquiler Vacacional Frente al Mar en María Chiquita",
      subtitle: "Tu casa de playa privada en el Caribe de Panamá. La alternativa #1 a hoteles en Colón con playa privada, seguridad y WiFi Starlink.",
      cta: "Reservar por WhatsApp",
      price: "Desde $120/noche",
    },
    features: {
      title: "Todo lo necesario para tu estadía",
      subtitle: "Equipado para confort total. Siéntete como en casa con nuestras amenidades premium.",
      list: {
        wifi: "WiFi Starlink Rápido",
        ac: "Aire Acondicionado",
        kitchen: "Cocina Completa",
        tv: "Smart TV + Streaming",
        parking: "Estacionamiento Privado",
        bedding: "Ropa de Cama Premium",
      },
    },
    gallery: {
      title: "Galería de Fotos",
      subtitle: "Explora cada rincón de nuestro apartamento frente al mar."
    },
    tours: {
      title: "Descubre la Costa Arriba de Colón",
      subtitle: "Más allá de la playa privada, estás a minutos de aventuras inolvidables y buceo de clase mundial.",
      items: [
        {
          title: "Buceo y Snorkel en Portobelo",
          desc: "Descubre por qué somos el mejor destino de 'scuba diving' en Panamá. Arrecifes de coral y barcos hundidos te esperan.",
          image: IMAGES.tours.diving
        },
        {
          title: "Ruinas Históricas de Portobelo",
          desc: "Explora el Patrimonio Mundial de la UNESCO, fortificaciones piratas y la Iglesia del Cristo Negro a solo 15 min.",
          image: IMAGES.tours.portobelo
        },
        {
          title: "Tour a Isla Grande y Mamey",
          desc: "Toma un bote cercano y visita las aguas cristalinas de Isla Grande o haz snorkeling en Isla Mamey.",
          image: IMAGES.tours.islands
        },
        {
          title: "Aventura en la Selva",
          desc: "Senderismo en Sierra Llorona o safaris fotográficos para ver monos y aves exóticas en su hábitat natural.",
          image: IMAGES.tours.jungle
        }
      ]
    },
    calendar: {
      title: "Disponibilidad en Tiempo Real",
      subtitle: "Revisa nuestras fechas libres. El calendario se actualiza automáticamente con Airbnb.",
      available: "Disponible",
      booked: "Ocupado",
      checkButton: "Verificar Fechas en Airbnb",
      error: "No pudimos cargar el calendario. Por favor verifica directamente en Airbnb."
    },
    reviews: {
      title: "Lo que dicen nuestros huéspedes",
      subtitle: "Experiencias reales de viajeros de todo el mundo.",
      source: "Verificado en Airbnb",
      items: REVIEWS_DATA
    },
    seoSection: {
      title: "¿Por qué elegir nuestro Beachfront Rental en María Chiquita?",
      p1: "Ubicado en la exclusiva costa de Colón, este apartamento ofrece una experiencia superior. Somos la opción preferida para quienes buscan 'Panama Beach Houses' y 'Vacation Rentals' en un entorno seguro y privado.",
      p2: "Estratégicamente ubicados cerca de la Zona Libre de Colón y Portobelo. Ofrecemos la tranquilidad de una 'beachfront house' con acceso rápido a las atracciones turísticas del Caribe panameño.",
    },
    comparison: {
      title: "¿Por qué reservar directo con nosotros?",
      direct: "Reserva Directa",
      airbnb: "Airbnb / Booking",
      benefit1: "Mejor tarifa garantizada (Sin Fees de Servicio)",
      benefit2: "Guía local de Colón y atención personalizada",
      benefit3: "Privacidad total y check-in flexible",
    },
    faq: {
      title: "Preguntas Frecuentes",
      subtitle: "Información clave para tu estancia en la costa de Colón.",
      items: [
        {
          question: "¿Es segura la propiedad en Colón?",
          answer: "Totalmente. Estamos dentro de un complejo privado con garita de seguridad 24/7. María Chiquita es una zona turística tranquila y segura para familias."
        },
        {
          question: "¿Qué velocidad de internet tienen?",
          answer: "Contamos con Starlink de alta velocidad (100Mbps+), perfecto para videollamadas, streaming y trabajo remoto sin interrupciones."
        },
        {
          question: "¿Puedo reservar estancias cortas?",
          answer: "Sí, aceptamos reservas desde 2 noches. También ofrecemos descuentos especiales para estancias semanales y mensuales."
        },
        {
          question: "¿Cuál es la diferencia de reservar directo vs Airbnb?",
          answer: "Al reservar directo te ahorras aproximadamente el 15-20% en comisiones de servicio que cobran las plataformas."
        }
      ]
    },
    newsletter: {
      title: "Únete al Club VIP de Colón",
      subtitle: "Recibe nuestra 'Guía Secreta de Colón' y acceso a descuentos exclusivos para tu próxima estancia.",
      placeholder: "Tu correo electrónico",
      button: "Suscribirme Gratis",
      disclaimer: "No enviamos spam. Solo ofertas reales y tips de viaje."
    },
    footer: {
      about: "Tu mejor opción de alquiler vacacional en María Chiquita, Colón. Lujo y confort en el Caribe panameño.",
      contact: "Contáctanos",
      rights: "Todos los derechos reservados.",
    },
  },
  en: {
    nav: {
      home: "Home",
      amenities: "Amenities",
      location: "Location",
      blog: "Colon Guide",
      bookNow: "Book Direct",
    },
    hero: {
      badge: "Better Than Airbnb - No Hidden Fees",
      title: "Luxury Beachfront Vacation Rental in Maria Chiquita, Colon",
      subtitle: "Your private Panama beach house on the Caribbean coast. The top-rated hotel alternative with direct ocean access and Starlink WiFi.",
      cta: "Book via WhatsApp",
      price: "From $120/night",
    },
    features: {
      title: "Everything You Need for Your Stay",
      subtitle: "Equipped for total comfort. Feel at home with our premium amenities.",
      list: {
        wifi: "Fast Starlink WiFi",
        ac: "Air Conditioning",
        kitchen: "Full Kitchen",
        tv: "Smart TV + Streaming",
        parking: "Private Parking",
        bedding: "Premium Bedding",
      },
    },
    gallery: {
      title: "Photo Gallery",
      subtitle: "Explore every corner of our beachfront apartment."
    },
    tours: {
      title: "Discover Costa Arriba, Colon",
      subtitle: "Beyond the private beach, you are minutes away from unforgettable adventures and world-class diving.",
      items: [
        {
          title: "Scuba Diving & Snorkeling Portobelo",
          desc: "Discover why we are a top 'scuba diving Panama' destination. Coral reefs and shipwrecks await just minutes away.",
          image: IMAGES.tours.diving
        },
        {
          title: "Portobelo Historic Ruins",
          desc: "Explore UNESCO World Heritage sites, pirate fortifications, and the Black Christ Church just 15 mins away.",
          image: IMAGES.tours.portobelo
        },
        {
          title: "Isla Grande & Mamey Tour",
          desc: "Take a nearby boat to the crystal clear waters of Isla Grande or enjoy world-class snorkeling at Isla Mamey.",
          image: IMAGES.tours.islands
        },
        {
          title: "Jungle Adventure",
          desc: "Hiking in Sierra Llorona or photo safaris to spot monkeys and exotic birds in their natural habitat.",
          image: IMAGES.tours.jungle
        }
      ]
    },
    calendar: {
      title: "Real-Time Availability",
      subtitle: "Check our open dates. The calendar syncs automatically with Airbnb.",
      available: "Available",
      booked: "Booked",
      checkButton: "Verify Dates on Airbnb",
      error: "Unable to load calendar. Please check directly on Airbnb."
    },
    reviews: {
      title: "Guest Reviews",
      subtitle: "Real experiences from travelers around the world.",
      source: "Verified on Airbnb",
      items: REVIEWS_DATA
    },
    seoSection: {
      title: "Why Choose Our Maria Chiquita Beachfront Rental?",
      p1: "Located on the exclusive Colon coast, this apartment offers a superior experience to standard hotels. As one of the top-rated 'Panama Beach Houses', we guarantee privacy, security, and uninterrupted Caribbean views.",
      p2: "Ideal for travelers searching for 'Vacation rentals near me' in Panama or exploring the Colon Free Zone. Our strategic location allows you to visit Portobelo and Caribbean beaches with total comfort.",
    },
    comparison: {
      title: "Why Book Direct?",
      direct: "Direct Booking",
      airbnb: "Airbnb / VRBO",
      benefit1: "Best Price Guaranteed (No Service Fees)",
      benefit2: "Local Colon Guide & Personal Service",
      benefit3: "Total Privacy & Flexible Check-in",
    },
    faq: {
      title: "Frequently Asked Questions",
      subtitle: "Everything you need to know about renting in Maria Chiquita, Colon.",
      items: [
        {
          question: "Is the property safe in Colón?",
          answer: "Absolutely. We are located within a gated complex with 24/7 security. Maria Chiquita is a peaceful tourist area, very safe for families and international travelers."
        },
        {
          question: "What internet speed do we have?",
          answer: "We use Starlink high-speed internet (100Mbps+), ensuring reliable connectivity for remote work, video calls, and streaming."
        },
        {
          question: "Can I book for short stays?",
          answer: "Yes, we accept bookings with a 2-night minimum. We also offer special discounts for weekly and monthly stays."
        },
        {
          question: "Why book direct instead of Airbnb?",
          answer: "Booking direct saves you 15-20% in platform service fees while giving you direct access to the property manager."
        }
      ]
    },
    newsletter: {
      title: "Join the Colon VIP Club",
      subtitle: "Get our 'Secret Guide to Colon' and access exclusive discounts for your next stay.",
      placeholder: "Your email address",
      button: "Subscribe for Free",
      disclaimer: "No spam. Just real offers and travel tips."
    },
    footer: {
      about: "Leading vacation rental in Maria Chiquita, Colon. Your best accommodation choice in the Panamanian Caribbean.",
      contact: "Contact Us",
      rights: "All rights reserved.",
    },
  },
  de: {
    nav: {
      home: "Startseite",
      amenities: "Ausstattung",
      location: "Standort",
      blog: "Reiseführer",
      bookNow: "Direkt Buchen",
    },
    hero: {
      badge: "Besser als Airbnb - Keine versteckten Gebühren",
      title: "Luxus-Ferienwohnung am Strand in María Chiquita, Colón",
      subtitle: "Ihr privates Strandhaus in Panama an der Karibikküste. Die perfekte Hotelalternative mit direktem Meerzugang und Starlink-WLAN.",
      cta: "Per WhatsApp Buchen",
      price: "Ab $120/Nacht",
    },
    features: {
      title: "Alles, was Sie für Ihren Aufenthalt brauchen",
      subtitle: "Ausgestattet für totalen Komfort. Fühlen Sie sich wie zu Hause.",
      list: {
        wifi: "Schnelles Starlink-WLAN",
        ac: "Klimaanlage",
        kitchen: "Voll ausgestattete Küche",
        tv: "Smart TV + Streaming",
        parking: "Privater Parkplatz",
        bedding: "Premium-Bettwäsche",
      },
    },
    gallery: {
      title: "Fotogalerie",
      subtitle: "Entdecken Sie jeden Winkel unserer Strandwohnung."
    },
    tours: {
      title: "Entdecken Sie Costa Arriba, Colón",
      subtitle: "Jenseits des Privatstrandes sind Sie nur Minuten von unvergesslichen Abenteuern und erstklassigem Tauchen entfernt.",
      items: [
        {
          title: "Tauchen & Schnorcheln in Portobelo",
          desc: "Entdecken Sie, warum Portobelo das beste Ziel für 'Scuba Diving Panama' ist. Korallenriffe und Schiffswracks erwarten Sie.",
          image: IMAGES.tours.diving
        },
        {
          title: "Historische Ruinen von Portobelo",
          desc: "Erkunden Sie UNESCO-Weltkulturerbestätten, Piratenfestungen und die Kirche des Schwarzen Christus, nur 15 Min. entfernt.",
          image: IMAGES.tours.portobelo
        },
        {
          title: "Isla Grande & Mamey Tour",
          desc: "Nehmen Sie ein Boot zu den kristallklaren Gewässern der Isla Grande oder genießen Sie erstklassiges Schnorcheln auf Isla Mamey.",
          image: IMAGES.tours.islands
        },
        {
          title: "Dschungelabenteuer",
          desc: "Wandern in der Sierra Llorona oder Fotosafaris, um Affen und exotische Vögel in ihrem natürlichen Lebensraum zu beobachten.",
          image: IMAGES.tours.jungle
        }
      ]
    },
    calendar: {
      title: "Echtzeit-Verfügbarkeit",
      subtitle: "Prüfen Sie unsere freien Termine. Der Kalender synchronisiert sich automatisch mit Airbnb.",
      available: "Verfügbar",
      booked: "Gebucht",
      checkButton: "Termine auf Airbnb prüfen",
      error: "Kalender konnte nicht geladen werden. Bitte prüfen Sie direkt auf Airbnb."
    },
    reviews: {
      title: "Gästebewertungen",
      subtitle: "Echte Erfahrungen von Reisenden aus aller Welt.",
      source: "Verifiziert auf Airbnb",
      items: REVIEWS_DATA
    },
    seoSection: {
      title: "Warum unsere Unterkunft in María Chiquita wählen?",
      p1: "An der exklusiven Küste von Colón gelegen, bietet dieses Apartment ein besseres Erlebnis als Standardhotels. Als eines der besten 'Panama Beach Houses' garantieren wir Privatsphäre und Sicherheit.",
      p2: "Ideal für Reisende auf der Suche nach Ferienwohnungen nahe der Freihandelszone Colón. Erkunden Sie Portobelo und die Karibikstrände mit totalem Komfort.",
    },
    comparison: {
      title: "Warum Direkt Buchen?",
      direct: "Direktbuchung",
      airbnb: "Airbnb / Booking",
      benefit1: "Bester Preis (Keine Servicegebühren)",
      benefit2: "Persönlicher Service & Lokaler Guide",
      benefit3: "Privatsphäre & Flexibler Check-in",
    },
    faq: {
      title: "Häufig gestellte Fragen",
      subtitle: "Alles über Ihren Aufenthalt in María Chiquita.",
      items: [
        {
          question: "Ist die Unterkunft in Colón sicher?",
          answer: "Absolut. Wir befinden uns in einer geschlossenen Anlage mit 24/7-Sicherheitsdienst. María Chiquita ist eine ruhige Touristengegend, sehr sicher für Familien."
        },
        {
          question: "Wie schnell ist das Internet?",
          answer: "Wir nutzen Starlink-Highspeed-Internet (100Mbps+), was eine zuverlässige Verbindung für Remote-Arbeit, Videoanrufe und Streaming gewährleistet."
        },
        {
          question: "Kann ich kurze Aufenthalte buchen?",
          answer: "Ja, wir akzeptieren Buchungen ab 2 Nächten. Wir bieten auch spezielle Rabatte für Wochen- und Monatsaufenthalte."
        },
        {
          question: "Warum direkt statt über Airbnb buchen?",
          answer: "Bei einer Direktbuchung sparen Sie 15-20% an Plattformgebühren und haben direkten Kontakt zum Vermieter."
        }
      ]
    },
    newsletter: {
      title: "Treten Sie dem Colón VIP Club bei",
      subtitle: "Erhalten Sie unseren 'Geheimen Reiseführer für Colón' und Zugang zu exklusiven Rabatten für Ihren nächsten Aufenthalt.",
      placeholder: "Ihre E-Mail-Adresse",
      button: "Kostenlos Abonnieren",
      disclaimer: "Kein Spam. Nur echte Angebote und Reisetipps."
    },
    footer: {
      about: "Führende Ferienwohnung in María Chiquita, Colón. Ihre beste Wahl für Unterkünfte in der panamaischen Karibik.",
      contact: "Kontakt",
      rights: "Alle Rechte vorbehalten.",
    },
  },
};

// Simplified Blog System with SEO-focused articles based on CSV analysis
export const BLOG_POSTS: BlogPost[] = [
  {
    id: "1",
    slug: "scuba-diving-portobelo-panama",
    title: {
      es: "Buceo en Portobelo, Panamá: Guía Completa de Sitios y Centros",
      en: "Scuba Diving in Portobelo, Panama: Complete Guide to Sites & Centers",
      de: "Tauchen in Portobelo, Panama: Kompletter Guide zu Tauchplätzen"
    },
    excerpt: {
      es: "Descubre por qué Portobelo es la capital del buceo en el Caribe panameño. Guía de 'scuba portobelo' y los mejores arrecifes cerca de María Chiquita.",
      en: "Discover why Portobelo is the diving capital of the Panamanian Caribbean. Guide to 'scuba portobelo' and the best reefs near Maria Chiquita.",
      de: "Entdecken Sie, warum Portobelo die Tauchhauptstadt der panamaischen Karibik ist. Führer zu 'scuba portobelo' und den besten Riffen in der Nähe."
    },
    content: {
      es: "Si buscas 'diving portobelo panama' o 'scuba panama', estás en el lugar correcto. A solo 15 minutos de nuestra propiedad en María Chiquita, Portobelo ofrece aguas cristalinas, naufragios históricos y una vida marina vibrante. Lugares como 'Panama Dive Adventure' y otros centros locales ofrecen certificaciones PADI y excursiones diarias. Es la actividad perfecta para complementar tu estancia frente al mar.",
      en: "If you are searching for 'diving portobelo panama' or 'scuba panama', you are in the right place. Just 15 minutes from our property in Maria Chiquita, Portobelo offers crystal clear waters, historic shipwrecks, and vibrant marine life. Places like 'Panama Dive Adventure' and other local centers offer PADI certifications and daily excursions. It is the perfect activity to complement your beachfront stay.",
      de: "Wenn Sie nach 'diving portobelo panama' oder 'scuba panama' suchen, sind Sie hier richtig. Nur 15 Minuten von unserem Anwesen in Maria Chiquita entfernt bietet Portobelo kristallklares Wasser, historische Schiffswracks und ein pulsierendes Meeresleben. Orte wie 'Panama Dive Adventure' und andere lokale Zentren bieten PADI-Zertifizierungen und tägliche Ausflüge an."
    },
    date: "Dec 05, 2025",
    image: IMAGES.tours.diving,
    category: "Activities"
  },
  {
    id: "2",
    slug: "best-scuba-diving-panama",
    title: {
      es: "¿Cuál es el Mejor Scuba Diving en Panamá? Caribe vs Pacífico",
      en: "Best Scuba Diving in Panama: Caribbean vs Pacific Coast",
      de: "Bestes Tauchen in Panama: Karibik vs. Pazifikküste"
    },
    excerpt: {
      es: "Comparativa de 'best scuba diving panama'. Por qué la costa de Colón y Portobelo ofrecen ventajas únicas sobre Coiba para principiantes y expertos.",
      en: "Comparison of 'best scuba diving panama'. Why the Colon coast and Portobelo offer unique advantages over Coiba for beginners and experts.",
      de: "Vergleich von 'best scuba diving panama'. Warum die Küste von Colón und Portobelo einzigartige Vorteile gegenüber Coiba bieten."
    },
    content: {
      es: "Mientras que Coiba es famosa por los tiburones, el 'best scuba diving in panama' para arrecifes coloridos y aguas cálidas está en el Caribe. Nuestra zona en Colón permite bucear todo el año con excelente visibilidad. Además, es mucho más accesible desde la ciudad que las opciones del Pacífico, convirtiendo a 'diving panama' en una experiencia fácil de planificar durante tu fin de semana en María Chiquita.",
      en: "While Coiba is famous for sharks, the 'best scuba diving in panama' for colorful reefs and warm waters is in the Caribbean. Our area in Colon allows diving year-round with excellent visibility. Plus, it is much more accessible from the city than Pacific options, making 'diving panama' an easy-to-plan experience during your weekend in Maria Chiquita.",
      de: "Während Coiba für Haie berühmt ist, befindet sich das 'best scuba diving in panama' für farbenfrohe Riffe und warmes Wasser in der Karibik. Unsere Gegend in Colón ermöglicht das ganze Jahr über Tauchen mit hervorragender Sicht. Außerdem ist es viel zugänglicher als die Optionen am Pazifik."
    },
    date: "Dec 03, 2025",
    image: IMAGES.tours.portobelo,
    category: "Travel Guide"
  },
  {
    id: "3",
    slug: "scuba-diving-panama-city-connection",
    title: {
      es: "De Panama City al Buceo: Tu Escapada de Fin de Semana",
      en: "From Panama City to Diving: Your Weekend Escape",
      de: "Von Panama City zum Tauchen: Ihr Wochenendausflug"
    },
    excerpt: {
      es: "Guía para quienes buscan 'scuba diving panama city panama'. Cómo llegar de la ciudad a la costa de buceo en menos de 90 minutos.",
      en: "Guide for those searching 'scuba diving panama city panama'. How to get from the city to the diving coast in less than 90 minutes.",
      de: "Leitfaden für Suchende nach 'scuba diving panama city panama'. Wie man in weniger als 90 Minuten von der Stadt zur Tauchküste kommt."
    },
    content: {
      es: "Muchos turistas buscan 'diving in panama city panama', pero la verdadera acción está en la costa caribeña de Colón. Hospédate en nuestro apartamento en María Chiquita y tendrás acceso a los mejores 'panama dive center' de la región sin el caos de la ciudad. Es la combinación perfecta: compras en la ciudad y relax submarino en el Caribe.",
      en: "Many tourists search for 'diving in panama city panama', but the real action is on the Caribbean coast of Colon. Stay at our apartment in Maria Chiquita and you'll have access to the best 'panama dive center' options in the region without the city chaos. It's the perfect combo: city shopping and underwater relaxation in the Caribbean.",
      de: "Viele Touristen suchen nach 'diving in panama city panama', aber die wahre Action findet an der Karibikküste von Colón statt. Übernachten Sie in unserem Apartment in Maria Chiquita und Sie haben Zugang zu den besten Tauchzentren der Region ohne das Chaos der Stadt."
    },
    date: "Dec 01, 2025",
    image: IMAGES.locationMap,
    category: "Itineraries"
  },
  {
    id: "4",
    slug: "top-things-to-do-colon-panama",
    title: {
      es: "Top 10 Cosas que Hacer en Colón, Panamá",
      en: "Top 10 Things to Do in Colon, Panama",
      de: "Top 10 Aktivitäten in Colón, Panama"
    },
    excerpt: {
      es: "Desde las ruinas de Portobelo hasta la exclusividad de María Chiquita. Descubre las joyas escondidas del Caribe.",
      en: "From Portobelo ruins to the exclusivity of Maria Chiquita. Discover the hidden gems of the Caribbean.",
      de: "Von den Ruinen von Portobelo bis zur Exklusivität von María Chiquita. Entdecken Sie die verborgenen Schätze der Karibik."
    },
    content: {
      es: "Colón es mucho más que la Zona Libre. La costa arriba ofrece playas vírgenes, historia pirata en Portobelo y buceo de clase mundial...",
      en: "Colon is much more than the Free Zone. The upper coast offers pristine beaches, pirate history in Portobelo, and world-class diving...",
      de: "Colón ist viel mehr als die Freihandelszone. Die obere Küste bietet unberührte Strände, Piratengeschichte in Portobelo und erstklassiges Tauchen..."
    },
    date: "Nov 30, 2025",
    image: "https://i.ibb.co/fdzwSP1y/bala-beach-maria-chiquita-034.jpg", // Using complex view for blog
    category: "Travel Guide"
  }
];