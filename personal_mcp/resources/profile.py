import json

from services.knowledge import (
    get_profile,
    get_skills,
    get_projects,
    get_experience
)


def register_profile_resources(mcp):
    """
    Register portfolio resources.
    """

    # ========================================================
    # PROFILE RESOURCE
    # ========================================================

    @mcp.resource(
        "portfolio://profile"
    )
    def profile_resource() -> str:
        """
        Complete professional profile.
        """

        return json.dumps(
            get_profile(),
            indent=2,
            ensure_ascii=False
        )


    # ========================================================
    # SKILLS RESOURCE
    # ========================================================

    @mcp.resource(
        "portfolio://skills"
    )
    def skills_resource() -> str:
        """
        Professional skills.
        """

        return json.dumps(
            get_skills(),
            indent=2,
            ensure_ascii=False
        )


    # ========================================================
    # PROJECTS RESOURCE
    # ========================================================

    @mcp.resource(
        "portfolio://projects"
    )
    def projects_resource() -> str:
        """
        Professional projects.
        """

        return json.dumps(
            get_projects(),
            indent=2,
            ensure_ascii=False
        )


    # ========================================================
    # EXPERIENCE RESOURCE
    # ========================================================

    @mcp.resource(
        "portfolio://experience"
    )
    def experience_resource() -> str:
        """
        Professional experience.
        """

        return json.dumps(
            get_experience(),
            indent=2,
            ensure_ascii=False
        )