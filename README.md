# Lunar — A Multipurpose Discord Bot

**Lunar** is a Discord bot built with [Pycord](https://docs.pycord.dev), designed to streamline moderation, automate utility tasks, and adapt to evolving server needs.

---
## Setup

### Clone the Repo

```bash
git clone https://github.com/Ryley4/lunar.git
cd lunar
```

### Install Dependencies

```bash
apt install python3
python3 -m pip install -U py-cord
```

### Configuration

- Add bot token into bot.run("")
- Remember to update missing IDs with your own.

### Run

```bash
python3 main.py
```
---
##  Slash Commands Overview

| Command         | Description                               |
|----------------|-------------------------------------------|
| `/ping`         | Check if Lunar is online                 |
| `/kick`         | Kick a user                              |
| `/ban`          | Ban a user                               |
| `/unban`        | Unban a previously banned user           |
| `/mute`         | Add a mute role to a user                |
| `/unmute`       | Remove mute role                         |
| `/clear`        | Bulk delete messages                     |
| `/uptime`       | Show how long Lunar has been running     |
| `/relay`        | Say something as the bot                 |
| `/filteradd`    | Add a word to the bad word list          |
| `/filterdel`    | Remove a word from the bad word list     |
| `/filterlist`   | View all filtered words                  |
| `/info`         | Display Lunar's info                     |
| `/lock`         | Lock a text channel                      |
| `/unlock`       | Unlock a text channel                    |
| `/emoteurl`     | Get the URL of a custom emoji            |
| `/pfpurl`       | Get a user’s profile picture URL         |
| `/eject`        | Kick a user but sus                      |

---

##  Autonomous Modules Overview

| Module          | Description                               |
|-----------------|-------------------------------------------|
| `on_member_join`| Pre-entry profile screening              |
| `member_count`  | Updates member counter channel           |
| `auth_ping`     | Removes non-mod @here pings (spam issue) |
| `filter`        | Chat filter                              |

---

##  License

This project is released under the [MIT](https://github.com/Ryley4/lunar/blob/main/LICENSE) License.

