from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pytz

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def local_time_iso():
    local_tz = pytz.timezone("Asia/Kolkata")  # Change to your timezone
    return datetime.now(local_tz).isoformat()

class Issue(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=3)
    status: str = Field(..., pattern="^(open|in-progress|closed)$")
    priority: str = Field(..., pattern="^(low|medium|high)$")
    assignee: str = Field(..., min_length=1)
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

issues: List[Issue] = []
issue_id = 1

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/issues", response_model=List[Issue])
def list_issues(
    search: Optional[str] = None,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    assignee: Optional[str] = None,
    sort: Optional[str] = None,
    order: str = Query("desc", pattern="^(asc|desc)$"),
    page: int = 1,
    pageSize: int = 10
):
    result = issues.copy()

    # Filters
    if search:
        result = [i for i in result if search.lower() in i.title.lower()]
    if status:
        result = [i for i in result if i.status == status]
    if priority:
        result = [i for i in result if i.priority == priority]
    if assignee:
        result = [i for i in result if i.assignee == assignee]


    if sort:
        reverse = True if order == "desc" else False
        result = sorted(result, key=lambda x: getattr(x, sort, ""), reverse=reverse)

    start = (page - 1) * pageSize
    end = start + pageSize
    return result[start:end]

@app.get("/issues/{issue_id}", response_model=Issue)
def get_issue(issue_id: int):
    for issue in issues:
        if issue.id == issue_id:
            return issue
    raise HTTPException(status_code=404, detail="Issue not found")

@app.post("/issues", response_model=Issue)
def create_issue(issue: Issue):
    global issue_id
    now = local_time_iso()
    issue.id = issue_id
    issue.createdAt = now
    issue.updatedAt = now
    issues.append(issue)
    issue_id += 1
    return issue

@app.put("/issues/{issue_id}", response_model=Issue)
def update_issue(issue_id: int, updated: Issue):
    for i, issue in enumerate(issues):
        if issue.id == issue_id:
            updated.id = issue_id
            updated.createdAt = issue.createdAt  # Preserve creation time
            updated.updatedAt = local_time_iso()
            issues[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Issue not found")
