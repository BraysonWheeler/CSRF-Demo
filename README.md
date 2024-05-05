# CSRF DEMO
## Setup
1. pip install -r requirement.txt
2. fastapi dev main.py

# What is CSRF 
Cross Site Request Forgery - An attack where a victim is tricked into clicking on a link that ends up performing an action on their behalf.

Example - bank.com/submit?payment=100&to=attackerId

if a victim where to click on this link their saved cookies would be automaticlaly inserted into the request by the browser performing the action with the identity of the victim.

## Fixes
- Use csrf tokens saved in the DOM validated by the server.
- don't set cookies with `same-site:"none"`

## Testing
You can use profile.html to view your email. malicous.html is intended to be the phishing site used to trick a user into clicking a form and changing their email. Default setup for form based csrf attacks. Uncomment fetch() in malicious.html and app.options for the vulnerable api in main.py to use fetch based csrf.

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
