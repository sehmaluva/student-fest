document.getElementById('generate').addEventListener('click', () => {
    const username = document.getElementById('username').value;
    if (!username) {
        alert('Please enter a GitHub username.');
        return;
    }

    const badgeUrl = `https://img.shields.io/github/followers/${username}?style=social`;
    const badgeContainer = document.getElementById('badge-container');
    badgeContainer.innerHTML = `
        <h3>Your Badge:</h3>
        <img src="${badgeUrl}" alt="GitHub followers badge">
        <p>Markdown:</p>
        <code>![GitHub followers](https://img.shields.io/github/followers/${username}?style=social)</code>
    `;
});
