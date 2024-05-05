# CSRF DEMO
## Setup
1. pip install -r requirement.txt
2. fastapi dev main.py

## Testing
You can use profile.html to view your email. malicous.html is intended to be the phishing site used to trick a user into clicking a form and changing their email. Default setup for form based csrf attacks. Uncomment the fetch() and the app.options for the vulnerable api in main.py to use fetch based csrf.

For normal user flow -> http://127.0.0.1:8000/profile

For victim flow -> open malicious.html in browser.

## Safely Update Profile Email Flow
![Image](https://github.com/BraysonWheeler/CSRF-Demo/blob/main/safe_email_update.png)
1. profile.html (http://127.0.0.1:8000/profile) requests a CSRF token.
2. CSRF token is loaded in javascript NOT saved in browser storage or cookies
3. profile.html requests JWT for user
4. JWT is saved in cookies
5. User clicks "Change Profile Email Safe" and a request is sent to /profile/change-email-safe API
6. change-email-safe API validates JWT
7. JWT is valid
8. change-email-safe API validates CSRF Token
9. CSRF Token is Valid and Email is Changed
10. Response is sent to client
