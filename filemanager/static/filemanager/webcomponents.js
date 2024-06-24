const loginCard = document.createElement('template');
loginCard.innerHTML = `
<style>

.container {
    width: 480px;
    height: 94.5%;
    display: flex;
    flex-direction: column;
    background: rgb(1,20,100);
    background: linear-gradient(150deg, rgba(1,20,100,1) 30%, rgba(244,91,4,1) 93%);
    align-items: center;
    border-radius: 8px;
    margin: 24px 16px;
}

form {
    display: flex;
    flex-direction: column;
    width: 65%;
    align-items: center;
    margin-top: 16px;
}

label {
    margin-right: auto;
}
input {
    width: 97%;
    height: 32px;
    margin-bottom: 16px;
    font-size: 16px;
    font-family: var(--font-secondary);
    padding-left: 4px;
}

a {
    text-decoration: none;
    color: var(--color-text);
}
button {
    width: 100%;
    height: 32px;
    border: 0;
    background-color: var(--color-terciary);
    margin-top: 16px;
    color: var(--color-text);
    font-weight: 700;
    cursor: pointer;
}

h1 {
    font-size: 56px;
    font-family: var(--font-primary)
    font-weight: bolder;
}

h2 {
    font-size: 40px;
    font-family: var(--font-secondary);
    font-weight: 500;
}

img {
    width: 50%;
    margin: 16px;
}

#passreset {
    margin-top: 47px;
}
</style>

<div class="container">

    <h1>ETIC_DRIVE</h1>
    
    <h2>Login</h2>

    <p>Don't have an account yet? <a href="${window.location.origin}/signup">Click here</a></p>


    <form method="post" action="${window.location.origin}/login/">
        <label>User</label>
        <input type="text" name="username">

        <label>Password</label>
        <input type="password" name="password">

        <button type="submit">Log in</button>
    </form>

    <a href="" id="passreset">Forgot your password?</a>

    <img src="/static/filemanager/logo_branco.png" alt="etic algarve logo">

    <p><a href="">Terms of service</a> | <a href="">Privacy Policy</a></p>

</div>
`
function getCsrfToken() {
    const cookieString = document.cookie;
    // Matches any characters that are not ;
    const csrfTokenPart = cookieString.match(/csrftoken=([^;]*)/);
    if (csrfTokenPart) {
      return csrfTokenPart[1];
    }
    return null;
  }

class LoginCard extends HTMLElement {

    shadowRoot = null;

    constructor() {

        super();
        
        this.shadowRoot = this.attachShadow({ mode: 'closed' });
        this.shadowRoot.appendChild(loginCard.content.cloneNode(true));

    }

    
    connectedCallback() {
        const form = this.shadowRoot.querySelector('form');
        console.log("form")
        const csrfToken = getCsrfToken();
        console.log(csrfToken)
        if (csrfToken) {
            const form = this.shadowRoot.querySelector('form');
    
            if (csrfToken) {
                const csrfInput = document.createElement('input');
                csrfInput.type = 'hidden';
                csrfInput.name = 'csrfmiddlewaretoken';
                csrfInput.value = csrfToken;
                form.insertBefore(csrfInput, form.firstChild);
            }
        }
    }
}
customElements.define('login-card', LoginCard);


