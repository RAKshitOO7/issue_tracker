# Issue Tracker Application

---

##  Screenshot

<img width="1903" height="923" alt="Screenshot 2025-09-25 001028" src="https://github.com/user-attachments/assets/6b2fa832-70f0-4845-bf55-069f6b8566d7" />
<img width="1911" height="919" alt="Screenshot 2025-09-25 001041" src="https://github.com/user-attachments/assets/bba52132-d2a5-49ea-a02b-5141b30cfbac" />
<img width="1915" height="920" alt="Screenshot 2025-09-25 001056" src="https://github.com/user-attachments/assets/0ebc5e93-d832-47e8-bcb0-a40959a90e64" />
<img width="1916" height="915" alt="Screenshot 2025-09-25 001139" src="https://github.com/user-attachments/assets/4944c9e6-23e3-4f96-b239-2e29cd6f2234" />
<img width="1919" height="915" alt="Screenshot 2025-09-25 102419" src="https://github.com/user-attachments/assets/4c83aa96-8041-49f5-bcbb-84cfc947a8ab" />
<img width="1914" height="917" alt="Screenshot 2025-09-25 102433" src="https://github.com/user-attachments/assets/15f94960-5291-473f-aa76-5758db9f6677" />

---

##  Features

This Issue Tracker app is designed to manage issues and tasks efficiently. Key features include:

- **Create Issues** — Add new issues with title, status, priority, and assignee.
- **Edit Issues** — Update issue details anytime.
- **List & Filter Issues** — View all issues and filter by search keyword, status, priority, or assignee.
- **Sorting & Pagination** — Sort issues and view them page by page.
- **Backend API with FastAPI** — Robust REST API to store and manage issues.
- **Frontend UI with Angular** — Clean, responsive, and interactive UI for issue management.
- **Local Time Tracking** — Stores created and updated timestamps in local ISO format.
- **CORS Enabled** — API accessible from frontend without cross-origin issues.
- **Submodule Integration** — Frontend is linked as a Git submodule for modular structure.

---

##  How It Works

1. **Frontend (Angular)** — Displays a UI to create, edit, and filter issues.
2. **Backend (FastAPI)** — Stores issues in memory, manages creation, updates, and filtering via API endpoints.
3. **Communication** — Frontend sends HTTP requests to backend APIs to store/retrieve issue data.
4. **Submodule** — Frontend is kept as a separate repository linked inside the main project for modular development.

---

##  Setup & Run

> **Note:** The `issue-tracker-ui` frontend is included as a **Git submodule** inside this repository.  
> Clicking its folder in GitHub will not directly show the files.  
> You must initialize and update the submodule after cloning this repository.  
> Follow the commands below to ensure the frontend is properly set up.

### Clone the repository
Clone this repo and initialize submodules:
```
git clone https://github.com/RAKshitOO7/issue_tracker.git
cd issue_tracker
git submodule update --init --recursive
```
---
## Backend Setup
1. Navigate to backend directory:
 ```
  cd backend

 ```
2. Create a virtual environment (recommended):
  ```
  python -m venv venv
  
  ```
3. Activate the virtual environment
  - **Windows**:
  ```
  venv\Scripts\activate
  ```
- **Mac/Linux**:
 ```
source venv/bin/activate

 ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the backend server:
   ```
   uvicorn app:app --reload
   ```
---

## Frontend Setup

1. Navigate to the frontend submodule directory:
   ```
   cd frontend/issue-tracker-ui
   ```
2. Install frontend dependencies:
   ```
   npm install
   ```
3. Run the Angular frontend:
   ```
   ng serve
   ```
4. The frontend will be available at:
   ```
   http://localhost:4200
   ```
---


##  API Endpoints

| Method | Endpoint           | Description                                      |
|--------|--------------------|--------------------------------------------------|
| GET    | `/issues`          | Get all issues with optional filters, sorting, and pagination |
| GET    | `/issues/{id}`     | Retrieve a specific issue by its ID             |
| POST   | `/issues`          | Create a new issue                              |
| PUT    | `/issues/{id}`     | Update an existing issue                        |
| GET    | `/health`          | Check backend health status                     |


