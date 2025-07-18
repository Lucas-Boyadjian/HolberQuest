// This file contains the logic for handling quests and submitting answers.

document.addEventListener('DOMContentLoaded', () => {
    const questForm = document.getElementById('quest-form');
    const questDisplay = document.getElementById('quest-display');
    const resultDisplay = document.getElementById('result-display');

    // Function to fetch a new quest
    async function fetchQuest() {
        const response = await fetch('/api/quest');
        const quest = await response.json();
        displayQuest(quest);
    }

    // Function to display the quest
    function displayQuest(quest) {
        questDisplay.innerHTML = `
            <h2>${quest.question}</h2>
            <input type="text" id="answer" placeholder="Your answer" />
            <button id="submit-answer">Submit</button>
        `;
        document.getElementById('submit-answer').addEventListener('click', () => submitAnswer(quest.id));
    }

    // Function to submit the answer
    async function submitAnswer(questId) {
        const answerInput = document.getElementById('answer');
        const answer = answerInput.value;

        const response = await fetch(`/api/quest/${questId}/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ answer }),
        });

        const result = await response.json();
        displayResult(result);
    }

    // Function to display the result of the answer submission
    function displayResult(result) {
        resultDisplay.innerHTML = `
            <p>${result.message}</p>
            <p>XP Gained: ${result.xp}</p>
        `;
        fetchQuest(); // Fetch a new quest after submitting
    }

    // Initial fetch of a quest
    fetchQuest();
});