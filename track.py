import re
import pandas as pd
import joblib
import socket  # For getting IP address of domain
from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Sample dataset
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
]

df = pd.DataFrame(DATASET, columns=["url", "label"])

# Feature Extraction Function
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

# Convert URL data into features
X = pd.DataFrame(df["url"].apply(lambda url: extract_features(url)).tolist())
y = df["label"]

# Split data into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "malicious_url_model.pkl")

def get_ip_address(url):
    """Extracts IP address of the domain in the given URL."""
    try:
        domain = re.sub(r"https?://", "", url)  # Remove 'http://' or 'https://'
        domain = domain.split("/")[0]  # Get the domain name
        ip_address = socket.gethostbyname(domain)  # Get IP address
        return ip_address
    except Exception:
        return "Unable to resolve IP"

def predict_url(url):
    """Predicts if a URL is malicious or safe and gets the IP address."""
    features = extract_features(url)
    model = joblib.load("malicious_url_model.pkl")
    prediction = model.predict(pd.DataFrame([features]))[0]
    ip_address = get_ip_address(url)

    result = "⚠️ WARNING: Malicious URL!" if prediction == 1 else "✅ Safe URL."
    return f"{result}\nDomain IP Address: {ip_address}"

# Get user input
if __name__ == "__main__":
    url = input("Enter a URL to check: ")
    print(predict_url(url))
