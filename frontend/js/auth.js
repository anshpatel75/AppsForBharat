export function saveUser(user_id, is_admin) {
  localStorage.setItem('user_id', user_id);
  localStorage.setItem('is_admin', is_admin ? 'true' : 'false');
}

export function isAdmin() {
  return localStorage.getItem('is_admin') === 'true';
}

export function getUser() {
  return localStorage.getItem('user_id');
}

export function logout() {
  localStorage.removeItem('user_id');
  localStorage.removeItem('is_admin');
  window.location.href = 'index.html';
}
