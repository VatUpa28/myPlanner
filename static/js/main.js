document.addEventListener("DOMContentLoaded", () => {
  const addAssignmentBtn = document.getElementById("AddAssignmentBtn");
  const addAssignmentModal = document.getElementById("AddAssignmentModal");
  const closeAddAssignmentModal = addAssignmentModal.querySelector(".close");

  addAssignmentBtn.addEventListener("click", () => {
    addAssignmentModal.style.display = "block";
  });

  closeAddAssignmentModal.addEventListener("click", () => {
    addAssignmentModal.style.display = "none";
  });

  const addEventBtn = document.getElementById("AddEventBtn");
  const addEventModal = document.getElementById("AddEventModal");
  const closeAddEventModal = addEventModal.querySelector(".close");

  addEventBtn.addEventListener("click", () => {
    addEventModal.style.display = "block";
  });

  closeAddEventModal.addEventListener("click", () => {
    addEventModal.style.display = "none";
  });

  const updateEventModal = document.getElementById("UpdateEventModal");
  const closeUpdateEventModal = updateEventModal.querySelector(".close");
  const updateEventButton = document.querySelectorAll(".update-event-button");

  updateEventButton.forEach((btn) => {
    btn.addEventListener("click", () => {
      const eventId = btn.getAttribute("data-id");
      const eventName = btn.getAttribute("data-name");
      const eventDate = btn.getAttribute("data-date");

      document.getElementById("updateEventName").value = eventName;
      document.getElementById("updateEventDate").value = eventDate;

      const form = document.getElementById("UpdateEventForm");
      form.action = `/update-events/${eventId}`;

      updateEventModal.style.display = "block";
    });
  });

  closeUpdateEventModal.addEventListener("click", () => {
    updateEventModal.style.display = "none";
  });

  const updateAssignmentModal = document.getElementById(
    "UpdateAssignmentModal",
  );
  const closeUpdateAssignmentModal =
    updateAssignmentModal.querySelector(".close");
  const updateAssignmentButtons = document.querySelectorAll(
    ".update-assignment-button",
  );

  updateAssignmentButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const assignmentId = btn.getAttribute("data-id");
      const assignmentName = btn.getAttribute("data-name");
      const assignmentDate = btn.getAttribute("data-date");

      document.getElementById("updateAssignmentName").value = assignmentName;
      document.getElementById("updateAssignmentDate").value = assignmentDate;

      const form = document.getElementById("UpdateAssignmentForm");
      form.action = `/update-assignments/${assignmentId}`;

      updateAssignmentModal.style.display = "block";
    });
  });

  closeUpdateAssignmentModal.addEventListener("click", () => {
    updateAssignmentModal.style.display = "none";
  });

  window.addEventListener("click", (e) => {
    if (e.target === addAssignmentModal) {
      addAssignmentModal.style.display = "none";
    }
    if (e.target === addEventModal) {
      addEventModal.style.display = "none";
    }
    if (e.target === updateEventModal) {
      updateEventModal.style.display = "none";
    }
    if (e.target === updateAssignmentModal) {
      updateAssignmentModal.style.display = "none";
    }
  });
});
