from services.knowledge import (
    get_experience
)


def register_experience_tools(mcp):
    """
    Register experience-related MCP tools.
    """

    @mcp.tool
    def list_experience() -> dict:
        """
        Return complete professional experience.
        """

        try:

            experience = get_experience()

            return {
                "status": "success",
                "count": len(experience)
                if isinstance(experience, list)
                else 1,
                "experience": experience
            }

        except Exception as exc:

            return {
                "status": "error",
                "error_type": type(exc).__name__,
                "error": str(exc)
            }


    @mcp.tool
    def search_experience(
        organization: str
    ) -> dict:
        """
        Search experience by organization,
        role or technology.
        """

        try:

            experience = get_experience()

            if not isinstance(
                experience,
                list
            ):
                experience = [experience]

            query = organization.lower().strip()

            matches = []

            for item in experience:

                text = str(
                    item
                ).lower()

                if query in text:
                    matches.append(item)

            return {
                "status": "success",
                "query": organization,
                "count": len(matches),
                "experience": matches
            }

        except Exception as exc:

            return {
                "status": "error",
                "error_type": type(exc).__name__,
                "error": str(exc)
            }