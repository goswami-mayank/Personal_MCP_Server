from services.knowledge import (
    search_knowledge,
    get_storage_status,
    list_data_files
)


def register_search_tools(mcp):
    """
    Register search and diagnostic tools.
    """

    @mcp.tool
    def search_profile(
        query: str
    ) -> dict:
        """
        Search across Mayank's complete professional knowledge.

        Searches:

        - Profile
        - Skills
        - Projects
        - Experience
        """

        try:

            return {
                "status": "success",
                **search_knowledge(query)
            }

        except Exception as exc:

            return {
                "status": "error",
                "error_type": type(exc).__name__,
                "error": str(exc)
            }


    @mcp.tool
    def check_data_availability() -> dict:
        """
        Check whether all JSON files are available
        inside the current server environment.

        Use this when debugging production deployment.
        """

        try:

            return {
                "status": "success",
                **get_storage_status()
            }

        except Exception as exc:

            return {
                "status": "error",
                "error_type": type(exc).__name__,
                "error": str(exc)
            }


    @mcp.tool
    def list_data_files_tool() -> dict:
        """
        List JSON files available to the MCP server.
        """

        try:

            return {
                "status": "success",
                "files": list_data_files()
            }

        except Exception as exc:

            return {
                "status": "error",
                "error_type": type(exc).__name__,
                "error": str(exc)
            }