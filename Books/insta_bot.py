import logging
from instagrapi import Client
from instagrapi.exceptions import ClientError
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

USERNAME = "siwansh578"
PASSWORD = "Rajan@123"
TARGET_USERNAME ="spiritualconce"


SESSION_FILE = "session.json"

def login():
    cl = Client()

    # If session exists, load it
    if os.path.exists(SESSION_FILE):
        try:
            cl.load_settings(SESSION_FILE)
            cl.login(USERNAME, PASSWORD)
            logging.info("Logged in using existing session.")
            return cl
        except Exception as e:
            logging.warning(f"Session load failed: {e}")

    # Fresh login
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(SESSION_FILE)
    logging.info("Logged in and session saved.")
    return cl

def main():
    logging.info("Starting Instagram spiritual bot.")
    cl = login()

    try:
        # Clean username and get user info
        target = TARGET_USERNAME.strip().replace(" ", "")
        user_info = cl.user_info_by_username_v1(target)
        user_id = user_info.pk
        logging.info(f"Found target {target} with ID {user_id}.")

        # Try following directly (no `.following` check)
        result = cl.user_follow(user_id)
        if result:
            logging.info(f"Successfully followed {target}.")
        else:
            logging.error(f"Could not follow {target}.")

        # Send a DM
        cl.direct_send("Namaste 🙏, I appreciate your spiritual wisdom!", [user_id])
        logging.info(f"Message sent to {target}.")

    except ClientError as e:
        logging.error(f"Instagram API error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

    # Save session to reuse later
    cl.dump_settings(SESSION_FILE)
    logging.info("Session saved.")

if __name__ == "__main__":
    main()
