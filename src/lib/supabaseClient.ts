import { createClient } from '@supabase/supabase-js';

// NOTA PARA EL USUARIO:
// 1. Ve a https://supabase.com/ y crea un proyecto gratuito.
// 2. Ve a Project Settings > API.
// 3. Copia la "URL" y la "anon" public key.
// 4. Reemplaza los valores abajo.

// Cast import.meta to any to avoid TypeScript error about missing 'env' property
const supabaseUrl = (import.meta as any).env.VITE_SUPABASE_URL || 'https://tu-proyecto.supabase.co';
const supabaseKey = (import.meta as any).env.VITE_SUPABASE_ANON_KEY || 'tu-anon-key';

export const supabase = createClient(supabaseUrl, supabaseKey);