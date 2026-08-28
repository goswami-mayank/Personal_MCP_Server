from services.knowledge import (
    get_projects
)


def register_project_tools(mcp):
    """
    Register project-related MCP tools.
    """

    @mcp.tool
    def list_projects() -> dict:
        """
        Return all professional projects.
        """

        try:

            projects = get_projects()

            return {
                "status": "success",
                "count": len(projects)
                if isinstance(projects, list)
                else 1,
                "projects": projects
            }

        except Exception as exc:

            return {
                "status": "error",
                "error_type": type(exc).__name__,
                "error": str(exc)
            }


    @mcp.tool
    def search_projects(
        query: str
    ) -> dict:
        """
        Search projects by name,
        technology, category or description.
        """

        try:

            projects = get_projects()

            if not isinstance(
                projects,
                list
            ):
                projects = [projects]

            query = query.lower().strip()

            matches = []

            for project in projects:

                text = str(
                    project
                ).lower()

                if query in text:
                    matches.append(project)

            return {
                "status": "success",
                "query": query,
                "count": len(matches),
                "projects": matches
            }

        except Exception as exc:

            return {
                "status": "error",
                "error_type": type(exc).__name__,
                "error": str(exc)
            }