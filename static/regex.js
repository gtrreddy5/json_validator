function getFlags() {
    let flags = "";
    if (document.getElementById("flagG").checked) flags += "g";
    if (document.getElementById("flagI").checked) flags += "i";
    if (document.getElementById("flagM").checked) flags += "m";
    return flags;
}

function runRegex() {
    const pattern = document.getElementById("regexInput").value;
    const text = document.getElementById("testString").value;
    const matchInfo = document.getElementById("matchInfo");
    const explain = document.getElementById("regexExplain");
    const count = document.getElementById("matchCount");

    matchInfo.innerHTML = "";
    explain.innerHTML = "";

    if (!pattern) {
        count.textContent = "0 matches";
        return;
    }

    let regex;
    try {
        regex = new RegExp(pattern, getFlags());
    } catch (e) {
        matchInfo.innerHTML = `<span class="error">${e.message}</span>`;
        return;
    }

    let matches = [...text.matchAll(regex)];
    count.textContent = `${matches.length} matches`;

    if (matches.length === 0) {
        matchInfo.innerHTML = "No matches found";
    }

    matches.forEach((m, idx) => {
        let groups = "";
        if (m.length > 1) {
            for (let i = 1; i < m.length; i++) {
                groups += `<div class="group">Group ${i}: ${m[i]}</div>`;
            }
        }

        matchInfo.innerHTML += `
            <div class="match-block">
                <strong>Match ${idx + 1}:</strong> "${m[0]}"
                ${groups}
            </div>
        `;
    });

    explainRegex(pattern);
}

function explainRegex(regex) {
    const explain = document.getElementById("regexExplain");

    const rules = [
        [/\\d/, "Matches any digit (0–9)"],
        [/\\w/, "Matches any word character (a–z, A–Z, 0–9, _)"],
        [/\[.*?\]/, "Character class – matches any one character inside"],
        [/\+/, "Matches one or more of the previous token"],
        [/\*/, "Matches zero or more of the previous token"],
        [/\?/, "Makes previous token optional"],
        [/\./, "Matches any character except newline"],
        [/\^/, "Start of string"],
        [/\$/, "End of string"],
        [/\(\)/, "Capturing group"]
    ];

    let html = `<ul>`;
    rules.forEach(([r, text]) => {
        if (r.test(regex)) html += `<li>${text}</li>`;
    });
    html += `</ul>`;

    explain.innerHTML = html || "No explanation available";
}

function copyRegex() {
    const flags = getFlags();
    const pattern = document.getElementById("regexInput").value;
    const full = `/${pattern}/${flags}`;
    navigator.clipboard.writeText(full);
    alert("Regex copied!");
}
