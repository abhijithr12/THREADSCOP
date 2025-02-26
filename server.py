import os
import re
import socket
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

try:
    model = joblib.load("malicious_url_model.pkl")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None  
    DATASET = [
    ("https://google.com", 0),
    ("http://malicious-site.com", 1),
    ("https://facebook.com", 0),
    ("http://free-money.xyz", 1),
    ("http://123.45.67.89/login", 1),
    ("https://github.com", 0),
    ("http://verify-account.net", 1),
    ("http://click-here-win.com", 1),
    ("https://youtube.com", 0),
    ("http://phishing-example.net", 1),
    ("https://amazon.com", 0),
    ("https://microsoft.com", 0),
    ("https://apple.com", 0),
    ("https://netflix.com", 0),
    ("https://linkedin.com", 0),
    ("https://twitter.com", 0),
    ("https://instagram.com", 0),
    ("https://adobe.com", 0),
    ("https://spotify.com", 0),
    ("https://dropbox.com", 0),
    ("https://paypal.com", 0),
    ("https://wikipedia.org", 0),
    ("https://bbc.com", 0),
    ("https://cnn.com", 0),
    ("https://nytimes.com", 0),
    ("https://forbes.com", 0),
    ("https://bloomberg.com", 0),
    ("https://nasa.gov", 0),
    ("https://who.int", 0),
    ("https://cdc.gov", 0),
    ("https://whitehouse.gov", 0),
    ("https://harvard.edu", 0),
    ("https://stanford.edu", 0),
    ("https://mit.edu", 0),
    ("https://yale.edu", 0),
    ("https://princeton.edu", 0),
    ("https://berkeley.edu", 0),
    ("https://ox.ac.uk", 0),
    ("https://cam.ac.uk", 0),
    ("https://coursera.org", 0),
    ("https://udemy.com", 0),
    ("https://khanacademy.org", 0),
    ("https://medium.com", 0),
    ("https://quora.com", 0),
    ("https://reddit.com", 0),
    ("https://stackoverflow.com", 0),
    ("https://github.io", 0),
    ("https://gitlab.com", 0),
    ("https://bitbucket.org", 0),
    ("https://cloudflare.com", 0),
    ("https://mozilla.org", 0),
    ("https://ubuntu.com", 0),
    ("https://debian.org", 0),
    ("https://centos.org", 0),
    ("https://python.org", 0),
    ("https://java.com", 0),
    ("https://php.net", 0),
    ("https://nodejs.org", 0),
    ("https://golang.org", 0),
    ("https://rust-lang.org", 0),
    ("https://tensorflow.org", 0),
    ("https://pytorch.org", 0),
    ("https://keras.io", 0),
    ("https://scikit-learn.org", 0),
    ("https://opencv.org", 0),
    ("https://numpy.org", 0),
    ("https://pandas.pydata.org", 0),
    ("https://matplotlib.org", 0),
    ("https://jupyter.org", 0),
    ("https://fastapi.tiangolo.com", 0),
    ("https://flask.palletsprojects.com", 0),
    ("https://expressjs.com", 0),
    ("https://spring.io", 0),
    ("https://hibernate.org", 0),
    ("https://postgresql.org", 0),
    ("https://mysql.com", 0),
    ("https://mariadb.org", 0),
    ("https://mongodb.com", 0),
    ("https://redis.io", 0),
    ("https://elastic.co", 0),
    ("https://apache.org", 0),
    ("https://nginx.org", 0),
    ("https://docker.com", 0),
    ("https://kubernetes.io", 0),
    ("https://prometheus.io", 0),
    ("https://grafana.com", 0),
    ("https://jenkins.io", 0),
    ("https://circleci.com", 0),
    ("https://travis-ci.com", 0),
    ("https://ansible.com", 0),
    ("https://terraform.io", 0),
    ("https://hashicorp.com", 0),
    ("https://digitalocean.com", 0),
    ("https://aws.amazon.com", 0),
    ("https://azure.microsoft.com", 0),
    ("https://cloud.google.com", 0),
    ("https://ibm.com/cloud", 0),
    ("https://oracle.com/cloud", 0),
    ("https://sap.com", 0),
    ("https://salesforce.com", 0),
    ("https://zoho.com", 0),
    ("https://hubspot.com", 0),
    ("https://mailchimp.com", 0),
    ("https://stripe.com", 0),
    ("https://squareup.com", 0),
    ("https://shopify.com", 0),
    ("https://bigcommerce.com", 0),
    ("https://wix.com", 0),
    ("https://wordpress.org", 0),
    ("https://joomla.org", 0),
    ("https://drupal.org", 0),
    ("https://moodle.org", 0),
]
malicious_links = [
    ("http://free-gift-cards.xyz", 1),
    ("http://claim-your-prize-now.com", 1),
    ("http://bank-secure-login.net", 1),
    ("http://password-reset-alert.com", 1),
    ("http://urgent-security-warning.com", 1),
    ("http://download-latest-software-free.com", 1),
    ("http://cheap-discount-medications.com", 1),
    ("http://click-here-to-win.com", 1),
    ("http://verify-your-paypal-account.net", 1),
    ("http://confirm-your-identity.com", 1),
    ("http://update-your-banking-info.net", 1),
    ("http://earn-money-fast-online.com", 1),
    ("http://bitcoin-doubling-service.com", 1),
    ("http://get-rich-quick-now.com", 1),
    ("http://install-latest-antivirus.com", 1),
    ("http://access-restricted-content.com", 1),
    ("http://your-device-is-infected-alert.com", 1),
    ("http://hacked-account-recovery.com", 1),
    ("http://email-login-verification.com", 1),
    ("http://win-a-brand-new-car.com", 1),
    ("http://socialmedia-security-alert.net", 1),
    ("http://credit-card-verification.net", 1),
    ("http://track-your-package-now.com", 1),
    ("http://exclusive-offer-just-for-you.com", 1),
    ("http://free-premium-subscription.com", 1),
    ("http://urgent-action-required.net", 1),
    ("http://unlock-restricted-account.com", 1),
    ("http://fake-tech-support.net", 1),
    ("http://vpn-unblock-premium.com", 1),
    ("http://instant-loan-approval.com", 1),
    ("http://verify-payment-details.net", 1),
    ("http://you-won-a-lottery.com", 1),
    ("http://fake-covid19-vaccine.com", 1),
    ("http://free-money-transfer.com", 1),
    ("http://casino-free-spins-bonus.com", 1),
    ("http://paypal-security-check.com", 1),
    ("http://facebook-2fa-login.com", 1),
    ("http://amazon-gift-card-claim.com", 1),
    ("http://microsoft-support-alert.com", 1),
    ("http://google-drive-shared-file.com", 1),
    ("http://your-email-password-reset.com", 1),
    ("http://urgent-billing-issue.com", 1),
    ("http://unblock-your-instagram-account.com", 1),
    ("http://fake-crypto-investment.com", 1),
    ("http://secure-your-apple-id.com", 1),
    ("http://linkedin-security-warning.com", 1),
    ("http://netflix-login-authentication.com", 1),
    ("http://your-amazon-order-update.com", 1),
    ("http://zoom-meeting-invitation.com", 1),
    ("http://suspicious-login-alert.com", 1),
    ("http://microsoft-urgent-update.com", 1),
    ("http://fake-government-refund.com", 1),
    ("http://youtube-premium-free.com", 1),
    ("http://download-free-movies.com", 1),
    ("http://android-system-update.net", 1),
    ("http://iphone-software-update-alert.com", 1),
    ("http://malicious-app-download.com", 1),
    ("http://bitcoin-trading-bot.net", 1),
    ("http://amazon-customer-support.net", 1),
    ("http://steam-account-hacked.com", 1),
    ("http://fake-telegram-verification.com", 1),
    ("http://dropbox-shared-document.com", 1),
    ("http://earn-crypto-fast.com", 1),
    ("http://instagram-verification-alert.com", 1),
    ("http://verify-your-google-account.com", 1),
    ("http://your-device-has-been-infected.com", 1),
    ("http://urgent-macbook-security-update.com", 1),
    ("http://hack-facebook-account.com", 1),
    ("http://paypal-login-confirmation.com", 1),
    ("http://telegram-reward-claim.com", 1),
    ("http://itunes-gift-card-promo.com", 1),
    ("http://redeem-your-reward-now.com", 1),
    ("http://amazon-prime-activation.com", 1),
    ("http://apple-id-billing-error.com", 1),
    ("http://government-urgent-message.com", 1),
    ("http://fake-bitcoin-airdrop.com", 1),
    ("http://your-credit-score-is-low.com", 1),
    ("http://get-cheap-flight-deals.com", 1),
    ("http://prize-reward-center.com", 1),
    ("http://hacked-twitter-alert.com", 1),
    ("http://download-premium-games-free.com", 1),
    ("http://microsoft-windows-security-alert.com", 1),
    ("http://ios-device-infected.com", 1),
    ("http://facebook-has-locked-your-account.com", 1),
    ("http://recover-your-suspended-email.com", 1),
    ("http://steam-gift-card-claim.com", 1),
    ("http://unlock-your-crypto-wallet.com", 1),
    ("http://telegram-group-invitation.com", 1),
    ("http://urgent-apple-device-update.com", 1),
    ("http://your-paypal-balance-is-low.com", 1),
    ("http://iphone-has-been-locked.com", 1),
    ("http://claim-your-bitcoin-reward.com", 1),
    ("http://fake-financial-advisor.com", 1),
    ("http://youtube-monetization-scam.com", 1),
    ("http://download-hacked-apps.com", 1),
    ("http://fake-antivirus-alert.com", 1),
    ("http://urgent-business-loan-approval.com", 1),
    ("http://investment-scheme-fast-returns.com", 1),
    ("http://sign-in-to-reactivate-your-account.com", 1),
    ("http://claim-your-unclaimed-funds.com", 1),
    ("http://crypto-wallet-password-reset.com", 1),
    ("http://play-free-casino-games.com", 1),
    ("http://click-here-to-see-private-photos.com", 1),
    ("http://update-your-email-password.com", 1),
    ("http://earn-passive-income-fast.com", 1),
    ("http://paypal-account-fraud-alert.com", 1),
    ("http://your-tax-refund-is-ready.com", 1),
    ("http://free-gaming-skins.com", 1),
    ("http://amazon-prime-verification.com", 1),
    ("http://fake-crypto-mining-platform.com", 1),
    ("http://bitcoin-giveaway-now.com", 1),
    ("http://microsoft-account-authentication.com", 1),
    ("http://secure-your-twitter-account-now.com", 1),
    ("http://your-email-is-about-to-be-deactivated.com", 1),
    ("http://telegram-premium-free.com", 1),
    ("http://latest-movie-streaming-free.com", 1),
    ("http://claim-your-reward-points-now.com", 1),
    ("http://your-paypal-account-is-restricted.com", 1),
    ("http://verify-your-amazon-delivery.com", 1),
    ("http://download-best-vpn-free.com", 1),
    ("https://secure.paypal.com.verify-login.malicious-site.com",1)
]

