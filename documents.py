documents = [
    {
        "name": "ProductOverview.txt",
        "content": "The product is a generic SaaS platform that provides user accounts and subscription-based access to features. Users can sign up, log in, and manage subscriptions in the account settings. Common support topics include billing, login issues, subscription activation, cancellations, and security guidance."
    },
    {
        "name": "SupportScopeAndLimitations.txt",
        "content": "Support can provide guidance, explain policies, and troubleshoot issues. Support does not have access to user passwords, 2FA codes, API keys, or payment card details. Support must not claim to have accessed or modified a user account. Support may ask for non-sensitive identifiers such as account email, order/invoice ID, and approximate timestamps."
    },
    {
        "name": "BillingAndCharges.txt",
        "content": "If a customer reports a charge but no active subscription, first confirm the email used at checkout matches the account email. Ask the user to refresh the page, log out and back in, and check if they have multiple accounts. If the issue persists, request the invoice/order ID and escalate to billing for manual verification."
    },
    {
        "name": "SubscriptionActivation.txt",
        "content": "Subscription activation may take a short time after payment. Recommended steps: wait a few minutes, refresh the app, log out and back in, and verify the subscription status in account settings. If activation still fails, collect order ID and account email, then escalate to billing support."
    },
    {
        "name": "RefundPolicy.txt",
        "content": "Refund requests are reviewed on a case-by-case basis. Do not guarantee refunds. Ask for order ID, purchase date, account email, and a brief description of the issue. Escalate to billing support for suspected double charges, charges after cancellation, or incorrect billing amounts."
    },
    {
        "name": "CancellationPolicy.txt",
        "content": "Customers can cancel from account settings. Cancellation stops future renewals but may not remove access immediately if the customer is still within a paid period. If a customer claims they were charged after canceling, request the invoice/order ID and cancellation timestamp if available, then escalate to billing for investigation."
    },
    {
        "name": "LoginTroubleshooting.txt",
        "content": "If a customer cannot log in, advise them to check for typos and verify they are using the correct email. Suggest trying a different browser/device and clearing cache/cookies. If needed, guide the user to the official password reset process. Never ask for the customer’s password."
    },
    {
        "name": "PasswordResetPolicy.txt",
        "content": "Password resets must be completed using the official password reset flow. Support cannot reset passwords manually. Support must never request or accept passwords, one-time codes, 2FA codes, or recovery codes from customers."
    },
    {
        "name": "2FASecurity.txt",
        "content": "If a customer has 2FA issues, guide them to official recovery options. Never ask for or accept 2FA codes, backup codes, API keys, tokens, or secrets. If account takeover is suspected, advise the customer to secure their email account and reset their password using official flows, then escalate as a security case."
    },
    {
        "name": "AccountVerification.txt",
        "content": "If verification is needed, request only minimal non-sensitive information: account email, invoice/order ID, approximate payment time, and the last successful login time if known. Do not request sensitive personal information or payment card details."
    },
    {
        "name": "IncidentAndOutageHandling.txt",
        "content": "If multiple customers report similar issues, treat it as a possible incident. Acknowledge the issue, collect key details (what happened, when it started, affected features), and inform the customer it may be under investigation. Avoid promising resolution times. Escalate internally when patterns suggest an outage."
    },
    {
        "name": "DataPrivacyAndGDPR.txt",
        "content": "Customer data must be handled in compliance with GDPR. Do not request unnecessary personal data. If a customer requests deletion of personal data, inform them that the request will be handled through the official data deletion process and escalate to the privacy process if required."
    },
    {
        "name": "ToneAndCommunication.txt",
        "content": "Support responses must be calm, polite, and professional. Acknowledge frustration, apologize when appropriate, avoid blame, and provide clear next steps. Keep responses concise and action-oriented. Avoid making claims about actions taken in the customer’s account."
    },
    {
        "name": "EscalationRules.txt",
        "content": "Escalate cases involving suspected fraud, repeated billing errors, security incidents, data breach concerns, account takeover suspicion, and issues not resolved by standard troubleshooting. Include a short summary, non-sensitive identifiers, and steps already attempted."
    },
]