form = document.getElementById("sign-up-form")
erorr_message = document.getElementById("form-error")

form.addEventListener("submit", async (e) => {
    e.preventDefault()

    erorr_message.classList.add("hidden")

    const formData = new FormData(form)

    try {

        const response = await fetch("/handle_login", {
            method: "POST",
            body: formData
        })

        const data = await response.json()

        if (data.success === false) {
            erorr_message.textContent = data.error || "an error happend"
            erorr_message.classList.remove("hidden")
        } else {
            window.location.href = data.redirect
        }

    } catch (error) {
        erorr_message.textContent = "An error happend during connecting to the servers"
        erorr_message.classList.remove("hidden")
    }
})