const loginCard = document.createElement('template');
loginCard.innerHTML = `
<style>

.container {
    display: flex;

}

input {
    width: 75%;
}

button {
    width: 75%;
}
</style>

<div class="container">

    <h1>ETIC_DRIVE</h1>
    
    <h2>Login</h2>

    <p>Don't have an account yet? Click here</p>

    <label>User</label>
    <input type="text">

    <label>Password</label>
    <input type="text">

    <button type="submit">Log in</button>

    <a href="">Forgot your password?</a>

    <img src="" alt="etic algarve logo">

    <p><a href="">Terms of service</a>|<a href="">Privacy Policy</a></p>

</div>
`

class LoginCard extends HTMLElement{

    shadowRoot;

    constructor() {
        super();
        this.shadowRoot = this.attachShadow({ mode: 'closed' });
        this.shadowRoot.appendChild(toggleTemplate.content.cloneNode(true));

    }
}
customElements.define('login-card', LoginCard);
