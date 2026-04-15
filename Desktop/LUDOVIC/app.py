from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Docker Flask App</title>
        <style>
            * { margin:0; padding:0; box-sizing:border-box; }
            body {
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            .card {
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 20px;
                padding: 50px 60px;
                text-align: center;
                max-width: 580px;
                backdrop-filter: blur(12px);
            }
            .icon { font-size: 64px; margin-bottom: 20px; }
            h1 { font-size: 1.9rem; margin-bottom: 12px; color: #00d4ff; }
            p { font-size: 1.05rem; line-height: 1.8; opacity: 0.88; }
            .badge {
                display: inline-block;
                background: #00d4ff;
                color: #0f0c29;
                font-weight: bold;
                padding: 8px 22px;
                border-radius: 50px;
                margin-top: 24px;
                font-size: 0.9rem;
            }
            .footer { margin-top: 28px; font-size: 0.8rem; opacity: 0.5; }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="icon">🐳</div>
            <h1>Application Conteneurisée</h1>
            <p>Bonjour à tous ! Ceci est une application Flask
               déployée avec <strong>Docker</strong>.</p>
            <div class="badge">✅ Actif — par TONNOM</div>
            <div class="footer">Flask · Python 3.9 · Docker · CC1 M1</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)