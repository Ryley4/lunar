# Lunar — A Multipurpose Discord Bot

**Lunar** is a Discord bot built with [Pycord](https://docs.pycord.dev), designed to streamline moderation, automate utility tasks, and adapt to evolving server needs.

> ⚠️ **Developer's Note:** *This version of Lunar is maintained as part of a personal side-project portfolio and exists solely for archival purposes, separate from the actively maintained build. Many features were originally developed prior to Discord's 2021 builds, before native tools (such as AutoMod) were introduced. They remain to reflect Lunar's original design and development context.*

---
##  Slash Commands Overview

| Command         | Description                               |
|----------------|-------------------------------------------|
| `/ping`         | Check if the bot is online               |
| `/kick`         | Kick a user                              |
| `/ban`          | Ban a user                               |
| `/unban`        | Unban a previously banned user           |
| `/mute`         | Add a mute role to a user                |
| `/unmute`       | Remove mute role                         |
| `/clear`        | Bulk delete messages                     |
| `/uptime`       | Show how long the bot has been running   |
| `/relay`        | Say something as the bot                 |
| `/filteradd`    | Add a word to the bad word list          |
| `/filterdel`    | Remove a word from the bad word list     |
| `/filterlist`   | View all filtered words                  |
| `/info`         | Display bot info                         |
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

