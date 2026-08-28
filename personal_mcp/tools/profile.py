from services.knowledge import (
    get_profile
)


def register_profile_tools(mcp):
    """
    Register profile-related MCP tools.
    """

    @mcp.tool
    def get_personal_profile() -> dict:
        """
        Get the complete professional profile.
        """

        try:

            return {
                "status": "success",
                "profile": get_profile()
            }

        except Exception as exc:

            return {
                "status": "error",
                "error_type": type(exc).__name__,
                "error": str(exc)
            }