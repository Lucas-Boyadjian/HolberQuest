const leaderboardContainer = document.getElementById('leaderboard');
const apiUrl = '/api/leaderboard'; // Adjust the API endpoint as necessary

async function fetchLeaderboard() {
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const leaderboardData = await response.json();
        displayLeaderboard(leaderboardData);
    } catch (error) {
        console.error('Error fetching leaderboard:', error);
        leaderboardContainer.innerHTML = '<p>Failed to load leaderboard.</p>';
    }
}

function displayLeaderboard(data) {
    leaderboardContainer.innerHTML = ''; // Clear existing content
    const list = document.createElement('ul');

    data.forEach(player => {
        const listItem = document.createElement('li');
        listItem.textContent = `${player.username} - Level: ${player.level}, XP: ${player.experience}`;
        list.appendChild(listItem);
    });

    leaderboardContainer.appendChild(list);
}

// Initialize leaderboard on page load
document.addEventListener('DOMContentLoaded', fetchLeaderboard);