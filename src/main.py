from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>FastAPI Test Page</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 2rem;
                    text-align: center;
                }
                .status {
                    color: #22c55e;
                    font-size: 1.5rem;
                    margin: 2rem 0;
                }
            </style>
        </head>
        <body>
            <h1>FastAPI Test Page</h1>
            <div class="status">✅ Server is running successfully!</div>
            <p>This is a simple test page to confirm that your FastAPI server is working correctly.</p>
        </body>
    </html>
    """
    return html_content
