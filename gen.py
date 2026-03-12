<!DOCTYPE html>
<html>
<head>
    <title>Hits Link Generator</title>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>

    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 40px auto;
            padding: 20px;
        }
        input, button {
            padding: 10px;
            font-size: 1rem;
        }
        #output {
            margin-top: 20px;
            padding: 10px;
            background: #f3f3f3;
            border-radius: 6px;
            white-space: pre-wrap;
        }
    </style>
</head>

<body>
    <h1>Hits Link Generator</h1>

    <input id="url-input" placeholder="Enter URL" style="width: 70%">
    <button id="generate-btn">Generate</button>

    <pre id="output"></pre>

    <py-config>
        files = ["gen.py"]
    </py-config>

    <py-script>
from pyscript import Element
from gen import generate_link
from js import navigator

def run_generator(event=None):
    url = Element("url-input").value.strip()
    output = Element("output")

    if not url:
        output.write("Please enter a URL.")
        return

    result = generate_link(url)
    output.write(result)

    # Copy to clipboard
    navigator.clipboard.writeText(result)

# Bind button click
Element("generate-btn").element.onclick = run_generator
    </py-script>
</body>
</html>
