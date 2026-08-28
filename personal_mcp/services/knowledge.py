"""
Knowledge/data service.

This service is responsible for reading JSON files.

IMPORTANT:
The data directory is resolved relative to this Python package
and NOT relative to the current working directory.

Expected production structure:

personal_mcp/
├── data/
│   ├── profile.json
│   ├── skills.json
│   ├── projects.json
│   └── experience.json
│
├── services/
│   └── knowledge.py
│
└── server.py
"""

import json
from pathlib import Path
from typing import Any


# ============================================================
# ABSOLUTE PACKAGE PATH
# ============================================================

# knowledge.py
#     ↓ parent
# services/
#     ↓ parent
# personal_mcp/

PACKAGE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = PACKAGE_DIR / "data"


# ============================================================
# FILES
# ============================================================

PROFILE_FILE = DATA_DIR / "profile.json"
SKILLS_FILE = DATA_DIR / "skills.json"
PROJECTS_FILE = DATA_DIR / "projects.json"
EXPERIENCE_FILE = DATA_DIR / "experience.json"


# ============================================================
# INTERNAL JSON LOADER
# ============================================================

def _load_json(path: Path) -> Any:
    """
    Load a JSON file safely.
    """

    if not DATA_DIR.exists():
        raise FileNotFoundError(
            f"Data directory does not exist: {DATA_DIR}"
        )

    if not path.exists():
        raise FileNotFoundError(
            f"JSON file does not exist: {path}"
        )

    if not path.is_file():
        raise ValueError(
            f"Expected a file but found: {path}"
        )

    try:
        with path.open(
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON file: {path}\n"
            f"Error: {exc}"
        ) from exc


# ============================================================
# PROFILE
# ============================================================

def get_profile() -> Any:
    """
    Return profile.json.
    """

    return _load_json(PROFILE_FILE)


# ============================================================
# SKILLS
# ============================================================

def get_skills() -> Any:
    """
    Return skills.json.
    """

    return _load_json(SKILLS_FILE)


# ============================================================
# PROJECTS
# ============================================================

def get_projects() -> Any:
    """
    Return projects.json.
    """

    return _load_json(PROJECTS_FILE)


# ============================================================
# EXPERIENCE
# ============================================================

def get_experience() -> Any:
    """
    Return experience.json.
    """

    return _load_json(EXPERIENCE_FILE)


# ============================================================
# ALL KNOWLEDGE
# ============================================================

def get_all_knowledge() -> dict:
    """
    Load all professional knowledge.
    """

    return {
        "profile": get_profile(),
        "skills": get_skills(),
        "projects": get_projects(),
        "experience": get_experience()
    }


# ============================================================
# SEARCH
# ============================================================

def search_knowledge(query: str) -> dict:
    """
    Search across all professional knowledge.
    """

    query = query.lower().strip()

    profile = get_profile()
    skills = get_skills()
    projects = get_projects()
    experience = get_experience()

    profile_match = None

    if query in json.dumps(
        profile,
        ensure_ascii=False
    ).lower():
        profile_match = profile

    skills_match = None

    if query in json.dumps(
        skills,
        ensure_ascii=False
    ).lower():
        skills_match = skills

    project_matches = []

    if isinstance(projects, list):

        for project in projects:

            text = json.dumps(
                project,
                ensure_ascii=False
            ).lower()

            if query in text:
                project_matches.append(project)

    experience_matches = []

    if isinstance(experience, list):

        for item in experience:

            text = json.dumps(
                item,
                ensure_ascii=False
            ).lower()

            if query in text:
                experience_matches.append(item)

    return {
        "query": query,
        "profile": profile_match,
        "skills": skills_match,
        "projects": project_matches,
        "experience": experience_matches
    }


# ============================================================
# STORAGE DIAGNOSTICS
# ============================================================

def get_storage_status() -> dict:
    """
    Return filesystem information.

    This is extremely useful for debugging
    production deployment.
    """

    expected_files = [
        PROFILE_FILE,
        SKILLS_FILE,
        PROJECTS_FILE,
        EXPERIENCE_FILE
    ]

    available_files = []

    for file_path in expected_files:

        if file_path.exists():
            available_files.append(
                file_path.name
            )

    missing_files = [
        file_path.name
        for file_path in expected_files
        if not file_path.exists()
    ]

    return {
        "package_directory": str(
            PACKAGE_DIR
        ),
        "data_directory": str(
            DATA_DIR
        ),
        "data_directory_exists": (
            DATA_DIR.exists()
        ),
        "available_files": available_files,
        "missing_files": missing_files,
        "all_files_available": (
            len(missing_files) == 0
        )
    }


# ============================================================
# LIST DATA FILES
# ============================================================

def list_data_files() -> list[str]:
    """
    Return all JSON files available in data/.
    """

    if not DATA_DIR.exists():
        return []

    return sorted(
        file.name
        for file in DATA_DIR.iterdir()
        if file.is_file()
        and file.suffix == ".json"
    )