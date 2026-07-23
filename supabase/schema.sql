-- Schema do projeto "teste" (NIM Chat)
-- Aplicado via Supabase MCP em 2026-07-09

-- chat_sessions
ALTER TABLE public.chat_sessions
  ADD COLUMN IF NOT EXISTS created_at timestamptz NOT NULL DEFAULT now();

ALTER TABLE public.chat_sessions
  ALTER COLUMN user_id DROP DEFAULT;

-- users_profile
CREATE TABLE IF NOT EXISTS public.users_profile (
  id uuid PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  full_name text,
  avatar_url text,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

ALTER TABLE public.users_profile ENABLE ROW LEVEL SECURITY;

CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
  INSERT INTO public.users_profile (id)
  VALUES (NEW.id)
  ON CONFLICT (id) DO NOTHING;
  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- RLS: chat_sessions
DROP POLICY IF EXISTS "Users manage own sessions" ON public.chat_sessions;
CREATE POLICY "Users manage own sessions" ON public.chat_sessions
  FOR ALL
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

-- RLS: chat_messages
DROP POLICY IF EXISTS "Users manage messages in own sessions" ON public.chat_messages;
CREATE POLICY "Users manage messages in own sessions" ON public.chat_messages
  FOR ALL
  USING (
    EXISTS (
      SELECT 1 FROM public.chat_sessions s
      WHERE s.id = chat_messages.session_id AND s.user_id = auth.uid()
    )
  )
  WITH CHECK (
    EXISTS (
      SELECT 1 FROM public.chat_sessions s
      WHERE s.id = chat_messages.session_id AND s.user_id = auth.uid()
    )
  );

-- RLS: users_profile
DROP POLICY IF EXISTS "Users manage own profile" ON public.users_profile;
CREATE POLICY "Users manage own profile" ON public.users_profile
  FOR ALL
  USING (auth.uid() = id)
  WITH CHECK (auth.uid() = id);

-- Storage: avatars
DROP POLICY IF EXISTS "Avatar images are publicly accessible" ON storage.objects;
CREATE POLICY "Avatar images are publicly accessible" ON storage.objects
  FOR SELECT USING (bucket_id = 'avatars');

DROP POLICY IF EXISTS "Users upload own avatars" ON storage.objects;
CREATE POLICY "Users upload own avatars" ON storage.objects
  FOR INSERT WITH CHECK (
    bucket_id = 'avatars' AND auth.uid()::text = split_part(name, '_', 1)
  );

DROP POLICY IF EXISTS "Users update own avatars" ON storage.objects;
CREATE POLICY "Users update own avatars" ON storage.objects
  FOR UPDATE USING (
    bucket_id = 'avatars' AND auth.uid()::text = split_part(name, '_', 1)
  );

DROP POLICY IF EXISTS "Users delete own avatars" ON storage.objects;
CREATE POLICY "Users delete own avatars" ON storage.objects
  FOR DELETE USING (
    bucket_id = 'avatars' AND auth.uid()::text = split_part(name, '_', 1)
  );

-- Revoke direct RPC access to trigger function (only used by auth trigger)
REVOKE ALL ON FUNCTION public.handle_new_user() FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.handle_new_user() TO service_role;

-- Storage: user_uploads (private bucket)
UPDATE storage.buckets SET public = false WHERE id = 'user_uploads';

DROP POLICY IF EXISTS "Users update own uploads" ON storage.objects;
CREATE POLICY "Users update own uploads" ON storage.objects
  FOR UPDATE USING (
    bucket_id = 'user_uploads' AND auth.uid()::text = (storage.foldername(name))[1]
  );

DROP POLICY IF EXISTS "Users upload own files" ON storage.objects;
CREATE POLICY "Users upload own files" ON storage.objects
  FOR INSERT WITH CHECK (
    bucket_id = 'user_uploads' AND auth.uid()::text = (storage.foldername(name))[1]
  );

DROP POLICY IF EXISTS "Users read own uploads" ON storage.objects;
CREATE POLICY "Users read own uploads" ON storage.objects
  FOR SELECT USING (
    bucket_id = 'user_uploads' AND auth.uid()::text = (storage.foldername(name))[1]
  );

DROP POLICY IF EXISTS "Users delete own uploads" ON storage.objects;
CREATE POLICY "Users delete own uploads" ON storage.objects
  FOR DELETE USING (
    bucket_id = 'user_uploads' AND auth.uid()::text = (storage.foldername(name))[1]
  );
