
// SEO Keyword Generator based on "Comprehensive SEO Analysis Final Report"
// Target Market: Panama (Maria Chiquita, Colon)
// Strategy: Combinatorial generation of Long-Tail and High-Volume keywords

const LOCATIONS = [
  "Maria Chiquita",
  "Colon Panama",
  "Panama Caribbean Coast",
  "Portobelo",
  "Bala Beach",
  "Playa Maria Chiquita",
  "Colon Province",
  "Caribbean Panama",
  "Near Panama Canal",
  "Costa Arriba Colon"
];

const PROPERTY_TYPES = [
  "Vacation Rental",
  "Beachfront Rental",
  "Short Term Rental",
  "Airbnb Alternative",
  "Beach House",
  "Apartment",
  "Condo",
  "Villa",
  "Holiday Home",
  "Accommodation"
];

const FEATURES = [
  "with Pool",
  "Ocean View",
  "Beachfront",
  "Pet Friendly",
  "with Starlink WiFi",
  "Secure",
  "Private Beach",
  "Luxury",
  "Modern",
  "Family Friendly"
];

const INTENTS = [
  "Rent",
  "Book",
  "Stay in",
  "Best",
  "Cheap",
  "Luxury",
  "Private",
  "Safe"
];

// Tier 1: High Volume Generic (From PDF)
const TIER_1_SEEDS = [
  "vacation home for rent near me",
  "vacation rentals colon panama",
  "beach houses for rent panama",
  "panama beach rentals",
  "maria chiquita hotels"
];

// Tier 2: Branded/Competitor (From PDF)
const TIER_2_SEEDS = [
  "airbnb maria chiquita",
  "vrbo colon panama",
  "booking com maria chiquita",
  "better than airbnb colon",
  "direct booking vacation rental"
];

export const generateKeywords = (): string[] => {
  let keywords: string[] = [...TIER_1_SEEDS, ...TIER_2_SEEDS];

  // Strategy 1: Location + Property Type (e.g., "Maria Chiquita Vacation Rental")
  LOCATIONS.forEach(loc => {
    PROPERTY_TYPES.forEach(type => {
      keywords.push(`${loc} ${type}`);
      keywords.push(`${type} in ${loc}`);
    });
  });

  // Strategy 2: Intent + Property + Location (e.g., "Book Condo in Colon Panama")
  INTENTS.forEach(intent => {
    PROPERTY_TYPES.forEach(type => {
      LOCATIONS.forEach(loc => {
        // Limit total to avoid memory issues if arrays grow, but aim for >1000 combinations
        if (Math.random() > 0.5) { // Sampling to keep it diverse but manageable
             keywords.push(`${intent} ${type} ${loc}`);
        }
      });
    });
  });

  // Strategy 3: Property + Feature (e.g., "Beachfront Rental with Starlink WiFi")
  PROPERTY_TYPES.forEach(type => {
    FEATURES.forEach(feature => {
      keywords.push(`${type} ${feature}`);
      LOCATIONS.slice(0, 3).forEach(loc => {
         keywords.push(`${type} ${feature} ${loc}`);
      });
    });
  });

  // Strategy 4: Niche Long Tail (Specific from Report)
  const NICHE_PHRASES = [
    "safe vacation rentals colon panama",
    "fast internet beach rental panama",
    "digital nomad housing maria chiquita",
    "weekend getaway from panama city",
    "beach apartment near zona libre",
    "family vacation home caribbean panama"
  ];
  keywords = [...keywords, ...NICHE_PHRASES];

  return keywords;
};

// Export a curated list for the footer (approx 20-30 high value)
export const FOOTER_KEYWORDS = [
  "Maria Chiquita Beachfront Rentals",
  "Scuba Diving Portobelo Panama",
  "Colon Panama Vacation Homes",
  "Airbnb Alternative Maria Chiquita",
  "Best Scuba Diving Panama",
  "Luxury Beach Condo Panama",
  "Short Term Rental Colon",
  "Portobelo Accommodation",
  "Diving Panama Caribbean",
  "Bala Beach Resort Rentals",
  "Panama Caribbean Beach House",
  "Panama Dive Center Near Me",
  "Safe Lodging Colon Panama",
  "Apartment with Starlink Panama",
  "Vacation Rentals Near Free Zone",
  "Family Beach House Colon",
  "Romantic Getaway Panama Caribbean",
  "Direct Booking Beach Rental",
  "Ocean View Apartment Maria Chiquita"
];
