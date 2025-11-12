import time
import random
import logging
from instagrapi import Client
from instagrapi.exceptions import ClientError, LoginRequired 

# ---------- CONFIG ----------
USERNAME = "siwansh578"
PASSWORD = "Rajan@123"
TARGET_USERNAME = "kumarvishwas"  
SESSION_FILE = f"{USERNAME}_session.json"

COMMENTS = [
    "Beautiful message — truly inspiring. 🙏",
    "This resonates deeply — thank you for sharing. 🌟",
    "Such peaceful energy in this post. 🙏✨",
    "Absolutely loved this — it really touched me.",
    "This is needed today. Thank you. 🌿"
]

DM_MESSAGE = (
    "Bot hu bhai — I enjoyed your posts and the energy you share. "
    "Would love to connect and support your journey. 🙏"
)

MAX_LIKES = 3
MAX_COMMENTS = 2
DELAY_BETWEEN_ACTIONS = (8, 20)
# ----------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def human_sleep():
    s = random.uniform(*DELAY_BETWEEN_ACTIONS)
    logging.info(f"Sleeping {s:.1f}s to appear human...")
    time.sleep(s)


def login_client():
    cl = Client()
    try:
        try:
            cl.load_settings(SESSION_FILE)
            cl.login(USERNAME, PASSWORD)
            logging.info("Logged in using existing session.")
        except Exception:
            cl.login(USERNAME, PASSWORD)
            cl.dump_settings(SESSION_FILE)
            logging.info("Logged in and saved session.")
    except ClientError as e:
        logging.error(f"Login failed: {e}")
        raise
    return cl  # ✅ added return so main() gets the client instance


def follow_target(cl, target_username):
    try:
        user_id = cl.user_id_from_username(target_username)
    except Exception as e:
        logging.error(f"Could not find user {target_username}: {e}")
        return None

    try:
        info = cl.user_info(user_id)
        if info.following:
            logging.info(f"Already following {target_username}.")
        else:
            cl.user_follow(user_id)
            logging.info(f"Followed {target_username} (id={user_id}).")
            human_sleep()
    except Exception as e:
        logging.error(f"Follow action failed: {e}")
        return None
    return user_id


def like_and_comment_recent(cl, user_id):
    try:
        medias = cl.user_medias(user_id, 10)
    except Exception as e:
        logging.error(f"Failed to fetch media: {e}")
        return

    likes = 0
    comments = 0
    for media in medias:
        if likes >= MAX_LIKES and comments >= MAX_COMMENTS:
            break

        try:
            if likes < MAX_LIKES and not cl.media_liked(media.id):
                cl.media_like(media.id)
                likes += 1
                logging.info(f"Liked media {media.id}")
                human_sleep()

            if comments < MAX_COMMENTS:
                if random.random() < 0.85:
                    comment_text = random.choice(COMMENTS)
                    cl.media_comment(media.id, comment_text)
                    comments += 1
                    logging.info(f"Commented on media {media.id}: {comment_text}")
                    human_sleep()

        except ClientError as e:
            logging.warning(f"ClientError on media {getattr(media, 'id', 'unknown')}: {e}")
            if "feedback_required" in str(e).lower() or "challenge_required" in str(e).lower():
                logging.error("Instagram feedback/challenge detected. Stopping actions.")
                break
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    logging.info(f"Done liking/commenting (likes={likes}, comments={comments}).")


def send_dm(cl, user_id):
    try:
        cl.direct_send(DM_MESSAGE, [user_id])
        logging.info(f"Sent DM to user id {user_id}")
        human_sleep()
    except Exception as e:
        logging.error(f"Failed to send DM: {e}")


def main():
    logging.info("Starting Instagram spiritual bot.")
    cl = login_client()
    try:
        target_id = follow_target(cl, TARGET_USERNAME)
        if not target_id:
            logging.error("Target not found or follow failed; exiting.")
            return

        like_and_comment_recent(cl, target_id)
        send_dm(cl, target_id)

    except LoginRequired:
        logging.error("Session expired or login required. Delete session file and try again.")
    except Exception as e:
        logging.exception(f"Unhandled exception: {e}")
    finally:
        try:
            cl.dump_settings(SESSION_FILE)
            logging.info("Session saved.")
        except Exception:
            pass

    logging.info("Bot run finished.")


if __name__ == "__main__":
    main()
