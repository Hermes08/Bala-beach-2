import React from 'react';
import { Helmet } from 'react-helmet-async';
import { Link } from 'react-router-dom';
import { Language } from '../types';
import { CONTENT, BLOG_POSTS } from '../constants';
import { ArrowRight } from 'lucide-react';

interface Props {
  lang: Language;
}

const BlogPage: React.FC<Props> = ({ lang }) => {
  const t = CONTENT[lang];

  return (
    <div className="pt-24 min-h-screen bg-sand-100">
      <Helmet>
        <title>{t.nav.blog} | Maria Chiquita Rentals</title>
        <meta name="description" content={`Read our guides about Colon, Panama, Beachfront rentals, and things to do in Maria Chiquita.`} />
      </Helmet>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="text-center mb-16">
          <h1 className="font-serif text-4xl md:text-5xl font-bold text-slate-900 mb-6">{t.nav.blog}</h1>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            Discover local secrets, travel tips, and reasons why booking a private rental is better than a hotel in Colón.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-10">
          {BLOG_POSTS.map((post) => (
            <article key={post.id} className="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-shadow duration-300 flex flex-col">
              <Link to={`/blog/${post.slug}`} className="block h-56 overflow-hidden">
                <img 
                  src={post.image} 
                  alt={post.title[lang]} 
                  className="w-full h-full object-cover hover:scale-105 transition-transform duration-500" 
                />
              </Link>
              <div className="p-8 flex flex-col flex-grow">
                <div className="flex items-center justify-between mb-4">
                  <span className="bg-brand-100 text-brand-700 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wide">
                    {post.category}
                  </span>
                  <span className="text-slate-400 text-sm">{post.date}</span>
                </div>
                <h2 className="font-serif text-2xl font-bold text-slate-900 mb-4 hover:text-brand-600 transition-colors">
                  <Link to={`/blog/${post.slug}`}>
                    {post.title[lang]}
                  </Link>
                </h2>
                <p className="text-slate-600 mb-6 leading-relaxed flex-grow">
                  {post.excerpt[lang]}
                </p>
                <Link 
                  to={`/blog/${post.slug}`} 
                  className="inline-flex items-center gap-2 text-brand-600 font-bold hover:gap-3 transition-all"
                >
                  Read Article <ArrowRight size={16} />
                </Link>
              </div>
            </article>
          ))}
        </div>
      </div>
    </div>
  );
};

export default BlogPage;