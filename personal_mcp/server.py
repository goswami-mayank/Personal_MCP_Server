"""
Personal Professional Knowledge MCP Server.

Local HTTP:

    fastmcp run personal_mcp/server.py:mcp \
        --transport http \
        --host 0.0.0.0 \
        --port 8000

MCP endpoint:

    http://localhost:8000/mcp
"""

import os

from dotenv import load_dotenv
from fastmcp import FastMCP

from tools.profile import (
    register_profile_tools
)

from tools.projects import (
    register_project_tools
)

from tools.experience import (
    register_experience_tools
)

from tools.search import (
    register_search_tools
)

from resources.profile import (
    register_profile_resources
)


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()


# ============================================================
# SERVER
# ============================================================

mcp = FastMCP(
    name=os.getenv(
        "MCP_SERVER_NAME",
        "Mayank Personal Professional MCP"
    )
)


# ============================================================
# TOOLS
# ============================================================

register_profile_tools(mcp)

register_project_tools(mcp)

register_experience_tools(mcp)

register_search_tools(mcp)


# ============================================================
# RESOURCES
# ============================================================

register_profile_resources(mcp)


# ============================================================
# DIRECT EXECUTION
# ============================================================

if __name__ == "__main__":

    host = os.getenv(
        "MCP_HOST",
        "0.0.0.0"
    )

    port = int(
        os.getenv(
            "MCP_PORT",
            "8000"
        )
    )

    mcp.run(
        transport="http",
        host=host,
        port=port
    )