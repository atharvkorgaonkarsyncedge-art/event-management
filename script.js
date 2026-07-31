const eventList = []; // Array to store event objects

// Function to handle adding events
document.getElementById('event-form')?.addEventListener('submit', function(e) {
    e.preventDefault();

    const eventName = document.getElementById('event-name').value;
    const eventDate = document.getElementById('event-date').value;
    const eventCategory = document.getElementById('event-category').value;
    const eventLocation = document.getElementById('event-location').value;

    // Create event object and push to array
    const newEvent = {
        name: eventName,
        date: eventDate,
        category: eventCategory,
        location: eventLocation
    };

    eventList.push(newEvent);
    updateEventList();
    populateDropdowns();

    // Clear the form
    this.reset();
});

// Function to update the events list in the UI
function updateEventList() {
    const eventListElement = document.getElementById('event-list');
    if (eventListElement) {
        eventListElement.innerHTML = ''; // Clear current list

        eventList.forEach(event => {
            const listItem = document.createElement('li');
            listItem.textContent = `${event.name} on ${event.date} (${event.category} at ${event.location})`;
            eventListElement.appendChild(listItem);
        });
    }
}

// Function to populate event dropdowns for registration and feedback
function populateDropdowns() {
    const selectEventElement = document.getElementById('select-event');
    const feedbackEventElement = document.getElementById('feedback-event');

    // Clear existing options
    if (selectEventElement) {
        selectEventElement.innerHTML = '';
    }
    if (feedbackEventElement) {
        feedbackEventElement.innerHTML = '';
    }

    // Populate dropdowns with events
    eventList.forEach((event, index) => {
        const option = document.createElement('option');
        option.value = index; // Use index as value
        option.textContent = event.name;
        if (selectEventElement) {
            selectEventElement.appendChild(option);
        }
        if (feedbackEventElement) {
            const feedbackOption = document.createElement('option');
            feedbackOption.value = index; // Use index as value
            feedbackOption.textContent = event.name;
            feedbackEventElement.appendChild(feedbackOption);
        }
    });
}

// Function to handle event registration
document.getElementById('register-event-form')?.addEventListener('submit', function(e) {
    e.preventDefault();

    const yourName = document.getElementById('your-name').value;
    const selectedEventIndex = document.getElementById('select-event').value;

    if (selectedEventIndex !== '') {
        const event = eventList[selectedEventIndex];
        alert(`Registered ${yourName} for the event: ${event.name}`);
        this.reset(); // Clear the form
    } else {
        alert('Please select an event to register.');
    }
});

// Function to handle feedback submission
document.getElementById('feedback-form')?.addEventListener('submit', function(e) {
    e.preventDefault();

    const selectedFeedbackIndex = document.getElementById('feedback-event').value;
    const feedbackText = document.getElementById('feedback-text').value;

    if (selectedFeedbackIndex !== '') {
        const event = eventList[selectedFeedbackIndex];
        alert(`Feedback submitted for ${event.name}: "${feedbackText}"`);
        this.reset(); // Clear the form
    } else {
        alert('Please select an event to provide feedback.');
    }
});
