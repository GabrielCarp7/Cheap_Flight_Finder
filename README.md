# Cheap Flight Finder

A Python project that automatically searches for the best flight deals using the Tequila Kiwi API and logs them in a spreadsheet using the Sheety API. When a cheaper flight is found, the app sends an email notification using smtplib.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [APIs Used](#apis-used)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- Automatically searches for the lowest flight prices.
- Updates flight data in a Google Sheet.
- Sends email notifications for cheap flights.

## Installation

### Prerequisites

- Python 3.x
- A Gmail account (for sending emails)
- API keys for Sheety and Tequila Kiwi APIs

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/GabrielCarp7/Cheap_Flight_Finder.git
    cd Cheap_Flight_Finder
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure your email and API keys:**

    - Open `main.py`.
    - Replace the placeholders with your email, email password, and API keys.

    ```python
    EMAIL = "your_email@example.com"
    PASSWORD = "your_email_password"
    SHEETY_ENDPOINT = "your_sheety_api_endpoint"
    TEQUILA_API_KEY = "your_tequila_api_key"
    ```

## Usage

1. **Run the script:**

    ```bash
    python main.py
    ```

2. **Flight Search and Notification:**

    The app will automatically search for the best flight prices, update your spreadsheet, and send you an email if a cheaper flight is found.

## Technologies

- **Programming Language:** Python
- **Email:** smtplib
- **Web Requests:** Requests
- **Data Storage:** Google Sheets (via Sheety API)

## APIs Used

- **[Sheety API](https://sheety.co/)**: Used to interact with Google Sheets.
- **[Tequila Kiwi API](https://tequila.kiwi.com/)**: Used to search for flight deals.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Contact

Gabriel Carp - [LinkedIn](https://www.linkedin.com/in/gabriel-carp-3b704022b/)
