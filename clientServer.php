<?php
header("Access-Control-Allow-Origin: *");

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['url'])) {
        $site = $_POST['url'];

        // Run Python script for analysis
        $python_path = "C:\Users\HP\AppData\Local\Microsoft\WindowsApps\python.exe"; // Path to Python 2.x interpreter
        $decision = exec("$python_path test.py $site 2>&1 ");

        // Output the decision
        echo $decision;
    } else {
        // 'url' parameter not found in the POST request
        echo "Error: 'url' parameter not found in POST request.";
    }
} else {
    // Not a POST request
    echo "Error: Only POST requests are allowed.";
}
?>
