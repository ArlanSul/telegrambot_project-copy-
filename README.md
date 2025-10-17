# **Peer Tutor Telegram Bot**

A Telegram bot designed to streamline the process of connecting student tutors with peers seeking academic help. This bot automates tutor matching, request handling, and communication, making peer tutoring more accessible and efficient.

This project was developed to solve the common problem of manual and inefficient tutor searching in a school environment, where students often struggle to find timely help, and available tutors are underutilized.

## **Features**

* **Dual User Roles**: Separate interfaces and functionalities for "Students" seeking help and "Tutors" offering it.  
* **Tutor Discovery**: Students can browse a list of available tutors and their subjects.  
* **Real-time Request System**: Students can send tutoring requests directly to a chosen tutor.  
* **Request Management**: Tutors receive notifications for new requests and can accept or decline them with inline keyboard buttons.  
* **Direct Messaging**: Once a request is accepted, the bot facilitates a direct, private conversation between the student and the tutor.  
* **Dynamic Profiles**: Tutors can easily set and update the subject they teach.  
* **Persistent Storage**: User data, subjects, and request statuses are managed using a local SQLite database.

## **System Architecture**

The bot operates with a simple client-server architecture:

* **Client-Side**: Any Telegram application (mobile or desktop).  
* **Server-Side**: A Python script using the pyTelegramBotAPI library to handle logic, user interaction, and database queries.  
* **Database**: A serverless SQLite database (tutors.db) to store user and request data.

## **Tech Stack**

* **Backend**: Python  
* **Telegram Bot API**: pyTelegramBotAPI  
* **Database**: SQLite3

## **Database Schema**

users table  
| Field | Data Type | Description |  
| :--- | :--- | :--- |  
| id | INTEGER | Telegram User ID (Primary Key) |  
| username | TEXT | User's Telegram handle |  
| mode | TEXT | Current role ('Find' or 'Become') |  
| subject | TEXT | Subject the user tutors |  
orders table  
| Field | Data Type | Description |  
| :--- | :--- | :--- |  
| id | INTEGER | Unique Request ID (Autoincrement) |  
| sender\_id | INTEGER | Student's Telegram ID |  
| sender\_name | TEXT | Student's Telegram username |  
| recipient\_id | INTEGER | Tutor's Telegram ID |  
| message | TEXT | The initial request message |  
| status | TEXT | Request status ('Pending', 'Accepted', 'Declined') |

## **Setup and Installation**

1. **Clone the repository:**  
   ```
   git clone \[https://github.com/your-username/tutor-bot.git\](https://github.com/your-username/tutor-bot.git)
   cd tutor-bot
   ```

2. **Install dependencies:**  
   ```pip install pyTelegramBotAPI```

3. **Get a Telegram Bot Token:**  
   * Talk to the [@BotFather](https://t.me/botfather) on Telegram.  
   * Create a new bot and copy the API token.  
4. **Configure the bot:**  
   * Open bot.py and replace "YOUR\_TELEGRAM\_BOT\_TOKEN" with the token you received.  
5. **Run the bot:**  
   ```python bot.py```

The bot will initialize the tutors.db database file on its first run.
