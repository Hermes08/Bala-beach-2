import React, { useState } from 'react';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import HomePage from './pages/HomePage';
import BlogPage from './pages/BlogPage';
import BlogPost from './pages/BlogPost';
import { Language } from './types';

const App: React.FC = () => {
  const [lang, setLang] = useState<Language>('es');

  return (
    <Router>
      <Layout lang={lang} setLang={setLang}>
        <Routes>
          <Route path="/" element={<HomePage lang={lang} />} />
          <Route path="/blog" element={<BlogPage lang={lang} />} />
          <Route path="/blog/:slug" element={<BlogPost lang={lang} />} />
        </Routes>
      </Layout>
    </Router>
  );
};

export default App;