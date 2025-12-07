
import React, { useState } from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import HomePage from './pages/HomePage';
import BlogPage from './pages/BlogPage';
import BlogPost from './pages/BlogPost';
import AdminPage from './pages/AdminPage';
import { Language } from './types';
import { CMSProvider } from './context/CMSContext';

const App: React.FC = () => {
  const [lang, setLang] = useState<Language>('es');

  return (
    <CMSProvider>
      <Router>
        <Routes>
          {/* Admin Route - Separate Layout */}
          <Route path="/admin" element={<AdminPage />} />
          
          {/* Public Routes - Wrapped in Main Layout */}
          <Route path="*" element={
            <Layout lang={lang} setLang={setLang}>
              <Routes>
                <Route path="/" element={<HomePage lang={lang} />} />
                <Route path="/blog" element={<BlogPage lang={lang} />} />
                <Route path="/blog/:slug" element={<BlogPost lang={lang} />} />
              </Routes>
            </Layout>
          } />
        </Routes>
      </Router>
    </CMSProvider>
  );
};

export default App;
