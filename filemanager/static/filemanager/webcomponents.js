const loginCard = document.createElement('template');
loginCard.innerHTML = `
<style>

.container {
    width: 480px;
    height: 100%;
    display: flex;
    flex-direction: column;
    background: rgb(1,20,100);
    background: linear-gradient(150deg, rgba(1,20,100,1) 30%, rgba(244,91,4,1) 93%);
    justify-content: center;
    align-items: center;
    border-radius: 8px;
    margin: 24px 16px;
}

input {
    width: 75%;
    border: 60px;
}

button {
    width: 75%;
    background-color: var(--color-terciary);
}

h1 {
    font-size: 56px;
}

h2 {
    font-size: 40px;

}

#passreset {
    margin-top: 47px;
}
</style>

<div class="container">

    <h1>ETIC_DRIVE</h1>
    
    <h2>Login</h2>

    <p>Don't have an account yet? <a href="${window.location.origin}/signup">Click here</a></p>


    <label>User</label>
    <input type="text">

    <label>Password</label>
    <input type="text">

    <button type="submit">Log in</button>

    <a href="" id="passreset">Forgot your password?</a>

    <img src="/static/filemanager/logo_branco.png" alt="etic algarve logo">

    <p><a href="">Terms of service</a> | <a href="">Privacy Policy</a></p>

</div>
`

class LoginCard extends HTMLElement {

    shadowRoot = null;

    constructor() {

        super();
        
        this.shadowRoot = this.attachShadow({ mode: 'closed' });
        this.shadowRoot.appendChild(loginCard.content.cloneNode(true));

    }
}
customElements.define('login-card', LoginCard);
