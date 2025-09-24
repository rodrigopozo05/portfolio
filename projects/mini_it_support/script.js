document.getElementById("ticketForm").addEventListener("submit", function(e) {
    e.preventDefault();
    
    const ticket = {
        id: Date.now(),
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        subject: document.getElementById("subject").value,
        description: document.getElementById("description").value,
        status: "Pending"
    };
    
    let tickets = JSON.parse(localStorage.getItem("tickets")) || [];
    tickets.push(ticket);
    localStorage.setItem("tickets", JSON.stringify(tickets));
    
    document.getElementById("message").innerText = "Ticket submitted successfully!";
    document.getElementById("ticketForm").reset();
});
