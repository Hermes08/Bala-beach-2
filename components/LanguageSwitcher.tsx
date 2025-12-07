import React from 'react';
import { Language } from '../types';

interface Props {
  currentLang: Language;
  onLanguageChange: (lang: Language) => void;
}

const LanguageSwitcher: React.FC<Props> = ({ currentLang, onLanguageChange }) => {
  return (
    <div className="flex items-center gap-2 bg-white/10 backdrop-blur-sm rounded-full p-1 border border-white/20">
      {(['en', 'es', 'de'] as Language[]).map((lang) => (
        <button
          key={lang}
          onClick={() => onLanguageChange(lang)}
          className={`
            w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold transition-all
            ${currentLang === lang 
              ? 'bg-white text-brand-900 shadow-md transform scale-105' 
              : 'text-white hover:bg-white/20'}
          `}
          aria-label={`Switch to ${lang.toUpperCase()}`}
        >
          {lang.toUpperCase()}
        </button>
      ))}
    </div>
  );
};

export default LanguageSwitcher;