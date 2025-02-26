from flask import Flask, request, jsonify
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

responses = {
    "hello": "Hi there! Welcome to THREADSCOPE. How can I assist you?",
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

if __name__ == '__main__':
    app.run(debug=True)
