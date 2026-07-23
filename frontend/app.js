/**
 * app.js - Módulo central do frontend NIM Chat
 * Responsável por inicializar Supabase, autenticação e utilitários globais
 */

let sb = null;         // Cliente Supabase
let API = null;        // URL base da API
let IS_TESTE = false;  // Flag de modo de teste

/**
 * Retorna o token JWT do localStorage
 */
function getToken() {
  return localStorage.getItem("access_token");
}

/**
 * Retorna headers de autenticação para requisições à API
 */
function authHeaders() {
  const token = getToken();
  return {
    "Authorization": `Bearer ${token}`,
    "Content-Type": "application/json"
  };
}

/**
 * Faz logout do usuário
 */
async function logout() {
  try {
    if (sb) {
      await sb.auth.signOut();
    }
  } catch (e) {
    console.warn("Erro ao fazer logout no Supabase:", e);
  }
  localStorage.removeItem("access_token");
  localStorage.removeItem("user_id");
  window.location.href = "login.html";
}

/**
 * Inicializa a aplicação
 * @param {Object} options - Opções de inicialização
 * @param {boolean} options.requireAuth - Se true, redireciona para login se não autenticado
 * @returns {Promise<boolean>} true se inicialização bem-sucedida, false caso contrário
 */
async function initApp(options = {}) {
  try {
    // Se já foi inicializado e temos token, pula
    if (sb && getToken()) {
      return true;
    }

    // Fetch da configuração
    const configRes = await fetch("config");
    if (!configRes.ok) {
      throw new Error(`Falha ao obter config: ${configRes.status}`);
    }
    const config = await configRes.json();

    // Define URL da API
    API = config.api_base || window.location.origin;
    IS_TESTE = config.teste || config.teste_eval || false;

    // Inicializa Supabase
    const { createClient } = window.supabase;
    sb = createClient(config.supabase_url, config.supabase_anon_key);

    // Verifica se há sessão ativa (refresh token no localStorage)
    const token = getToken();
    if (token) {
      // Valida o token
      try {
        const { data, error } = await sb.auth.getUser(token);
        if (error || !data?.user) {
          localStorage.removeItem("access_token");
          localStorage.removeItem("user_id");
          if (options.requireAuth) {
            window.location.href = "login.html";
            return false;
          }
          return false;
        }
      } catch (e) {
        localStorage.removeItem("access_token");
        localStorage.removeItem("user_id");
        if (options.requireAuth) {
          window.location.href = "login.html";
          return false;
        }
        return false;
      }
    } else if (options.requireAuth) {
      window.location.href = "login.html";
      return false;
    }

    return true;
  } catch (error) {
    console.error("❌ Erro ao inicializar app:", error);
    if (options.requireAuth) {
      window.location.href = "login.html";
    }
    return false;
  }
}

/**
 * Função auxiliar para mostrar toasts (mensagens flutuantes)
 * @param {string} message - Mensagem a exibir
 * @param {string} type - Tipo: "success", "error", ou vazio para info
 * @param {number} duration - Duração em ms (padrão: 3000)
 */
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
    setTimeout(() => {
      toastEl.classList.remove("show");
    }, duration);
  }
}

/**
 * Realiza uma chamada à API com autenticação
 * @param {string} endpoint - Endpoint da API (ex: "/sessions")
 * @param {Object} options - Opções do fetch (method, body, etc)
 * @returns {Promise<Object>} Resposta JSON da API
 */
async function apiCall(endpoint, options = {}) {
  try {
    if (!API) {
      throw new Error("API não foi inicializada. Chame initApp() primeiro.");
    }

    const url = API + endpoint;
    const finalOptions = {
      ...options,
      headers: {
        ...authHeaders(),
        ...options.headers
      }
    };

    // Se tem body, serializa como JSON (a menos que seja FormData)
    if (options.body && !(options.body instanceof FormData)) {
      finalOptions.body = JSON.stringify(options.body);
    }

    const response = await fetch(url, finalOptions);

    if (response.status === 401) {
      localStorage.removeItem("access_token");
      localStorage.removeItem("user_id");
      window.location.href = "login.html";
      return null;
    }

    if (!response.ok) {
      throw new Error(`API Error ${response.status}: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error(`❌ Erro em apiCall(${endpoint}):`, error);
    throw error;
  }
}

/**
 * Retorna o user_id do localStorage
 */
function getUserId() {
  return localStorage.getItem("user_id");
}
