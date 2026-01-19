const addAssignmentBtn = document.getElementById("AddAssignmentBtn");
const addAssignmentModal = document.getElementById("AddAssignmentModal");
const closeAssignmentModal = addAssignmentModal.querySelector(".close");

addAssignmentBtn.addEventListener("click", () => {
    addAssignmentModal.style.display = "block";
});

closeAssignmentModal.addEventListener("click", () => {
    addAssignmentModal.style.display = "none";
});

window.addEventListener("click", (e) => {
    if (e.target === addAssignmentModal) {
        addAssignmentModal.style.display = "none";
    }
});


const addEventBtn = document.getElementById("AddEventBtn");
const addEventModal = document.getElementById("AddEventModal");
const closeEventModal = addEventModal.querySelector(".close");

addEventBtn.addEventListener("click", () => {
    addEventModal.style.display = "block";
});

closeEventModal.addEventListener("click", () => {
    addEventModal.style.display = "none";
});

window.addEventListener("click", (e) => {
    if (e.target === addEventModal) {
        addEventModal.style.display = "none";
    }
});