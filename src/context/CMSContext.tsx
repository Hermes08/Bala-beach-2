
import React, { createContext, useContext, useEffect, useState } from 'react';
import { BlogPost, ContentDictionary } from '../types';
import { BLOG_POSTS, CONTENT, IMAGES } from '../constants';
import { supabase } from '../lib/supabaseClient';

interface CMSContextType {
  blogPosts: BlogPost[];
  refreshBlog: () => Promise<void>;
  uploadImage: (file: File, bucket: string) => Promise<string | null>;
  addBlogPost: (post: BlogPost) => Promise<boolean>;
  deleteBlogPost: (id: string) => Promise<boolean>;
  isAuthenticated: boolean;
  login: (email: string) => void; // Simplified for demo, ideally use supabase.auth
  logout: () => void;
}

const CMSContext = createContext<CMSContextType | undefined>(undefined);

export const CMSProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  // Start with static data as fallback
  const [blogPosts, setBlogPosts] = useState<BlogPost[]>(BLOG_POSTS);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Check if we have Supabase connected (dummy check)
  const isSupabaseConfigured = !supabase.supabaseUrl.includes('tu-proyecto');

  const refreshBlog = async () => {
    if (!isSupabaseConfigured) return;

    const { data, error } = await supabase
      .from('blog_posts')
      .select('*')
      .order('date', { ascending: false });

    if (!error && data) {
      // Merge Supabase posts with static ones or replace them
      // For this demo, we'll map the DB structure to our TS structure
      const dbPosts: BlogPost[] = data.map(p => ({
        id: p.id,
        slug: p.slug,
        title: p.title, // Assuming JSONB in DB
        excerpt: p.excerpt, // Assuming JSONB in DB
        content: p.content, // Assuming JSONB in DB
        date: p.created_at, // simplified date
        image: p.image_url,
        category: p.category
      }));
      setBlogPosts([...dbPosts, ...BLOG_POSTS]); 
    }
  };

  useEffect(() => {
    refreshBlog();
    
    // Check local storage for simple auth persistence
    const auth = localStorage.getItem('cms_auth');
    if (auth === 'true') setIsAuthenticated(true);
  }, []);

  const uploadImage = async (file: File, bucket: 'blog-images' | 'gallery'): Promise<string | null> => {
    if (!isSupabaseConfigured) {
      alert("Supabase no está configurado. No se puede subir imagen.");
      return null;
    }

    const fileExt = file.name.split('.').pop();
    const fileName = `${Math.random()}.${fileExt}`;
    const filePath = `${fileName}`;

    const { error: uploadError } = await supabase.storage
      .from(bucket)
      .upload(filePath, file);

    if (uploadError) {
      console.error(uploadError);
      return null;
    }

    const { data } = supabase.storage.from(bucket).getPublicUrl(filePath);
    return data.publicUrl;
  };

  const addBlogPost = async (post: BlogPost): Promise<boolean> => {
    if (!isSupabaseConfigured) {
      // Local mock for demo
      setBlogPosts([post, ...blogPosts]);
      return true;
    }

    const { error } = await supabase
      .from('blog_posts')
      .insert([{
        slug: post.slug,
        title: post.title,
        excerpt: post.excerpt,
        content: post.content,
        image_url: post.image,
        category: post.category,
        created_at: new Date().toISOString()
      }]);

    if (!error) {
      await refreshBlog();
      return true;
    }
    return false;
  };

  const deleteBlogPost = async (id: string): Promise<boolean> => {
    if (!isSupabaseConfigured) {
      setBlogPosts(blogPosts.filter(p => p.id !== id));
      return true;
    }
    
    const { error } = await supabase.from('blog_posts').delete().eq('id', id);
    if (!error) {
      await refreshBlog();
      return true;
    }
    return false;
  };

  const login = (password: string) => {
    // Simple hardcoded protection for the frontend
    // In production, enable supabase.auth
    if (password === 'Panama2025!') {
      setIsAuthenticated(true);
      localStorage.setItem('cms_auth', 'true');
    } else {
      alert('Contraseña incorrecta');
    }
  };

  const logout = () => {
    setIsAuthenticated(false);
    localStorage.removeItem('cms_auth');
  };

  return (
    <CMSContext.Provider value={{ 
      blogPosts, 
      refreshBlog, 
      uploadImage, 
      addBlogPost, 
      deleteBlogPost,
      isAuthenticated,
      login,
      logout
    }}>
      {children}
    </CMSContext.Provider>
  );
};

export const useCMS = () => {
  const context = useContext(CMSContext);
  if (context === undefined) {
    throw new Error('useCMS must be used within a CMSProvider');
  }
  return context;
};
