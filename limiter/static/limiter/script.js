const button = document.getElementById("sendRequest");

const statusElement = document.getElementById("status");
const remainingElement = document.getElementById("remaining");

const responseBox = document.getElementById("responseBox");

const retryContainer = document.getElementById("retryContainer");
const retryAfterElement = document.getElementById("retryAfter");


button.addEventListener("click", async () => {

    button.disabled = true;

    statusElement.textContent = "Sending...";

    retryContainer.classList.add("hidden");

    try {

        const response = await fetch("/api/");

        const data = await response.json();

        responseBox.textContent =
            JSON.stringify(data, null, 2);

        remainingElement.textContent =
            data.remaining;

        if (response.status === 429) {

            statusElement.textContent =
                "Rate Limited";

            retryContainer.classList.remove("hidden");

            retryAfterElement.textContent =
                data.retry_after;

            startRetryTimer(data.retry_after);

        } else {

            statusElement.textContent =
                "Success";

            button.disabled = false;
        }

    } catch (error) {

        statusElement.textContent =
            "Error";

        responseBox.textContent =
            error.toString();

        button.disabled = false;
    }
});


function startRetryTimer(seconds) {

    let remaining = seconds;

    retryAfterElement.textContent = remaining;

    const timer = setInterval(() => {

        remaining--;

        retryAfterElement.textContent = remaining;

        if (remaining <= 0) {

            clearInterval(timer);

            retryContainer.classList.add("hidden");

            statusElement.textContent =
                "Ready";

            button.disabled = false;
        }

    }, 1000);
}