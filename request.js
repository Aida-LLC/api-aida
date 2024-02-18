var xhr = new XMLHttpRequest();
var url = "http://143.198.232.28/gemini_api";
var body = JSON.stringify(
    {
        "prompt": "Write logbook entries in concise, past-tense sentences that provide clear and detailed descriptions of each day's activities, focusing on what was accomplished, learned, and experienced during the practical training. Maintain a formal and professional tone, using technical terminology as needed to accurately convey the tasks, tools, and outcomes. Ensure entries are organized chronologically, emphasizing the educational aspects of the training while also highlighting the practical outcomes achieved based on this week summary We started with sketches on Monday, turned them into digital prototypes by Tuesday, refined the designs throughout the week, tested everything on Thursday, and by Friday, we had a polished prototype ready for evaluation. Collaboration and smart use of design tools made the process smooth. the output should be in python dictionary with { day: entry } format"
    }
);

xhr.open("POST", url, true);
xhr.setRequestHeader("Content-Type", "application/json");

xhr.onreadystatechange = function () {
if (xhr.readyState === 4 && xhr.status === 200) {
    // Handle the successful response here
    console.log(xhr.responseText);
}
};

xhr.send(body);