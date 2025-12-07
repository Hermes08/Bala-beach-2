
import React, { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import { Wifi, Wind, Utensils, MapPin, CheckCircle, ArrowRight, Plus, Minus, MessageCircle, Tv, Car, BedDouble, ChevronLeft, ChevronRight, Mail, Compass, Star } from 'lucide-react';
import { Link } from 'react-router-dom';
import { Language } from '../types';
import { CONTENT, BLOG_POSTS, IMAGES, CONTACT_INFO } from '../constants';
import AvailabilityCalendar from '../components/AvailabilityCalendar';

interface Props {
  lang: Language;
}

const FAQItem: React.FC<{ question: string; answer: string }> = ({ question, answer }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="border-b border-sand-200 last:border-0">
      <button 
        onClick={() => setIsOpen(!isOpen)}
        className="w-full py-5 flex justify-between items-center text-left focus:outline-none group"
      >
        <span className={`font-bold text-lg pr-4 transition-colors ${isOpen ? 'text-brand-600' : 'text-slate-800 group-hover:text-brand-600'}`}>
          {question}
        </span>
        <div className={`p-2 rounded-full transition-colors ${isOpen ? 'bg-brand-100 text-brand-600' : 'bg-sand-100 text-slate-500 group-hover:bg-brand-50 group-hover:text-brand-500'}`}>
          {isOpen ? <Minus size={20} /> : <Plus size={20} />}
        </div>
      </button>
      <div 
        className={`overflow-hidden transition-all duration-300 ease-in-out ${isOpen ? 'max-h-48 opacity-100 mb-6' : 'max-h-0 opacity-0'}`}
      >
        <p className="text-slate-600 leading-relaxed pl-2 border-l-2 border-brand-200">{answer}</p>
      </div>
    </div>
  );
};

