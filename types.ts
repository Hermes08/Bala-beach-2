
export type Language = 'es' | 'en' | 'de';

export interface BlogPost {
  id: string;
  slug: string;
  title: Record<Language, string>;
  excerpt: Record<Language, string>;
  content: Record<Language, string>;
  date: string;
  image: string;
  category: string;
}

export interface SEOMetadata {
  title: string;
  description: string;
  keywords: string;
}

export interface FAQItem {
  question: string;
  answer: string;
}

export interface TourItem {
  title: string;
  desc: string;
  image: string;
}

export interface ReviewItem {
  author: string;
  location: string;
  date: string;
  rating: number;
  text: string;
  avatar: string; // url or initial
}

export interface ContentDictionary {
  nav: {
    home: string;
    amenities: string;
    location: string;
    blog: string;
    bookNow: string;
  };
  hero: {
    badge: string;
    title: string;
    subtitle: string;
    cta: string;
    price: string;
  };
  features: {
    title: string;
    subtitle: string;
    list: {
      wifi: string;
      ac: string;
      kitchen: string;
      tv: string;
      parking: string;
      bedding: string;
    };
  };
  gallery: {
    title: string;
    subtitle: string;
  };
  tours: {
    title: string;
    subtitle: string;
    items: TourItem[];
  };
  calendar: {
    title: string;
    subtitle: string;
    available: string;
    booked: string;
    checkButton: string;
    error: string;
  };
  reviews: {
    title: string;
    subtitle: string;
    source: string;
    items: ReviewItem[];
  };
  seoSection: {
    title: string;
    p1: string;
    p2: string;
  };
  comparison: {
    title: string;
    direct: string;
    airbnb: string;
    benefit1: string;
    benefit2: string;
    benefit3: string;
  };
  faq: {
    title: string;
    subtitle: string;
    items: FAQItem[];
  };
  newsletter: {
    title: string;
    subtitle: string;
    placeholder: string;
    button: string;
    disclaimer: string;
  };
  footer: {
    about: string;
    contact: string;
    rights: string;
  };
}
