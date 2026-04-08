const chat_message = document.getElementById("chat-messages")
const userQuestion = document.getElementById("question")
const form = document.getElementById("assistant-form")

userQuestion.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault()
        form.dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }))
    }
})

function addAiMeassge(message) {
    const wrapper = document.createElement("div")
    wrapper.className = "flex justify-start"

    const bubble = document.createElement("div")
    bubble.className = "max-w-[70%] rounded-2xl rounded-bl-md bg-white text-slate-900 px-4 py-3 shadow-sm border border-gray-200"
    bubble.textContent = message

    wrapper.appendChild(bubble)
    chat_message.appendChild(wrapper)
}

function addUserMessage(message) {
    const wrapper = document.createElement("div")
    wrapper.className = "flex justify-end"

    const bubble = document.createElement("div")
    bubble.className = "max-w-[70%] rounded-2xl rounded-br-md bg-black text-white px-4 py-3"
    bubble.textContent = message

    wrapper.appendChild(bubble)
    chat_message.appendChild(wrapper)
}


form.addEventListener("submit", async (e) => {

    e.preventDefault()

    const question = userQuestion.value.trim()
    if (!question) {
        return
    }

    addUserMessage(question)

    const formData = new FormData(form)


    const response = await fetch("/assistant/chat", {
        method: "POST",
        body: formData
    })

    const data = await response.json()

    addAiMeassge(data.reply)

    chat_message.scrollTop = chat_message.scrollHeight
    userQuestion.value = ""
    userQuestion.style.height = "60px"
})
