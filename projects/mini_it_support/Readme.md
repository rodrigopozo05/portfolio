# Mini IT Support Desk
Project Overview

Mini IT Support Desk is a simple, interactive help desk/ticketing system built to showcase skills in IT support, technical problem-solving, and web development. Users can submit tickets for technical issues, and admins can manage these tickets directly through a dashboard.

This project is designed as a portfolio demonstration, emphasizing clean design, interactivity, and usability.

# Features

- User Side:

Submit a new ticket with:

Name

Email

Subject

Description of the problem

Tickets are stored locally in the browser using localStorage

Immediate confirmation after submission

- Admin Side (Dashboard):

View all tickets in a clean table

Change ticket status: Pending → In Progress → Resolved

Responsive design for mobile and desktop

Simple, interactive interface with hover effects and dropdowns for status

# Technologies Used

HTML5 – Markup for user and admin pages

CSS3 – Modern, clean, and responsive styling

JavaScript – Form handling, dashboard updates, and localStorage

localStorage – Temporary ticket storage without requiring a backend

# How to Run

Download or clone the repository.

Open index.html in your browser to submit tickets.

Open admin.html in your browser to view and manage tickets.

⚠️ Note: Currently, tickets are stored in localStorage, which means they will be lost if the browser is cleared or the project is closed.

# Future Improvements

Add SQLite or MySQL database for persistent storage of tickets

Integrate a backend (Python Flask / Node.js) to handle CRUD operations

Add user authentication for admin dashboard

Enable email notifications when a ticket is created or updated

Expand analytics and reporting for ticket trends