const ReviewsSection: React.FC<Props> = ({ lang }) => {
  const t = CONTENT[lang].reviews;
  
  return (
    <section className="py-24 bg-white overflow-hidden">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <div className="flex justify-center gap-1 mb-4 text-amber-400">
            <Star fill="currentColor" size={24} />
            <Star fill="currentColor" size={24} />
            <Star fill="currentColor" size={24} />
            <Star fill="currentColor" size={24} />
            <Star fill="currentColor" size={24} />
          </div>
          <h2 className="font-serif text-3xl md:text-4xl font-bold text-slate-900 mb-4">{t.title}</h2>
          <p className="text-slate-600 text-lg">{t.subtitle}</p>
          <span className="inline-block mt-4 text-xs font-bold uppercase tracking-wider text-brand-500 bg-brand-50 px-3 py-1 rounded-full">{t.source}</span>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {t.items.map((review, idx) => (
            <div key={idx} className="bg-sand-100 p-6 rounded-2xl shadow-sm border border-sand-200 flex flex-col h-full hover:shadow-md transition-shadow">
              <div className="flex items-center gap-3 mb-4">
                <div className="w-10 h-10 rounded-full bg-brand-200 flex items-center justify-center font-bold text-brand-700">
                  {review.avatar}
                </div>
                <div>
                  <div className="font-bold text-slate-900">{review.author}</div>
                  <div className="text-xs text-slate-500">{review.location} • {review.date}</div>
                </div>
              </div>
              <p className="text-slate-700 text-sm leading-relaxed italic mb-4 flex-grow">"{review.text}"</p>
              <div className="flex text-amber-400 gap-0.5">
                {[...Array(review.rating)].map((_, i) => (
                  <Star key={i} size={14} fill="currentColor" />
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

const HeroCarousel: React.FC = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % IMAGES.heroSlides.length);
    }, 5000); // Change slide every 5 seconds
    return () => clearInterval(timer);
  }, []);

  const goToSlide = (index: number) => {
    setCurrentSlide(index);
  };

  return (
    <div className="absolute inset-0 z-0 bg-brand-900">
      {IMAGES.heroSlides.map((slide, index) => (
        <div
          key={index}
          className={`absolute inset-0 transition-opacity duration-1000 ease-in-out ${
            index === currentSlide ? 'opacity-100' : 'opacity-0'
          }`}
        >
          <img 
            src={slide} 
            alt={`Maria Chiquita Beachfront Rental - Ocean View Slide ${index + 1} - Colon Panama`} 
            className="w-full h-full object-cover"
          />
          {/* Enhanced gradient for better text visibility */}
          <div className="absolute inset-0 bg-gradient-to-t from-brand-900/90 via-brand-900/40 to-black/30" />
        </div>
      ))}
      
      {/* Carousel Indicators */}
      <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2 flex gap-3 z-20">
        {IMAGES.heroSlides.map((_, index) => (
          <button
            key={index}
            onClick={() => goToSlide(index)}
            className={`w-3 h-3 rounded-full transition-all duration-300 shadow-sm border border-white/30 ${
              index === currentSlide ? 'bg-brand-500 scale-125' : 'bg-white/60 hover:bg-white'
            }`}
            aria-label={`Go to slide ${index + 1}`}
          />
        ))}
      </div>
    </div>
  );
};

const HomePage: React.FC<Props> = ({ lang }) => {
  const t = CONTENT[lang];

  // Schema Markup for Vacation Rental
  const schemaMarkup = {
    "@context": "https://schema.org",
    "@type": "VacationRental",
    "name": "Maria Chiquita Beachfront Rentals",
    "headline": t.hero.title,
    "description": t.hero.subtitle,
    "image": [
      IMAGES.heroSlides[0],
      IMAGES.gallery[0]
    ],
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "María Chiquita",
      "addressRegion": "Colón",
      "addressCountry": "PA"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 9.44,
      "longitude": -79.75
    },
    "priceRange": "$120 - $200",
    "amenityFeature": [
      { "@type": "LocationFeatureSpecification", "name": "Ocean View", "value": "True" },
      { "@type": "LocationFeatureSpecification", "name": "WiFi Starlink", "value": "True" },
      { "@type": "LocationFeatureSpecification", "name": "Private Beach Access", "value": "True" }
    ],
    "starRating": {
      "@type": "Rating",
      "ratingValue": "4.9",
      "bestRating": "5"
    }
  };

  return (
    <>
      <Helmet>
        <title>{t.hero.title} | Beach Houses Panama</title>
        <meta name="description" content={`Maria Chiquita Beachfront Rental: ${t.hero.subtitle} Book direct for best rates on Colon Panama vacation rentals.`} />
        <meta name="keywords" content="maria chiquita, panama beach, beachfront house, colon panama, vacation rental, airbnb alternative, beach houses panama, short term rental colon" />
        <link rel="canonical" href="https://mariachiquitabeachrentals.com/" />
      </Helmet>
      
      <script type="application/ld+json">
        {JSON.stringify(schemaMarkup)}
      </script>

      {/* HERO SECTION */}
      <section className="relative h-screen min-h-[600px] flex items-center justify-center overflow-hidden">
        <HeroCarousel />

        <div className="relative z-10 max-w-5xl mx-auto px-4 text-center mt-20">
          <span className="inline-block px-4 py-1.5 bg-brand-500 text-white text-xs md:text-sm font-bold tracking-wider uppercase rounded-full mb-6 shadow-lg animate-in fade-in slide-in-from-bottom-4 duration-700">
            {t.hero.badge}
          </span>
          <h1 className="font-serif text-4xl md:text-6xl lg:text-7xl font-bold text-white mb-6 leading-tight drop-shadow-2xl animate-in fade-in slide-in-from-bottom-6 duration-1000">
            {t.hero.title}
          </h1>
          <p className="text-lg md:text-xl text-white/90 max-w-2xl mx-auto mb-10 leading-relaxed font-light drop-shadow-md animate-in fade-in slide-in-from-bottom-8 duration-1000 delay-100">
            {t.hero.subtitle}
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center animate-in fade-in slide-in-from-bottom-10 duration-1000 delay-200">
            <a 
              href={`https://wa.me/${CONTACT_INFO.whatsappNumber}?text=${encodeURIComponent(CONTACT_INFO.bookingMessage)}`}
              target="_blank"
              rel="noopener noreferrer"
              className="w-full sm:w-auto px-8 py-4 bg-brand-500 hover:bg-brand-400 text-white font-bold rounded-lg shadow-xl hover:shadow-2xl hover:-translate-y-1 transition-all text-lg flex items-center justify-center gap-2"
            >
              <MessageCircle size={20} /> {t.hero.cta}
            </a>
            <a
               href="https://www.airbnb.com/rooms/1409650618945019706" 
               target="_blank"
               rel="noopener noreferrer" 
               className="w-full sm:w-auto px-8 py-4 bg-white/10 hover:bg-white/20 text-white font-medium rounded-lg backdrop-blur-md transition-all flex items-center justify-center border border-white/30 hover:border-white/50"
            >
              Airbnb Listing
            </a>
          </div>
          <div className="mt-8 inline-block animate-in fade-in zoom-in duration-1000 delay-300">
             <span className="text-white/90 text-sm font-bold bg-black/40 px-6 py-2 rounded-full backdrop-blur-md border border-white/10">
               {t.hero.price}
             </span>
          </div>
        </div>
      </section>

      {/* AMENITIES SECTION */}
      <section id="amenities" className="py-24 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="font-serif text-3xl md:text-4xl font-bold text-slate-900 mb-4">{t.features.title}</h2>
            <p className="text-slate-600 max-w-2xl mx-auto text-lg">{t.features.subtitle}</p>
          </div>

          <div className="grid grid-cols-2 md:grid-cols-3 gap-6 md:gap-8">
            {[
              { icon: Wifi, title: t.features.list.wifi, desc: "100Mbps+" },
              { icon: Wind, title: t.features.list.ac, desc: "Cool & Quiet" },
              { icon: Utensils, title: t.features.list.kitchen, desc: "Fully Equipped" },
              { icon: Tv, title: t.features.list.tv, desc: "Netflix/Prime" },
              { icon: Car, title: t.features.list.parking, desc: "Secure Spot" },
              { icon: BedDouble, title: t.features.list.bedding, desc: "Hotel Quality" },
            ].map((item, idx) => (
              <div key={idx} className="p-8 bg-sand-100/50 rounded-2xl hover:bg-white hover:shadow-xl transition-all duration-300 border border-sand-200 group text-center">
                <div className="w-14 h-14 bg-white text-brand-600 rounded-full flex items-center justify-center mb-6 mx-auto shadow-sm group-hover:bg-brand-500 group-hover:text-white transition-colors">
                  <item.icon size={28} />
                </div>
                <h3 className="font-bold text-lg mb-2 text-slate-800">{item.title}</h3>
                <p className="text-sm text-slate-500">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* GALLERY SECTION */}
      <section className="py-24 bg-sand-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="font-serif text-3xl md:text-4xl font-bold text-slate-900 mb-4">{t.gallery.title}</h2>
            <p className="text-slate-600 max-w-2xl mx-auto text-lg">{t.gallery.subtitle}</p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
             {IMAGES.gallery.map((imgSrc, index) => (
               <div key={index} className="group relative overflow-hidden rounded-2xl shadow-lg aspect-[4/3] cursor-pointer">
                 <img 
                   src={imgSrc} 
                   alt={`Maria Chiquita Vacation Rental Gallery - Image ${index + 1} - Beach Apartment Colon Panama`} 
                   className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" 
                 />
                 <div className="absolute inset-0 bg-black/20 group-hover:bg-black/0 transition-colors duration-500"></div>
                 <div className="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/80 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <span className="text-white font-medium tracking-wide">View Full Size</span>
                 </div>
               </div>
             ))}
          </div>
        </div>
      </section>

      {/* SEO / VALUE PROP SECTION */}
      <section className="py-24 bg-brand-900 text-white overflow-hidden relative">
        <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-brand-500 rounded-full blur-3xl opacity-20"></div>
        <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-96 h-96 bg-brand-600 rounded-full blur-3xl opacity-20"></div>
        
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
          <div className="grid md:grid-cols-2 gap-16 items-center">
            <div>
              <h2 className="font-serif text-3xl md:text-4xl font-bold mb-6 leading-tight">
                {t.seoSection.title}
              </h2>
              <div className="prose prose-lg prose-invert text-brand-100 mb-10">
                <p className="mb-6 leading-relaxed">
                  {t.seoSection.p1}
                </p>
                <p className="leading-relaxed">
                  {t.seoSection.p2}
                </p>
              </div>
              
              <div className="bg-white/5 rounded-2xl p-8 backdrop-blur-md border border-white/10 shadow-2xl">
                <h3 className="font-bold text-xl mb-6 text-white border-b border-white/10 pb-4">{t.comparison.title}</h3>
                <ul className="space-y-4">
                  <li className="flex items-start gap-3 text-brand-50">
                    <CheckCircle className="text-brand-400 shrink-0 mt-1" size={20} />
                    <span>{t.comparison.benefit1}</span>
                  </li>
                  <li className="flex items-start gap-3 text-brand-50">
                    <CheckCircle className="text-brand-400 shrink-0 mt-1" size={20} />
                    <span>{t.comparison.benefit2}</span>
                  </li>
                  <li className="flex items-start gap-3 text-brand-50">
                    <CheckCircle className="text-brand-400 shrink-0 mt-1" size={20} />
                    <span>{t.comparison.benefit3}</span>
                  </li>
                </ul>
              </div>
            </div>
            <div className="relative hidden md:block">
               <div className="grid grid-cols-2 gap-6">
                  <img src={IMAGES.seo.beach} alt="Beachfront details Panama - Maria Chiquita Beach" className="rounded-2xl shadow-2xl translate-y-12 object-cover h-[500px] w-full" />
                  <img src={IMAGES.seo.interior} alt="Luxury apartment Maria Chiquita - Living Room Interior" className="rounded-2xl shadow-2xl -translate-y-12 object-cover h-[500px] w-full" />
               </div>
            </div>
          </div>
        </div>
      </section>

      {/* LOCATION PREVIEW */}
      <section id="location" className="py-24 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-2 gap-12 items-center mb-16">
            <div className="h-[450px] bg-slate-200 rounded-3xl overflow-hidden shadow-2xl relative group transform hover:scale-[1.01] transition-transform duration-500">
               <img src={IMAGES.locationMap} alt="Map Location Colon Panama - Maria Chiquita Area" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
               <div className="absolute inset-0 flex items-center justify-center bg-black/10 group-hover:bg-black/20 transition-colors">
                  <div className="bg-white px-8 py-4 rounded-full shadow-2xl flex items-center gap-3 font-bold text-brand-900 text-lg">
                    <MapPin className="text-red-500 fill-red-500/20" /> María Chiquita, Colón
                  </div>
               </div>
            </div>
            <div className="pl-0 md:pl-10">
              <span className="text-brand-600 font-bold tracking-wider uppercase text-sm mb-3 block">The Location</span>
              <h2 className="font-serif text-3xl md:text-5xl font-bold text-slate-900 mb-6 leading-tight">Discover Colón's Caribbean Jewel</h2>
              <p className="text-slate-600 mb-8 text-lg leading-relaxed">
                Away from the crowds, María Chiquita offers a pristine beach experience. Located just 1 hour from Panama City and minutes from the historic Portobelo ruins.
              </p>
              <div className="grid grid-cols-3 gap-4">
                <div className="bg-sand-100 p-4 rounded-xl shadow-sm border border-sand-200 text-center hover:bg-white hover:shadow-md transition-all">
                  <span className="block text-3xl font-bold text-brand-600 mb-1">20m</span>
                  <span className="text-xs font-bold text-slate-400 uppercase tracking-wide">To Beach</span>
                </div>
                <div className="bg-sand-100 p-4 rounded-xl shadow-sm border border-sand-200 text-center hover:bg-white hover:shadow-md transition-all">
                  <span className="block text-3xl font-bold text-brand-600 mb-1">15m</span>
                  <span className="text-xs font-bold text-slate-400 uppercase tracking-wide">Portobelo</span>
                </div>
                <div className="bg-sand-100 p-4 rounded-xl shadow-sm border border-sand-200 text-center hover:bg-white hover:shadow-md transition-all">
                  <span className="block text-3xl font-bold text-brand-600 mb-1">60m</span>
                  <span className="text-xs font-bold text-slate-400 uppercase tracking-wide">Panama City</span>
                </div>
              </div>
            </div>
          </div>

          {/* Interactive Map Embed */}
          <div className="w-full h-[400px] rounded-2xl overflow-hidden shadow-lg border border-sand-200">
            <iframe 
              src="https://maps.google.com/maps?q=Maria+Chiquita,+Colon,+Panama&t=&z=14&ie=UTF8&iwloc=&output=embed"
              width="100%" 
              height="100%" 
              style={{ border: 0 }} 
              allowFullScreen={true} 
              loading="lazy" 
              title="Google Maps Location Maria Chiquita"
            ></iframe>
          </div>
        </div>
      </section>

      {/* TOURS & EXPERIENCES SECTION */}
      <section className="py-24 bg-sand-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <span className="text-brand-600 font-bold tracking-wider uppercase text-sm mb-3 block">Local Guide</span>
            <h2 className="font-serif text-3xl md:text-4xl font-bold text-slate-900 mb-4">{t.tours.title}</h2>
            <p className="text-slate-600 max-w-2xl mx-auto text-lg">{t.tours.subtitle}</p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {t.tours.items.map((tour, idx) => (
              <div key={idx} className="group bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2">
                <div className="h-48 overflow-hidden relative">
                  <img src={tour.image} alt={tour.title} className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-60"></div>
                  <div className="absolute bottom-4 left-4 text-white font-bold flex items-center gap-2">
                    <Compass size={18} /> Experience
                  </div>
                </div>
                <div className="p-6">
                  <h3 className="font-serif text-xl font-bold text-slate-900 mb-2 group-hover:text-brand-600 transition-colors">{tour.title}</h3>
                  <p className="text-slate-600 text-sm leading-relaxed">{tour.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* REVIEWS SECTION */}
      <ReviewsSection lang={lang} />

      {/* AVAILABILITY CALENDAR SECTION */}
      <section className="py-24 bg-sand-100 border-t border-slate-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <AvailabilityCalendar lang={lang} />
        </div>
      </section>

      {/* FAQ SECTION */}
      <section className="py-24 bg-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
           <div className="text-center mb-16">
            <h2 className="font-serif text-3xl md:text-4xl font-bold text-slate-900 mb-4">{t.faq.title}</h2>
            <p className="text-slate-600 text-lg">{t.faq.subtitle}</p>
          </div>
          <div className="bg-sand-100 rounded-3xl shadow-xl border border-sand-200 overflow-hidden p-6 md:p-10">
            {t.faq.items.map((item, index) => (
              <FAQItem key={index} question={item.question} answer={item.answer} />
            ))}
          </div>
        </div>
      </section>

      {/* NEWSLETTER SECTION */}
      <section className="py-20 bg-brand-900 text-white relative overflow-hidden">
        {/* Decorative elements */}
        <div className="absolute left-0 top-0 w-full h-full opacity-10 pointer-events-none">
           <div className="absolute right-10 top-10 w-64 h-64 bg-brand-400 rounded-full blur-3xl"></div>
           <div className="absolute left-10 bottom-10 w-64 h-64 bg-brand-600 rounded-full blur-3xl"></div>
        </div>

        <div className="max-w-4xl mx-auto px-4 relative z-10 text-center">
          <div className="w-16 h-16 bg-white/10 rounded-full flex items-center justify-center mx-auto mb-6 backdrop-blur-md border border-white/20">
            <Mail size={32} className="text-brand-100" />
          </div>
          <h2 className="font-serif text-3xl md:text-4xl font-bold mb-4">{t.newsletter.title}</h2>
          <p className="text-brand-100 text-lg mb-8 max-w-xl mx-auto">{t.newsletter.subtitle}</p>
          
          <form className="max-w-md mx-auto flex flex-col sm:flex-row gap-4" onSubmit={(e) => e.preventDefault()}>
            <input 
              type="email" 
              placeholder={t.newsletter.placeholder} 
              className="flex-grow px-6 py-4 rounded-full bg-white/10 border border-white/20 text-white placeholder-brand-200/70 focus:outline-none focus:ring-2 focus:ring-brand-400 backdrop-blur-sm transition-all"
              required
            />
            <button 
              type="submit" 
              className="px-8 py-4 bg-white text-brand-900 font-bold rounded-full hover:bg-brand-50 transition-colors shadow-lg hover:shadow-xl"
            >
              {t.newsletter.button}
            </button>
          </form>
          <p className="text-brand-300/60 text-xs mt-4">{t.newsletter.disclaimer}</p>
        </div>
      </section>

      {/* BLOG PREVIEW */}
      <section className="py-24 bg-sand-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-end mb-12">
            <div>
              <h2 className="font-serif text-3xl md:text-4xl font-bold text-slate-900 mb-2">{t.nav.blog}</h2>
              <p className="text-slate-500 text-lg">Expert tips for your Panama vacation.</p>
            </div>
            <Link to="/blog" className="text-brand-600 font-bold hover:text-brand-700 flex items-center gap-2 group text-lg">
              View All <ArrowRight size={20} className="group-hover:translate-x-1 transition-transform" />
            </Link>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-10">
            {BLOG_POSTS.slice(0, 3).map((post) => (
              <Link key={post.id} to={`/blog/${post.slug}`} className="group block h-full">
                <div className="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-2xl transition-all duration-300 border border-slate-100 h-full flex flex-col transform group-hover:-translate-y-1">
                  <div className="h-56 overflow-hidden relative">
                    <img src={post.image} alt={post.title[lang]} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                    <div className="absolute top-4 left-4">
                       <span className="bg-white/90 backdrop-blur-sm text-brand-700 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wide shadow-sm">
                        {post.category}
                      </span>
                    </div>
                  </div>
                  <div className="p-8 flex-grow flex flex-col">
                    <h3 className="font-serif text-2xl font-bold text-slate-900 mb-3 group-hover:text-brand-600 transition-colors leading-tight">
                      {post.title[lang]}
                    </h3>
                    <p className="text-slate-600 mb-6 line-clamp-3 flex-grow leading-relaxed">
                      {post.excerpt[lang]}
                    </p>
                    <div className="flex items-center justify-between pt-4 border-t border-slate-50">
                      <span className="text-sm font-medium text-slate-400">{post.date}</span>
                      <span className="text-brand-600 text-sm font-bold flex items-center gap-1 group-hover:gap-2 transition-all">
                        Read Article <ArrowRight size={14} />
                      </span>
                    </div>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>
    </>
  );
};

export default HomePage;