/**
 * Shared Supabase authentication and FastAPI helpers.
 */

let API = (() => {
  const { origin, port } = window.location;
  if (port === "8000" || origin.includes("localhost:8000") || origin.includes("127.0.0.1:8000")) {
    return origin;
  }
  return "http://localhost:8000";
})();

let sb = null;
let _token = localStorage.getItem("access_token") || "";
let IS_TESTE = false;

async function initApp({ requireAuth = false } = {}) {
  const res = await fetch(`${API}/config`);
  if (!res.ok) throw new Error("Não foi possível carregar a configuração da API");
  const cfg = await res.json();

  API = cfg.api_base || API;
  IS_TESTE = Boolean(cfg.teste || cfg.teste_eval);
  sb = window.supabase.createClient(cfg.supabase_url, cfg.supabase_anon_key);

  const { data } = await sb.auth.getSession();
  if (data?.session) {
    _token = data.session.access_token;
    localStorage.setItem("access_token", _token);
    localStorage.setItem("user_id", data.session.user.id);
  }

  sb.auth.onAuthStateChange((_event, session) => {
    _token = session?.access_token || "";
    if (session) {
      localStorage.setItem("access_token", _token);
      localStorage.setItem("user_id", session.user.id);
    } else {
      localStorage.removeItem("access_token");
      localStorage.removeItem("user_id");
    }
  });

  if (requireAuth && !_token) {
    window.location.href = "login.html";
    return false;
  }
  return true;
}

function getToken() {
  return _token || localStorage.getItem("access_token") || "";
}

function authHeaders(extra = {}) {
  const headers = { "Content-Type": "application/json", ...extra };
  const token = getToken();
  if (token) headers.Authorization = `Bearer ${token}`;
  return headers;
}

async function apiFetch(path, opts = {}) {
  const headers = { ...authHeaders(), ...(opts.headers || {}) };
  if (opts.body instanceof FormData && !opts.headers?.["Content-Type"]) {
    delete headers["Content-Type"];
  }
  const res = await fetch(API + path, {
    ...opts,
    headers,
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
  const data = text ? JSON.parse(text) : {};
  if (!res.ok) {
    throw new Error(`API Error ${res.status}: ${res.statusText}`);
  }
  return data;
}

async function apiCall(endpoint, options = {}) {
  const requestOptions = { ...options };
  if (requestOptions.body && !(requestOptions.body instanceof FormData)) {
    requestOptions.body = JSON.stringify(requestOptions.body);
  }
  return apiFetch(endpoint, requestOptions);
}

async function logout() {
  if (sb) {
    try {
      await sb.auth.signOut();
    } catch (error) {
      console.warn("Erro ao fazer logout no Supabase:", error);
    }
  }
  _token = "";
  localStorage.removeItem("access_token");
  localStorage.removeItem("user_id");
  window.location.href = "login.html";
}

function showToast(message, type = "", duration = 3000) {
  let toastEl = document.getElementById("toast");
  if (!toastEl) {
    toastEl = document.createElement("div");
    toastEl.id = "toast";
    toastEl.className = "toast";
    document.body.appendChild(toastEl);
  }

  toastEl.textContent = message;
  toastEl.className = `toast show ${type}`;

  if (duration > 0) {
    setTimeout(() => toastEl.classList.remove("show"), duration);
  }
}

function getUserId() {
  return localStorage.getItem("user_id");
}
