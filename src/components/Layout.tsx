
import React, { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import { Link, useLocation } from 'react-router-dom';
import { Menu, X, Phone, Mail, Instagram, MapPin, Lock } from 'lucide-react';
import LanguageSwitcher from './LanguageSwitcher';
import { Language } from '../types';
import { CONTENT, SEO_KEYWORDS_LIST, CONTACT_INFO } from '../constants';

interface LayoutProps {
  children: React.ReactNode;
  lang: Language;
  setLang: (lang: Language) => void;
}

const Layout: React.FC<LayoutProps> = ({ children, lang, setLang }) => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const location = useLocation();
  const t = CONTENT[lang];

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    window.scrollTo(0, 0);
    setIsMobileMenuOpen(false);
  }, [location.pathname]);

  return (
    <div className="min-h-screen flex flex-col font-sans text-slate-800 bg-sand-100">
      <Helmet>
        <html lang={lang} />
        <meta name="robots" content="index, follow" />
        <link rel="canonical" href={`https://mariachiquitabeachrentals.com${location.pathname}`} />
      </Helmet>

      {/* Navigation */}
      <nav 
        className={`fixed w-full z-50 transition-all duration-300 ${
          isScrolled ? 'bg-white/95 backdrop-blur-md shadow-sm py-3' : 'bg-transparent py-5'
        }`}
      >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center">
            {/* Logo */}
            <Link to="/" className="z-50 focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 rounded-lg p-1">
              <span className={`font-serif text-xl md:text-2xl font-bold tracking-tight ${
                isScrolled ? 'text-brand-900' : 'text-white'
              }`}>
                Maria Chiquita<span className="text-brand-500">.Rentals</span>
              </span>
            </Link>

            {/* Desktop Nav */}
            <div className="hidden md:flex items-center gap-8">
              <div className={`flex gap-6 text-sm font-medium ${isScrolled ? 'text-slate-600' : 'text-white/90'}`}>
                <Link to="/" className="hover:text-brand-500 transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 rounded px-2 py-1">{t.nav.home}</Link>
                <a href="/#amenities" className="hover:text-brand-500 transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 rounded px-2 py-1">{t.nav.amenities}</a>
                <a href="/#location" className="hover:text-brand-500 transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 rounded px-2 py-1">{t.nav.location}</a>
                <Link to="/blog" className="hover:text-brand-500 transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 rounded px-2 py-1">{t.nav.blog}</Link>
              </div>
              
              <div className="flex items-center gap-4">
                <LanguageSwitcher currentLang={lang} onLanguageChange={setLang} />
                <a 
                  href="https://www.airbnb.com/rooms/1409650618945019706" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="bg-brand-500 hover:bg-brand-600 hover:scale-105 active:scale-95 text-white px-5 py-2.5 rounded-full font-semibold text-sm transition-all shadow-lg hover:shadow-brand-500/30 focus:outline-none focus:ring-2 focus:ring-brand-400 focus:ring-offset-2"
                >
                  {t.nav.bookNow}
                </a>
              </div>
            </div>

            {/* Mobile Menu Button */}
            <div className="flex md:hidden items-center gap-4">
              <LanguageSwitcher currentLang={lang} onLanguageChange={setLang} />
              <button 
                onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
                className={`p-2 rounded-lg ${isScrolled ? 'text-slate-800' : 'text-white'} focus:outline-none focus:ring-2 focus:ring-brand-500`}
                aria-expanded={isMobileMenuOpen}
                aria-controls="mobile-menu"
                aria-label="Toggle navigation menu"
              >
                {isMobileMenuOpen ? <X /> : <Menu />}
              </button>
            </div>
          </div>
        </div>

        {/* Mobile Nav Overlay */}
        {isMobileMenuOpen && (
          <div id="mobile-menu" className="absolute top-full left-0 w-full bg-white shadow-xl border-t p-4 flex flex-col gap-4 md:hidden animate-in slide-in-from-top-5">
            <Link to="/" className="text-lg font-medium text-slate-800 p-2">{t.nav.home}</Link>
            <a href="/#amenities" className="text-lg font-medium text-slate-800 p-2">{t.nav.amenities}</a>
            <a href="/#location" className="text-lg font-medium text-slate-800 p-2">{t.nav.location}</a>
            <Link to="/blog" className="text-lg font-medium text-slate-800 p-2">{t.nav.blog}</Link>
            <a 
              href="https://www.airbnb.com/rooms/1409650618945019706" 
              className="bg-brand-500 text-white text-center py-3 rounded-lg font-bold hover:bg-brand-600 transition-colors"
            >
              {t.nav.bookNow}
            </a>
          </div>
        )}
      </nav>

      {/* Main Content */}
      <main className="flex-grow pt-0">
        {children}
      </main>

      {/* Footer */}
      <footer className="bg-brand-900 text-white py-16 border-t border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
            <div className="col-span-1 md:col-span-2">
              <h3 className="font-serif text-2xl font-bold mb-4">Maria Chiquita<span className="text-brand-500">.Rentals</span></h3>
              <p className="text-brand-100 max-w-sm mb-6 leading-relaxed">
                {t.footer.about}
              </p>
              <div className="flex gap-4">
                <a href="#" aria-label="Instagram" className="p-2 bg-white/10 rounded-full hover:bg-brand-500 transition-colors focus:outline-none focus:ring-2 focus:ring-white"><Instagram size={20} /></a>
                <a href="#" aria-label="Email Us" className="p-2 bg-white/10 rounded-full hover:bg-brand-500 transition-colors focus:outline-none focus:ring-2 focus:ring-white"><Mail size={20} /></a>
              </div>
            </div>
            
            <div>
              <h4 className="text-lg font-semibold mb-4 text-brand-50">{t.nav.location}</h4>
              <ul className="space-y-2 text-brand-100 text-sm">
                <li className="flex items-center gap-2"><MapPin size={14} className="text-brand-500" /> María Chiquita, Colón</li>
                <li>Panama Caribbean Coast</li>
                <li>Near Portobelo National Park</li>
                <li className="pt-2"><a href="/#location" className="text-brand-400 hover:text-white transition-colors underline-offset-4 hover:underline">View on Map →</a></li>
              </ul>
            </div>

            <div>
              <h4 className="text-lg font-semibold mb-4 text-brand-50">{t.footer.contact}</h4>
              <ul className="space-y-3 text-brand-100 text-sm">
                <li className="flex items-center gap-2"><Phone size={16} /> {CONTACT_INFO.displayPhone}</li>
                <li className="flex items-center gap-2"><Mail size={16} /> bookings@mariachiquita.rentals</li>
              </ul>
            </div>
          </div>

          {/* Popular Searches / SEO Keywords - IMPROVED CONTRAST */}
          <div className="border-t border-white/10 pt-8 mb-8">
            <h5 className="text-sm font-bold text-brand-500 uppercase tracking-wider mb-4">Popular Searches & Destinations</h5>
            <div className="flex flex-wrap gap-x-4 gap-y-2">
              {SEO_KEYWORDS_LIST.map((keyword, index) => (
                <span key={index} className="text-xs text-brand-100 hover:text-white cursor-pointer transition-colors">
                  {keyword} {index < SEO_KEYWORDS_LIST.length - 1 && "•"}
                </span>
              ))}
            </div>
          </div>

          <div className="pt-8 border-t border-white/10 text-center text-brand-200 text-sm flex flex-col md:flex-row justify-between items-center gap-4">
            <p>&copy; {new Date().getFullYear()} Maria Chiquita Beachfront Rentals. {t.footer.rights}</p>
            <div className="flex items-center gap-4">
              {/* IMPROVED CONTRAST FOR ADMIN LINK */}
              <Link to="/admin" className="flex items-center gap-1 text-xs text-brand-200 hover:text-white transition-all focus:outline-none focus:underline">
                <Lock size={10} /> Admin Login
              </Link>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Layout;
