# Study Bud

Study Bud is a web application designed to assist students in organizing their study materials, collaborating on projects, and enhancing their learning experience.

## Main Features:

- **User Authentication:** Users can create accounts, log in, and log out.
- **Study Rooms:** Users can create study rooms, each associated with a specific topic.
- **Messaging System:** Users can send and receive messages within study rooms.
- **User Profiles:** Users have profiles displaying their study rooms and activities.
- **Search Functionality:** Search queries cover room names, topics, and room descriptions.
- **Room Management:** Room hosts can update room details, including the room name, topic, and description.
- **User Profile Update:** Users can update their profile information, including username and other relevant details.

## Technologies Used

- **Django:**
- **MySQL:**
- **HTML, CSS, JavaScript:**

## Getting Started

### Prerequisites

- Python 3.10
- MySQL
- Pipenv (optional)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/johnivanpuayap/StudyBud.git
    cd StudyBud
    ```

2. Create and activate a virtual environment (using virtualenv):

    ```bash
    python -m venv venv  # if using virtualenv
    source venv/bin/activate  # on macOS/Linux
    .\venv\Scripts\activate  # on Windows
    ```

3. Install Dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the database settings in 'settings.py':

        Create a database called StudyBud

5. Apply migrations and create database tables:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application at http://localhost:8000/ in your web browser.
