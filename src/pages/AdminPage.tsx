
import React, { useState } from 'react';
import { useCMS } from '../context/CMSContext';
import { BlogPost, Language } from '../types';
import { Upload, Trash2, Plus, LogOut, Image as ImageIcon } from 'lucide-react';
import { Link } from 'react-router-dom';

const AdminPage: React.FC = () => {
  const { isAuthenticated, login, logout, blogPosts, addBlogPost, deleteBlogPost, uploadImage } = useCMS();
  const [password, setPassword] = useState('');
  
  // Form State
  const [activeTab, setActiveTab] = useState<'list' | 'create'>('list');
  const [newPost, setNewPost] = useState<Partial<BlogPost>>({
    title: { es: '', en: '', de: '' },
    excerpt: { es: '', en: '', de: '' },
    content: { es: '', en: '', de: '' },
    category: 'Travel Guide',
    image: ''
  });
  const [uploading, setUploading] = useState(false);

  if (!isAuthenticated) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-sand-100">
        <div className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-md">
          <h1 className="font-serif text-2xl font-bold text-center mb-6 text-brand-900">Admin Login</h1>
          <p className="text-sm text-center text-slate-500 mb-6">Enter password to manage content</p>
          <input 
            type="password" 
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full px-4 py-3 rounded-lg border border-slate-300 mb-4"
            placeholder="Password"
          />
          <button 
            onClick={() => login(password)}
            className="w-full bg-brand-600 text-white font-bold py-3 rounded-lg hover:bg-brand-700 transition-colors"
          >
            Access CMS
          </button>
        </div>
      </div>
    );
  }

  const handleImageUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files || e.target.files.length === 0) return;
    setUploading(true);
    const file = e.target.files[0];
    const url = await uploadImage(file, 'blog-images');
    if (url) {
      setNewPost({ ...newPost, image: url });
    }
    setUploading(false);
  };

  const handleSubmit = async () => {
    if (!newPost.title?.es || !newPost.slug) {
      alert("Please fill at least the Slug and Spanish Title");
      return;
    }

    const post: BlogPost = {
      id: Date.now().toString(), // temporary ID
      slug: newPost.slug || '',
      title: newPost.title as Record<Language, string>,
      excerpt: newPost.excerpt as Record<Language, string>,
      content: newPost.content as Record<Language, string>,
      date: new Date().toLocaleDateString(),
      image: newPost.image || 'https://via.placeholder.com/800x600',
      category: newPost.category || 'Updates'
    };

    const success = await addBlogPost(post);
    if (success) {
      alert("Post created!");
      setActiveTab('list');
    }
  };

  return (
    <div className="min-h-screen bg-slate-50">
      <nav className="bg-brand-900 text-white px-8 py-4 flex justify-between items-center">
        <span className="font-bold text-xl">Maria Chiquita CMS</span>
        <div className="flex gap-4">
          <Link to="/" className="text-sm hover:text-brand-200 py-2">View Site</Link>
          <button onClick={logout} className="flex items-center gap-2 bg-red-500/20 hover:bg-red-500/40 px-4 py-2 rounded-lg transition-colors">
            <LogOut size={16} /> Logout
          </button>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-4 py-8">
        <div className="flex gap-4 mb-8">
          <button 
            onClick={() => setActiveTab('list')}
            className={`px-6 py-2 rounded-lg font-bold ${activeTab === 'list' ? 'bg-brand-600 text-white' : 'bg-white text-slate-600'}`}
          >
            All Posts
          </button>
          <button 
            onClick={() => setActiveTab('create')}
            className={`px-6 py-2 rounded-lg font-bold ${activeTab === 'create' ? 'bg-brand-600 text-white' : 'bg-white text-slate-600'}`}
          >
            Create New Post
          </button>
        </div>

        {activeTab === 'list' && (
          <div className="bg-white rounded-xl shadow-sm overflow-hidden">
            <table className="w-full text-left">
              <thead className="bg-slate-100 text-slate-500 uppercase text-xs font-bold">
                <tr>
                  <th className="px-6 py-4">Image</th>
                  <th className="px-6 py-4">Title (ES)</th>
                  <th className="px-6 py-4">Date</th>
                  <th className="px-6 py-4">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {blogPosts.map(post => (
                  <tr key={post.id} className="hover:bg-slate-50">
                    <td className="px-6 py-4">
                      <img src={post.image} alt="" className="w-12 h-12 rounded object-cover" />
                    </td>
                    <td className="px-6 py-4 font-medium text-slate-900">{post.title.es}</td>
                    <td className="px-6 py-4 text-slate-500">{post.date}</td>
                    <td className="px-6 py-4">
                      <button 
                        onClick={() => deleteBlogPost(post.id)}
                        className="text-red-500 hover:text-red-700 p-2 hover:bg-red-50 rounded-full"
                      >
                        <Trash2 size={18} />
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {activeTab === 'create' && (
          <div className="bg-white rounded-xl shadow-sm p-8 max-w-4xl mx-auto">
            <h2 className="text-2xl font-bold mb-6 text-slate-800">Create New Blog Post</h2>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
              <div>
                 <label className="block text-sm font-bold text-slate-700 mb-2">Slug (URL)</label>
                 <input 
                   className="w-full px-4 py-2 border rounded-lg" 
                   placeholder="my-new-post"
                   value={newPost.slug}
                   onChange={e => setNewPost({...newPost, slug: e.target.value})}
                 />
              </div>
              <div>
                 <label className="block text-sm font-bold text-slate-700 mb-2">Category</label>
                 <input 
                   className="w-full px-4 py-2 border rounded-lg" 
                   placeholder="Travel Guide"
                   value={newPost.category}
                   onChange={e => setNewPost({...newPost, category: e.target.value})}
                 />
              </div>
            </div>

            {/* Image Upload */}
            <div className="mb-8 border-2 border-dashed border-slate-300 rounded-xl p-8 text-center bg-slate-50">
              {newPost.image ? (
                <div className="relative inline-block">
                  <img src={newPost.image} alt="Preview" className="h-48 rounded-lg shadow-md" />
                  <button 
                    onClick={() => setNewPost({...newPost, image: ''})}
                    className="absolute -top-2 -right-2 bg-red-500 text-white rounded-full p-1 shadow"
                  >
                    <Trash2 size={16} />
                  </button>
                </div>
              ) : (
                <label className="cursor-pointer block">
                   <div className="w-16 h-16 bg-brand-100 text-brand-600 rounded-full flex items-center justify-center mx-auto mb-4">
                     {uploading ? <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-brand-600"></div> : <Upload size={32} />}
                   </div>
                   <span className="font-bold text-brand-600 block">Click to Upload Cover Image</span>
                   <span className="text-xs text-slate-500">JPG, PNG, WEBP</span>
                   <input type="file" className="hidden" onChange={handleImageUpload} />
                </label>
              )}
            </div>

            {/* Multi-language inputs */}
            <div className="space-y-8">
               {/* Spanish */}
               <div className="bg-orange-50 p-6 rounded-xl border border-orange-100">
                  <h3 className="font-bold text-orange-800 mb-4">Spanish Content (ES)</h3>
                  <input 
                    className="w-full px-4 py-2 border rounded-lg mb-4" 
                    placeholder="Título en Español"
                    value={newPost.title?.es}
                    onChange={e => setNewPost({...newPost, title: {...newPost.title!, es: e.target.value}})}
                  />
                  <textarea 
                    className="w-full px-4 py-2 border rounded-lg h-32" 
                    placeholder="Contenido principal..."
                    value={newPost.content?.es}
                    onChange={e => setNewPost({...newPost, content: {...newPost.content!, es: e.target.value}})}
                  />
               </div>

               {/* English */}
               <div className="bg-blue-50 p-6 rounded-xl border border-blue-100">
                  <h3 className="font-bold text-blue-800 mb-4">English Content (EN)</h3>
                  <input 
                    className="w-full px-4 py-2 border rounded-lg mb-4" 
                    placeholder="English Title"
                    value={newPost.title?.en}
                    onChange={e => setNewPost({...newPost, title: {...newPost.title!, en: e.target.value}})}
                  />
                  <textarea 
                    className="w-full px-4 py-2 border rounded-lg h-32" 
                    placeholder="Main content..."
                    value={newPost.content?.en}
                    onChange={e => setNewPost({...newPost, content: {...newPost.content!, en: e.target.value}})}
                  />
               </div>
            </div>

            <div className="mt-8 pt-8 border-t flex justify-end">
              <button 
                onClick={handleSubmit}
                className="bg-brand-600 text-white font-bold px-8 py-3 rounded-xl hover:bg-brand-700 shadow-lg"
              >
                Publish Post
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default AdminPage;
