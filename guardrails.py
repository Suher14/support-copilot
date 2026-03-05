def check_guardrails(user_input: str):
    text = user_input.lower()

    # Sensitive credentials / payment details
    sensitive_terms = [
        "password", "passcode", "2fa", "otp", "one-time code", "backup code",
        "api key", "token", "secret",
        "credit card", "card number", "cvv"
    ]

    # Only block if the user appears to be sharing sensitive info
    share_intent_terms = [
        "my password is", "here is my password", "password is",
        "my otp is", "otp is", "code is", "2fa code is",
        "my api key is", "api key is", "token is",
        "cvv is", "card number is"
    ]

    if any(t in text for t in sensitive_terms) and any(s in text for s in share_intent_terms):
        return (
            "For security reasons, please do not share passwords, 2FA/OTP codes, API keys/tokens, "
            "or card details. Use the official account recovery or billing process.\n"
            "If you describe the issue without sensitive details, I can help safely."
        )

    # De-escalation for rude language (simple)
    if any(word in text for word in ["stupid", "idiot", "useless", "worst", "unacceptable"]):
        return (
            "I understand this is frustrating. I’m here to help. "
            "Please describe the issue and I will guide you with the next steps."
        )

    return None