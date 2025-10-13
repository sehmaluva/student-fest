document.addEventListener('DOMContentLoaded', () => {
    fetch('contributors.json')
        .then(response => response.json())
        .then(data => {
            const grid = document.getElementById('contributors-grid');
            data.forEach(contributor => {
                const card = document.createElement('div');
                card.className = 'contributor-card';

                const avatar = document.createElement('img');
                avatar.src = contributor.avatar_url;
                avatar.alt = `${contributor.username}'s avatar`;

                const name = document.createElement('h2');
                name.textContent = contributor.username;

                const funFact = document.createElement('p');
                funFact.textContent = `"${contributor.fun_fact}"`;

                const emoji = document.createElement('div');
                emoji.className = 'emoji';
                emoji.textContent = contributor.favorite_emoji;

                const profileLink = document.createElement('a');
                profileLink.href = contributor.profile_url;
                profileLink.target = '_blank';
                profileLink.textContent = 'View Profile';

                card.appendChild(avatar);
                card.appendChild(name);
                card.appendChild(funFact);
                card.appendChild(emoji);
                card.appendChild(profileLink);

                grid.appendChild(card);
            });
        })
        .catch(error => console.error('Error loading contributors:', error));
});
