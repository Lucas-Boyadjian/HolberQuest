// This file contains the main JavaScript logic for the frontend application.

// Function to initialize the application
function initApp() {
    // Load player data from local storage or API
    loadPlayerData();
    
    // Set up event listeners for buttons and interactions
    setupEventListeners();
}

// Function to load player data
function loadPlayerData() {
    // Fetch player data from the backend API
    fetch('/api/player')
        .then(response => response.json())
        .then(data => {
            // Update the UI with player data
            updateProfileUI(data);
        })
        .catch(error => console.error('Error loading player data:', error));
}

// Function to update the profile UI
function updateProfileUI(player) {
    document.getElementById('username').innerText = player.username;
    document.getElementById('avatar').src = player.avatar;
    document.getElementById('level').innerText = `Level: ${player.level}`;
    document.getElementById('xp').innerText = `XP: ${player.xp}`;
}

// Function to set up event listeners
function setupEventListeners() {
    document.getElementById('quest-button').addEventListener('click', startQuest);
}

// Function to start a quest
function startQuest() {
    // Fetch a new quest from the backend API
    fetch('/api/quest')
        .then(response => response.json())
        .then(quest => {
            // Display the quest question to the player
            displayQuest(quest);
        })
        .catch(error => console.error('Error fetching quest:', error));
}

// Function to display the quest question
function displayQuest(quest) {
    document.getElementById('quest-question').innerText = quest.question;
    // Additional logic to handle quest answers can be added here
}

// Initialize the application when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initApp);