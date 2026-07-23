/**
 * Configuração compartilhada: Supabase Auth + chamadas à FastAPI.
 * Carregue este script antes do código específico de cada página.
 */
const API = (() => {
  const { origin, port } = window.location;
  if (port === "8000" || origin.includes("localhost:8000") || origin.includes("127.0.0.1:8000")) {
    return origin;
  }
  return "http://localhost:8000";
})();

let sb = null;
let _token = localStorage.getItem("access_token") || "";

async function initApp({ requireAuth = false } = {}) {
  const res = await fetch(`${API}/config`);
  if (!res.ok) throw new Error("Não foi possível carregar a configuração da API");
  const cfg = await res.json();

  sb = supabase.createClient(cfg.supabase_url, cfg.supabase_anon_key);

  const { data } = await sb.auth.getSession();
  if (data?.session) {
    _token = data.session.access_token;
    localStorage.setItem("access_token", _token);
    localStorage.setItem("user_id", data.session.user.id);
  }

  sb.auth.onAuthStateChange((_event, session) => {
    if (session) {
      _token = session.access_token;
      localStorage.setItem("access_token", _token);
      localStorage.setItem("user_id", session.user.id);
    }
  });

  if (requireAuth && !_token) {
    window.location.href = "login.html";
    return false;
  }
  return true;
}

function getToken() {
  return _token;
}

function authHeaders(extra = {}) {
  return { "Content-Type": "application/json", Authorization: `Bearer ${getToken()}`, ...extra };
}

async function apiFetch(path, opts = {}) {
  const res = await fetch(API + path, {
    ...opts,
    headers: { ...authHeaders(), ...(opts.headers || {}) },
  });
  if (res.status === 401) {
    await logout();
    return null;
  }
  if (res.status === 429) {
    window.dispatchEvent(new CustomEvent("api:ratelimit"));
    return null;
  }
  if (res.status === 204) return {};
  const text = await res.text();
  return text ? JSON.parse(text) : {};
}

async function logout() {
  if (sb) await sb.auth.signOut();
  localStorage.clear();
  window.location.href = "login.html";
}
