document.addEventListener("DOMContentLoaded", function () {
    const chatForm = document.getElementById("chat-form");
    const messageInput = document.getElementById("message");
    const responseOutput = document.getElementById("response");

    chatForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const userMessage = messageInput.value;

        if (!userMessage) {
            alert("Please enter a message!");
            return;
        }

        // Display user message in the chatbox
        const chatBox = document.getElementById("chat-box");
        chatBox.innerHTML += `<p>User: ${userMessage}</p>`;

        // Send the user message to the backend
        try {
            const res = await fetch("http://127.0.0.1:8000/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: userMessage }),
            });

            const data = await res.json();
            if (data.reply) {
                chatBox.innerHTML += `<p>AI: ${data.reply}</p>`;
            } else {
                chatBox.innerHTML += `<p>Error: ${data.error}</p>`;
            }
        } catch (error) {
            console.error("Error:", error);
            responseOutput.textContent = "Error: Unable to get a response from the backend.";
        }

        messageInput.value = "";
    });
});
