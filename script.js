function handleSubmit() {
    const text = document.getElementById("textInput").value;
    const pattern = document.getElementById("regexInput").value;
    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "";

    if (!text || !pattern) {
        resultDiv.innerHTML = "<p class='error'>Both fields are required.</p>";
        return;
    }

    try {
        const regex = new RegExp(pattern, "g");
        const matches = text.match(regex);

        if (matches && matches.length > 0) {
            let output = "<strong>Matched Strings:</strong><ul>";
            matches.forEach(match => {
                output += `<li>${match}</li>`;
            });
            output += "</ul>";
            resultDiv.innerHTML = output;
        } else {
            resultDiv.innerHTML = "<p>No matches found.</p>";
        }

    } catch (err) {
        resultDiv.innerHTML = "<p class='error'>Invalid regular expression.</p>";
    }
}