def extract_features(url):
    """Extracts numerical features from URLs for AI model."""
    return {
        "url_length": len(url),
        "has_https": 1 if url.startswith("https") else 0,
        "has_ip": 1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0,
        "num_digits": sum(c.isdigit() for c in url),
        "num_special_chars": sum(c in "!@#$%^&*()-_=+" for c in url),
        "num_hyphens": url.count("-"),
    }

def get_ip_address(url):
    """Extracts IP address of the domain in the given URL."""
    try:
        domain = re.sub(r"https?://", "", url).split("/")[0]  # Extract domain
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except Exception:
        return "Unable to resolve IP"

@app.route("/predict", methods=["POST"])
def predict_url():
    """Receives a URL, predicts its safety, and retrieves the domain's IP address."""
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    if model is None:
        return jsonify({"error": "Model not available"}), 500

    features = extract_features(url)
    prediction = model.predict(pd.DataFrame([features]))[0]
    ip_address = get_ip_address(url)

    return jsonify({
        "status": "malicious" if prediction == 1 else "safe",
        "ip_address": ip_address
    })



responses = {
    "hello": "Hi there! Welcome to THREADSCOPE. How can I assist you?",
    "hi": "Hi there! Welcome to THREADSCOPE. How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a nice day and stay safe online!",
    "what is threadscope": "THREADSCOPE is a platform for AI-based malware detection discussions and community engagement.",
    "how does threadscope work": "THREADSCOPE analyzes URLs and files for potential malicious activity using AI-powered detection techniques.",
    "is threadscope free to use": "Yes! THREADSCOPE offers free malware detection and a community forum for discussions.",
    "default": "I'm not sure how to respond to that. Try asking something related to THREADSCOPE!","hello": "Hi there! Welcome to THREADSCOPE. How can I assist you?",
    "hi": "Hi there! Welcome to THREADSCOPE. How can I assist you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a nice day and stay safe online!",
    "what is threadscope": "THREADSCOPE is a platform for AI-based malware detection discussions and community engagement.",
    "how does threadscope work": "THREADSCOPE analyzes URLs and files for potential malicious activity using AI-powered detection techniques.",
    "is threadscope free to use": "Yes! THREADSCOPE offers free malware detection and a community forum for discussions.",
    "how can i detect malicious urls": "You can use THREADSCOPE’s AI-powered detection tool to analyze URLs and identify potential threats.",
    "can i discuss malware analysis here": "Absolutely! THREADSCOPE has a community where users discuss AI-based malware detection and cybersecurity topics.",
    "how accurate is threadscope's ai detection": "THREADSCOPE’s AI model is trained on various threats, providing high accuracy in detecting malicious URLs.",
    "do i need an account to use threadscope": "Some features, like posting in the community, require an account, but URL scanning is available without one.",
    "how can i contribute to threadscope": "You can contribute by engaging in community discussions, sharing knowledge, and helping improve AI threat detection.",
    "what should i do if a website is flagged as malicious": "If THREADSCOPE detects a malicious website, avoid visiting it and consider reporting it to relevant authorities.",
    "does threadscope have an ai chatbot": "Yes! THREADSCOPE includes an AI chatbot to answer questions about malware detection and security topics.",
    "can i trust threadscope's scan results": "THREADSCOPE uses AI-driven analysis, but always double-check results with multiple security tools for complete safety.",
    "is there a way to report false positives": "Yes! If you believe a URL was wrongly flagged, you can report it for review in our community forum.",
    "who created threadscope": "THREADSCOPE was created to help users detect and discuss online threats using AI-driven solutions.",
    "what kind of threats can threadscope detect": "THREADSCOPE can detect phishing, malware, suspicious scripts, and other cybersecurity threats in URLs.",
    "default": "I'm not sure how to respond to that. Try asking something related to THREADSCOPE!",
    "what is your name": "I'm SUNI MWON!",
    "default": "I'm not sure how to respond to that. Try asking something else!","what is cybersecurity": "Cybersecurity is the practice of protecting systems, networks, and data from cyber threats.",
    "why is cybersecurity important": "Cybersecurity is crucial to prevent data breaches, identity theft, and other cyber threats that can harm individuals and businesses.",
    "what are the types of cyber attacks": "Common cyber attacks include phishing, malware, ransomware, DDoS attacks, and social engineering.",
    "what is phishing": "Phishing is a cyber attack where hackers trick individuals into providing sensitive information, usually through fake emails or websites.",
    "how can i protect my password": "Use a strong password with a mix of letters, numbers, and symbols. Enable two-factor authentication (2FA) for extra security.",
    "what is two factor authentication": "Two-factor authentication (2FA) adds an extra layer of security by requiring a second form of verification, like a text message code.",
    "what is malware": "Malware is malicious software designed to harm or exploit computers, networks, or users. Examples include viruses, worms, and trojans.",
    "how can i detect malware": "Look for slow performance, unexpected pop-ups, unauthorized changes, or unknown software installed on your device.",
    "what should i do if my computer is infected": "Disconnect from the internet, run a security scan, remove suspicious files, and consider reinstalling your OS if needed.",
    "what is ransomware": "Ransomware is malware that encrypts your files and demands payment to restore access. Avoid paying and seek professional help.",
    "how can i prevent ransomware attacks": "Keep software updated, avoid suspicious links, use strong passwords, and back up your data regularly.",
    "what is social engineering": "Social engineering is a tactic hackers use to manipulate people into revealing confidential information, often by pretending to be trustworthy.",
    "how does a firewall work": "A firewall monitors and filters incoming and outgoing network traffic to block unauthorized access and cyber threats.",
    "what is a vpn": "A VPN (Virtual Private Network) encrypts your internet connection, keeping your data private and secure from hackers and surveillance.",
    "is public wi fi safe": "Public Wi-Fi is risky because hackers can intercept data. Use a VPN or avoid entering sensitive information while connected.",
    "what is ethical hacking": "Ethical hacking is legally testing a system’s security to find and fix vulnerabilities before malicious hackers exploit them.",
    "what are strong password practices": "Use long, unique passwords with uppercase, lowercase, numbers, and symbols. Avoid personal details and update regularly.",
    "how do i recognize a fake website": "Check for HTTPS, look for spelling errors, verify the URL, and avoid entering sensitive data on suspicious sites.",
    "what is a ddos attack": "A DDoS (Distributed Denial of Service) attack floods a website or network with traffic, causing it to crash or become unavailable.",
    "what is encryption": "Encryption is the process of converting data into unreadable code to protect it from unauthorized access.",
    "how do i secure my email": "Use a strong password, enable 2FA, be cautious of phishing emails, and never share your login credentials.",
    "what is a botnet": "A botnet is a network of infected devices controlled by hackers to launch cyber attacks like DDoS or spam campaigns.",
    "what is a trojan virus": "A Trojan is malware disguised as legitimate software that, once installed, can steal data or harm your system.",
    "how can i protect my smartphone": "Use strong passwords, keep your software updated, avoid suspicious apps, and enable remote wipe in case of loss.",
    "what is spyware": "Spyware is malicious software that secretly collects user information, such as keystrokes and browsing activity, without consent.",
    "how often should i update my software": "Regularly! Keeping software updated ensures security patches fix vulnerabilities before hackers can exploit them.",
    "default": "I'm not sure how to respond to that. Try asking something else!",

}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()
    bot_response = responses.get(user_message, responses["default"])
    return jsonify({"reply": bot_response})


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, nullable=True)  


if not os.path.exists("community.db"):
    with app.app_context():
        db.create_all()

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    posts_data = [{
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "date_posted": post.date_posted.strftime("%Y-%m-%d %H:%M:%S"),
        "user_id": post.user_id
    } for post in posts]
    return jsonify(posts_data)

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    if not data.get("title") or not data.get("content"):
        return jsonify({"error": "Title and content are required"}), 400
    
    new_post = Post(
        title=data["title"],
        content=data["content"],
        user_id=data.get("user_id")  
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post added successfully"}), 201



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
