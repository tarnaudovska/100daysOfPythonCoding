# ISS Overhead Notification System

This Python script sends an email notification to alert you when the International Space Station (ISS) is passing overhead at night in your location.

## Prerequisites:
- Python 3.x installed
- `requests` library installed
- Access to an SMTP server (e.g., Gmail, Outlook)
- A valid email account and password (or app password for Gmail)

## Features:
1. **ISS Location Check**: The script checks the current position of the ISS using the Open Notify API and determines if it's within a 5-degree radius of your location.
2. **Day/Night Check**: The script checks if it's currently night time at your location based on the sunrise and sunset times using the Sunrise-Sunset API.
3. **Email Notification**: If both conditions are met (ISS overhead and night time), it sends an email to the specified address notifying you that the ISS is visible.

## How to Use:
1. **Set Your Coordinates**:
   Update the following variables with your own information:
   - `MY_EMAIL`: Your email address.
   - `MY_PASSWORD`: Your email password or an app-specific password (if using Gmail).
   - `MY_LAT`: Your latitude (in decimal degrees).
   - `MY_LONG`: Your longitude (in decimal degrees).

2. **Set Up SMTP Server**:
   - Replace `__YOUR_SMTP_ADDRESS_HERE___` with the SMTP server address of your email provider. For Gmail, use `"smtp.gmail.com"`.
   - Ensure you have access to the SMTP server and have allowed less secure apps or used an app-specific password (for Gmail users).
   
3. **Install Required Libraries**:
   Ensure you have the required libraries installed by running the following command:
