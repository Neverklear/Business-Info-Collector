# Business Data Scraper

This project is a Python script that searches for businesses using the Google Places API. It reads a list of business categories from a plain text file (one category per line) and, for each category and a specified location, it retrieves detailed business information. The script then saves the results into individual Excel files (one per category) and also creates one master Excel file with all the data.

## Features

- **Google Places API Integration:** Searches for businesses by category and location.
- **Detailed Information:** Retrieves business name, address, phone number, website, and scrapes the website for an email address.
- **Excel Output:** Saves each business category’s results into a separate Excel file and aggregates everything into one master file.
- **Simple Input File:** Reads a list of business categories from a text file (one category per line).

## Prerequisites

Before using this script, please make sure you have the following:

1. **Python 3.11 (or later):**  
   Download and install Python from [python.org/downloads](https://www.python.org/downloads/).  
   **Important:** When installing, check the box that says **"Add Python to PATH"** so your computer knows where to find Python.

2. **pip:**  
   pip is included with Python. You can verify the installation by running the following command in Command Prompt or PowerShell:
   ```bash
   python --version
   pip --version
   ```
   You should see version numbers for both Python and pip.

3. **Google Maps API Key:**  
   You will need a valid Google Maps API Key with access to the Places API. You can get one by visiting the [Google Cloud Platform](https://cloud.google.com/maps-platform/).

## Installation

1. **Clone or Download the Repository:**  
   You can clone this repository using Git:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```
   Or simply download the ZIP file and extract it to a folder on your computer.

2. **Install Required Python Packages:**  
   Open a Command Prompt (or PowerShell) and navigate to the folder where you saved the script. Then run:
   ```bash
   pip install googlemaps pandas requests beautifulsoup4 openpyxl
   ```
   This command installs:
   - **googlemaps:** For interacting with the Google Places API.
   - **pandas:** For organizing and saving data into Excel files.
   - **requests:** For downloading web pages.
   - **beautifulsoup4:** For scraping web pages (to find email addresses).
   - **openpyxl:** For writing data into Excel files.

## Creating Your Business Categories File

1. **Open Notepad:**  
   Click on the **Start** menu, type `Notepad`, and open it.

2. **Enter Business Categories:**  
   Type the list of business categories you want to search for, with each category on a separate line. For example:
   ```
   Restaurants
   Tech Services
   Grocery Stores
   Health Clinics
   ```
3. **Save the File:**  
   - Click **File** > **Save As…**
   - Choose a location that is easy to remember (e.g., your Desktop).
   - Set the file name to `categories.txt`.
   - In the "Save as type" dropdown, choose **All Files**.
   - Click **Save**.

## Running the Script

1. **Open the Command Prompt:**  
   Click on the **Start** menu, type `cmd`, and press **Enter**.

2. **Navigate to the Script Location:**  
   If you saved the script on your Desktop, type:
   ```bash
   cd %USERPROFILE%\Desktop
   ```

3. **Run the Script:**  
   Type the following command and press **Enter**:
   ```bash
   python scrape.py
   ```
   The program will prompt you for:
   - Your **Google Maps API Key**.
   - A **location** (City, Zipcode, or State) where you want to search.
   - The full path to your categories file (for example, `C:\Users\Owner\Desktop\categories.txt`).

4. **Review the Output:**  
   - The script will create an Excel file for each category (e.g., `business_data_Restaurants.xlsx`).
   - A master file named `master_business_data.xlsx` will be created that contains all the business information.

## Troubleshooting

- **Missing Modules:**  
  If you see errors like `ModuleNotFoundError`, ensure you installed the required packages using the pip command provided above.
- **Google Maps API Issues:**  
  Double-check that your API Key is valid and that you have enabled the Places API in your Google Cloud account.
- **File Paths:**  
  When entering file paths, ensure you use the correct format (for example, `C:\Users\Owner\Desktop\categories.txt`).

## Contributing

Contributions are welcome! If you have suggestions, bug fixes, or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any questions or further assistance, please open an issue on GitHub or contact the repository maintainer.
