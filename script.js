function generateEmail() {
    var companyName = document.getElementById("companyName").value;
    var textBefore = document.getElementById("textBefore").value;
    var domain = document.getElementById("domainSelect").value;

    // Generate email address
    var email = textBefore + "@" + companyName + "." + domain;

    // Display the generated email address
    document.getElementById("result").value = email;
    println("Generated email: " + email);
}
function processCSV() {
    var fileInput = document.getElementById('csvFileInput');
    var file = fileInput.files[0];
    var domainSelect = document.getElementById('domainSelect');
    var selectedDomains = Array.from(domainSelect.selectedOptions).map(option => option.value);
    var textBefore = document.getElementById('textBefore').value;

    if (file) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var contents = e.target.result;
            var lines = contents.split('\n');
            lines.forEach(function(line) {
                var companyName = line.trim().split(',')[0]; // Assuming company name is the first column
                selectedDomains.forEach(function(domain) {
                    var email = textBefore + "@" + companyName + "." + domain;
                    console.log(email);
                });
            });
        };
        reader.readAsText(file);
    } else {
        console.error('No file selected');
    }
}

function processFile() {
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];

    if (file) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var contents = e.target.result;
            var rows = contents.split('\n').slice(0, 10); // Limit to 10 rows
            rows.forEach(function(row) {
                // Process each row (e.g., extract names)
                console.log(row);
            });
        };
        reader.readAsText(file);
    } else {
        console.error('No file selected');
    }
}
