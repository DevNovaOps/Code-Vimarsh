document.addEventListener('DOMContentLoaded', function() {
  
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Load events
    loadEvents();
});

async function loadEvents() {
    const container = document.getElementById('events-container');
    if (!container) return;

    try {
        const response = await fetch('/api/events/');
        const data = await response.json();
        
        if (data.events && data.events.length > 0) {
            container.innerHTML = '';
            data.events.forEach(event => {
                const eventCard = createEventCard(event);
                container.appendChild(eventCard);
            });
        } else {
            container.innerHTML = '<div class="loading">No upcoming events at the moment. Check back soon!</div>';
        }
    } catch (error) {
        console.error('Error loading events:', error);
        container.innerHTML = '<div class="loading">Error loading events. Please refresh the page.</div>';
    }
}

function createEventCard(event) {
    const card = document.createElement('div');
    card.className = 'event-card';
    
    const title = document.createElement('h3');
    title.className = 'event-title';
    title.textContent = event.title;
    
    const date = document.createElement('div');
    date.className = 'event-date';
    date.innerHTML = `📅 ${event.date}`;
    
    const description = document.createElement('p');
    description.className = 'event-description';
    description.textContent = event.description;
    
    card.appendChild(title);
    card.appendChild(date);
    card.appendChild(description);
    
    if (event.registration_link) {
        const registerBtn = document.createElement('a');
        registerBtn.href = event.registration_link;
        registerBtn.target = '_blank';
        registerBtn.rel = 'noopener noreferrer';
        registerBtn.className = 'btn-register';
        registerBtn.textContent = 'Register Now';
        card.appendChild(registerBtn);
    }
    
    return card;
}


