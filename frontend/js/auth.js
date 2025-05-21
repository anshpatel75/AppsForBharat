export function saveUser(user_id) {
  localStorage.setItem('user_id', user_id);
}

export function getUser() {
  return localStorage.getItem('user_id');
}

export function logout() {
  localStorage.removeItem('user_id');
}
