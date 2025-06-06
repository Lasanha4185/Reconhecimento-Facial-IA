function validarLogin() {
    const usuario = document.getElementById('username').value;
    const senha = document.getElementById('password').value;

    if (usuario === 'admin' && senha === '1234') {
        window.location.href = "Prot.html";
        return false;
    } else {
        alert('Usuário ou senha incorretos!');
        return false;
    }
}
