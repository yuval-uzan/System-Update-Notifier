import subprocess
import smtplib
from datetime import datetime

# Your email address
your_email = "blabla@gmail.com"

# Bash command to check for updates
update_command = "sudo apt list --upgradable"

# Run the command and get output
process = subprocess.Popen(update_command, shell=True, stdout=subprocess.PIPE)
output, _ = process.communicate()

# Check if updates are available
if "No packages can be upgraded" in output:
    # No updates available
    print("No updates available.")
else:
    # Updates are available
    print("Updates are available.")

    # Send email notification
    subject = "System Updates Available!"
    body = f"""
    Hello {your_email},

    This message is sent automatically by your security system.

    There are updates available for your operating system.

    **It is recommended to install the updates as soon as possible** to protect your system from security vulnerabilities and improve performance.

    Here is a list of available updates:

    {output}

    **To install the updates:**

    1. Open a terminal window.
    2. Type the following command:

        ```
        sudo apt upgrade
        ```

    3. Press Enter and enter your system password when prompted.

    4. Wait for the updates to be installed.

    **Note:** You may need to restart your system after installing the updates.

    Sincerely,

    Your security system
    """

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "your_gmail_username"
    password = "your_gmail_password"

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(username, password)
        smtp.sendmail(username, your_email, f"Subject: {subject}\n{body}")

    print(f"Email sent to {your_email}")

