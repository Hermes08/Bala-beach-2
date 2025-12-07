import React from 'react';
import { Helmet } from 'react-helmet-async';
import { useParams, Link, Navigate } from 'react-router-dom';
import { Language } from '../types';
import { BLOG_POSTS, CONTENT } from '../constants';
import { ArrowLeft, Calendar, User, Tag } from 'lucide-react';

interface Props {
  lang: Language;
}

const BlogPost: React.FC<Props> = ({ lang }) => {
  const { slug } = useParams<{ slug: string }>();
  const post = BLOG_POSTS.find(p => p.slug === slug);
  const t = CONTENT[lang];

  if (!post) {
    return <Navigate to="/blog" replace />;
  }

  return (
    <div className="pt-24 min-h-screen bg-white">
      <Helmet>
        <title>{post.title[lang]} | Maria Chiquita Rentals</title>
        <meta name="description" content={post.excerpt[lang]} />
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
          {post.title[lang]}
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
          <img src={post.image} alt={post.title[lang]} className="w-full h-auto object-cover max-h-[500px]" />
        </div>

        {/* Content Body */}
        <article className="prose prose-lg prose-slate max-w-none">
          {/* 
            In a real SSG/Headless setup, this would be a RichText renderer.
            For this simplified structure, we inject the string content.
          */}
          <p className="text-xl text-slate-600 leading-relaxed mb-6 font-medium">
            {post.excerpt[lang]}
          </p>
          <div className="text-slate-800 leading-8">
            {post.content[lang]}
            <p className="mt-4">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            </p>
            <h2 className="font-serif text-2xl font-bold mt-8 mb-4">Discovering the Coast</h2>
            <p>
              Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
              Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </p>
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