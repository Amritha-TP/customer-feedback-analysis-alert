async function analyzeFeedback() {

    const feedback =
        document.getElementById("feedback").value.trim();

    const button =
        document.getElementById("analyzeButton");

    const result =
        document.getElementById("result");

    const sentiment =
        document.getElementById("sentiment");

    const telegram =
        document.getElementById("telegram");


    // ------------------------------------------
    // Validate input
    // ------------------------------------------

    if (!feedback) {

        alert("Please enter customer feedback.");

        return;
    }


    // ------------------------------------------
    // Disable button while processing
    // ------------------------------------------

    button.disabled = true;

    button.innerText = "Analyzing...";


    try {

        // --------------------------------------
        // Send request to FastAPI
        // --------------------------------------

        const response = await fetch(
            "/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    text: feedback
                })
            }
        );


        // --------------------------------------
        // Check API response
        // --------------------------------------

        if (!response.ok) {

            throw new Error(
                "Prediction request failed"
            );
        }


        // --------------------------------------
        // Read JSON response
        // --------------------------------------

        const data =
            await response.json();


        console.log("API Response:", data);


        // --------------------------------------
        // Display result
        // --------------------------------------

        result.style.display = "block";

        result.className =
            data.sentiment;


        sentiment.innerText =
            "Sentiment: " +
            data.sentiment.toUpperCase();


        // --------------------------------------
        // Telegram status
        // --------------------------------------

        if (data.sentiment === "negative") {

            if (data.telegram_alert_sent) {

                telegram.innerText =
                    "🚨 Negative feedback sent to the business owner.";

            } else {

                telegram.innerText =
                    "⚠️ Negative feedback detected.";

            }

        } else {

            telegram.innerText = "";

        }

    }


    catch (error) {

        console.error(
            "Error:",
            error
        );


        result.style.display = "block";

        result.className = "negative";


        sentiment.innerText =
            "Unable to analyze feedback";


        telegram.innerText =
            "Please make sure the FastAPI server is running.";

    }


    finally {

        button.disabled = false;

        button.innerText =
            "Analyze Feedback";

    }

}