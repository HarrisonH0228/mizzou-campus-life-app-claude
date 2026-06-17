const form = document.getElementById("chat-form");
const input = document.getElementById("chat-input");
const thread = document.getElementById("chat-thread");

let history = [];

function appendMessage(role, text, isTyping = false) {
  const msg = document.createElement("div");
  msg.className = `message ${role}`;
  const bubble = document.createElement("span");
  bubble.className = isTyping ? "bubble typing" : "bubble";
  if (role === "assistant" && !isTyping) {
    bubble.innerHTML = DOMPurify.sanitize(marked.parse(text));
  } else {
    bubble.textContent = text;
  }
  msg.appendChild(bubble);
  thread.appendChild(msg);
  thread.scrollTop = thread.scrollHeight;
  return bubble;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const userText = input.value.trim();
  if (!userText) return;

  appendMessage("user", userText);
  input.value = "";
  input.disabled = true;

  const typingBubble = appendMessage("assistant", "Thinking…", true);

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userText, history }),
    });

    if (!res.ok) {
      throw new Error(`Server error: ${res.status}`);
    }

    const data = await res.json();
    typingBubble.innerHTML = DOMPurify.sanitize(marked.parse(data.reply));
    typingBubble.classList.remove("typing");

    history.push({ role: "user", content: userText });
    history.push({ role: "assistant", content: data.reply });
  } catch (err) {
    typingBubble.textContent = "Sorry, something went wrong. Please try again.";
    typingBubble.classList.remove("typing");
  } finally {
    input.disabled = false;
    input.focus();
  }
});
