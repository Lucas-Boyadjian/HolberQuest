const avatarContainer = document.getElementById('avatar-container');
const avatarInput = document.getElementById('avatar-input');
const selectedAvatar = document.getElementById('selected-avatar');

// Function to display the selected avatar
function displaySelectedAvatar(avatar) {
    selectedAvatar.src = avatar;
}

// Event listener for avatar selection
avatarInput.addEventListener('change', (event) => {
    const avatar = event.target.value;
    displaySelectedAvatar(avatar);
});

// Function to initialize avatar selection
function initAvatarSelection() {
    const defaultAvatar = avatarInput.value;
    if (defaultAvatar) {
        displaySelectedAvatar(defaultAvatar);
    }
}

// Initialize avatar selection on page load
document.addEventListener('DOMContentLoaded', initAvatarSelection);