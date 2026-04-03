const form = document.getElementById("sign-up-form")
const erorr_message = document.getElementById("form-error")

if (form && erorr_message) {
    form.addEventListener("submit", async (e) => {
        e.preventDefault()

        erorr_message.textContent = ""
        erorr_message.classList.add("hidden")

        const formdata = new FormData(form)

        try {
            const response = await fetch("/sign_up", {
                method: "POST",
                body: formdata
            })

            const data = await response.json()

            if (data.success === false) {
                erorr_message.textContent = data.error || "you did something wrong"
                erorr_message.classList.remove("hidden")
                return
            }

            if (data.success === true) {
                window.location.href = data.redirect
            }
        } catch (error) {
            erorr_message.textContent = "unable to reach the servers right now"
            erorr_message.classList.remove("hidden")
        }
    })
}