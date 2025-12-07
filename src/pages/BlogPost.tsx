
import React from 'react';
import { Helmet } from 'react-helmet-async';
import { useParams, Link, Navigate } from 'react-router-dom';
import { Language } from '../types';
import { CONTENT } from '../constants';
import { useCMS } from '../context/CMSContext';
import { ArrowLeft, Calendar, User, Tag } from 'lucide-react';

interface Props {
  lang: Language;
}

const BlogPost: React.FC<Props> = ({ lang }) => {
  const { slug } = useParams<{ slug: string }>();
  const { blogPosts } = useCMS();
  const post = blogPosts.find(p => p.slug === slug);
  const t = CONTENT[lang];

  if (!post) {
    return <Navigate to="/blog" replace />;
  }

  // Fallback if translation is missing
  const title = post.title[lang] || post.title.en;
  const excerpt = post.excerpt[lang] || post.excerpt.en;
  const content = post.content[lang] || post.content.en;

  return (
    <div className="pt-24 min-h-screen bg-white">
      <Helmet>
        <title>{title} | Maria Chiquita Rentals</title>
        <meta name="description" content={excerpt} />
      </Helmet>

      {/* Article Header */}
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <Link to="/blog" className="inline-flex items-center gap-2 text-slate-500 hover:text-brand-600 font-medium mb-8 transition-colors">
          <ArrowLeft size={16} /> Back to Blog
        </Link>
        
        <span className="text-brand-600 font-bold tracking-wider uppercase text-sm block mb-4">
          {post.category}
        </span>
        
        <h1 className="font-serif text-3xl md:text-5xl font-bold text-slate-900 mb-8 leading-tight">
          {title}
        </h1>

        <div className="flex items-center gap-6 text-slate-500 text-sm border-b border-slate-100 pb-8 mb-8">
          <div className="flex items-center gap-2">
            <Calendar size={16} />
            {post.date}
          </div>
          <div className="flex items-center gap-2">
            <User size={16} />
            Maria Chiquita Host
          </div>
        </div>

        {/* Featured Image */}
        <div className="rounded-2xl overflow-hidden shadow-lg mb-12">
          <img src={post.image} alt={title} className="w-full h-auto object-cover max-h-[500px]" />
        </div>

        {/* Content Body */}
        <article className="prose prose-lg prose-slate max-w-none">
          <p className="text-xl text-slate-600 leading-relaxed mb-6 font-medium">
            {excerpt}
          </p>
          <div className="text-slate-800 leading-8 whitespace-pre-wrap">
            {content}
          </div>
        </article>

        {/* CTA Box */}
        <div className="bg-brand-50 rounded-xl p-8 mt-16 border border-brand-100 text-center">
          <h3 className="font-serif text-2xl font-bold text-brand-900 mb-4">Ready to experience this yourself?</h3>
          <p className="text-brand-700 mb-6">Book your beachfront stay in Maria Chiquita today and skip the Airbnb service fees.</p>
          <a 
            href="https://www.airbnb.com/rooms/1409650618945019706" 
            className="inline-block bg-brand-600 text-white font-bold py-3 px-8 rounded-full shadow-lg hover:shadow-xl hover:bg-brand-500 transition-all"
          >
            {t.nav.bookNow}
          </a>
        </div>
      </div>
    </div>
  );
};

export default BlogPost;
