

# PUBMED_AUTOMATION_APP 📚🔍

## Overview 🚀

PUBMED_AUTOMATION_APP is a full-stack (without database) web application that automating PubMed literature search and data download workflows.
Users upload an Excel file with search queries, and the backend runs automated searches on PubMed, downloads the results, and updates the Excel with comments and counts.

This project uses:

* Python Flask backend + Selenium for automation
* React + Tailwind CSS frontend for user-friendly file upload UI

---

## Features ⭐

* Upload Excel with search queries & filenames
* Automated PubMed searching with Selenium
* Download of search result files (.txt)
* Result counts and comments are added to Excel
* Clean, styled output Excel file
* Responsive React frontend
* Error handling and skip logic for edge cases
* Modular, extensible backend and frontend codebases

---

## Folder Structure 🗂️

```
PUBMED_FULLSTACK/
├── backend/
│   ├── app.py                  # Flask API entry point
│   ├── pubmed_pdf_downloader.py # Core Selenium logic & Excel processing
│   ├── downloads/              # Folder for downloaded PubMed files
│   ├── processed_files/        # Processed Excel files saved here
│   ├── requirements.txt        # Backend dependencies
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── UploadForm.js   # React upload form component
│   │   ├── App.js              # Main React application
│   │   ├── index.js            # React entry point
│   ├── public/                 # Static files for React
│   ├── package.json            # Frontend dependencies
│   ├── tailwind.config.js      # Tailwind CSS configuration
│   └── ...
├── README.md                   # Project documentation (this file)
├── requirements.txt            # (optional root dependencies)
```

---

## Prerequisites ⚙️

* Python 3.8 or higher
* Node.js 16+ with npm or yarn
* Google Chrome browser installed
* ChromeDriver matching your Chrome browser version

  * Download from [here](https://sites.google.com/chromium.org/driver/)
  * Place executable in system PATH or backend folder

---

## Backend Setup 🐍

1. Open terminal, go to backend folder:

   ```bash
   cd backend
   ```

2. Create and activate Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   .\venv\Scripts\activate     # Windows
   ```

3. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run Flask app:

   ```bash
   python app.py
   ```

5. Backend API is now running on:

   ```
   http://127.0.0.1:5000
   ```

---

## Frontend Setup ⚛️

1. Open another terminal, go to frontend folder:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start React development server:

   ```bash
   npm start
   ```

4. Frontend is available at:

   ```
   http://localhost:3000
   ```

---

## API Endpoints 🔌

| Endpoint          | Method | Description                      |
| ----------------- | ------ | -------------------------------- |
| `/upload`         | POST   | Upload Excel file for processing |
| `/download/:file` | GET    | Download processed Excel file    |

---

## How Backend Works 🧠

1. **File Upload:** Receives Excel from frontend.
2. **Excel Parsing:** Reads `Search Strategy 1` and `File Name` columns.
3. **Selenium Automation:**

   * Opens Chrome using ChromeDriver.
   * Visits PubMed, searches queries.
   * Reads result counts, detects warnings.
   * Downloads results if count ≤ 1000.
4. **File Management:**

   * Moves downloaded PubMed files into `downloads/` with user-defined names.
   * Updates Excel with comments & result counts.
5. **Excel Styling:** Uses OpenPyXL to style header and cells.
6. **Response:** Saves updated Excel in `processed_files/` and sends file path to frontend.

---

## How Frontend Works 🎨

* React `UploadForm` component lets user select and upload Excel.
* Sends file via POST `/upload` endpoint.
* Displays status messages based on backend response.
* Provides link/button to download processed Excel.
* Uses Tailwind CSS for modern, responsive styling.

---

## Usage Instructions 📥📤

1. Prepare `Pubs.xlsx` with these required columns:

   * **Search Strategy 1** — Your PubMed search queries
   * **File Name** — Desired name for downloaded text file

2. Run backend and frontend servers (see setup above).

3. Open React frontend in browser: `http://localhost:3000`

4. Upload your Excel file using the upload form.

5. Backend processes, downloads result files, and updates Excel.

6. Download the updated Excel file from the frontend.

7. Check the backend `downloads/` folder for text files downloaded.

---

### 📸 Screenshots

**📥 Excel Input Format**  
![Excel Input](./assets/Excel%20input%20format.png)

**🖼️ Frontend Upload Form**  
![Frontend Upload](./assets/Frontend%20Upload%20Form.png)

**🖥️ Script Running in Terminal**  
![Script Running](./assets/Script%20running%20in%20terminal.png)

**📂 Downloaded Files**  
![Downloaded Files](./assets/Downloaded%20files.png)

**📊 Updated Excel File**  
![Updated Excel](./assets/Updated%20Excel%20File.png)

---

## Troubleshooting & Tips ⚠️

* Ensure ChromeDriver version matches your Chrome browser exactly.
* If downloads fail, confirm ChromeDriver is executable and in PATH.
* Avoid searches with result counts > 1000, they are skipped.
* Check console logs in backend for detailed errors.
* Delete old files in `downloads/` if you want fresh runs.
* Increase Selenium wait times if your internet is slow.

---

## Roadmap & Improvements 🛠️

* Add user authentication for upload and download access
* Support other output formats (CSV, JSON)
* Parallelize Selenium searches for speed
* Deploy backend with Docker container
* Add more detailed logging and retry logic
* Improve frontend UI with progress bars and history
* Unit and integration testing for backend and frontend

---

## Contributing 🤝

Contributions welcome!

1. Fork the repository
2. Create a new feature branch (`git checkout -b feature/my-feature`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push branch (`git push origin feature/my-feature`)
5. Open a Pull Request

Please ensure code passes linting and tests.

---

## Acknowledgments 🙏

* PubMed for their public search interface
* Selenium for browser automation
* React & Tailwind CSS communities for UI frameworks
* OpenPyXL for Excel manipulation

---

## License 📄

This project is licensed under the **MIT License**.

---

## Contact 🙋‍♂️

Created by **Vignesh**
GitHub: [https://github.com/vignesh-vc]
Email: [ceit58vignesh24@gmail.com]

---


