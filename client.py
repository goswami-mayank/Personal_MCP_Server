import asyncio
import json
import os

from fastmcp import Client


# ============================================================
# MCP SERVER URL
# ============================================================

SERVER_URL = os.getenv(
    "MCP_SERVER_URL",
    "http://localhost:8000/mcp"
)


# ============================================================
# DISPLAY RESULT
# ============================================================

def print_result(title, result):

    print()
    print("=" * 80)
    print(title)
    print("=" * 80)

    try:
        print(
            json.dumps(
                result,
                indent=2,
                ensure_ascii=False,
                default=str
            )
        )
    except Exception:
        print(result)


# ============================================================
# CALL MCP TOOL
# ============================================================

async def call_tool(client, tool_name, arguments):

    try:

        result = await client.call_tool(
            tool_name,
            arguments
        )

        return result

    except Exception as exc:

        return {
            "status": "error",
            "tool": tool_name,
            "error_type": type(exc).__name__,
            "error": str(exc)
        }


# ============================================================
# MAIN
# ============================================================

async def main():

    print()
    print("=" * 80)
    print("PERSONAL PROFESSIONAL MCP TEST CLIENT")
    print("=" * 80)

    print()
    print("Connecting to:")
    print(SERVER_URL)

    # ========================================================
    # CONNECT TO MCP SERVER
    # ========================================================

    async with Client(SERVER_URL) as client:

        print()
        print("✓ Connected to MCP server")

        # ====================================================
        # LIST TOOLS
        # ====================================================

        tools = await client.list_tools()

        print_result(
            "AVAILABLE MCP TOOLS",
            [
                tool.name
                for tool in tools
            ]
        )

        # ====================================================
        # LIST RESOURCES
        # ====================================================

        resources = await client.list_resources()

        print_result(
            "AVAILABLE MCP RESOURCES",
            [
                str(resource.uri)
                for resource in resources
            ]
        )

        # ====================================================
        # TEST QUESTIONS
        # ====================================================

        questions = [

            {
                "question": "Is the personal JSON data available?",
                "tool": "check_data_availability",
                "arguments": {}
            },

            {
                "question": "Tell me about Mayank's personal professional profile.",
                "tool": "get_personal_profile",
                "arguments": {}
            },

            {
                "question": "What projects has Mayank built?",
                "tool": "list_projects",
                "arguments": {}
            },

            {
                "question": "What professional experience does Mayank have?",
                "tool": "list_experience",
                "arguments": {}
            },

            {
                "question": "What GenAI projects has Mayank built?",
                "tool": "search_projects",
                "arguments": {
                    "query": "Generative AI"
                }
            },

            {
                "question": "What was Mayank's experience at EY?",
                "tool": "search_experience",
                "arguments": {
                    "organization": "EY"
                }
            },

            {
                "question": "What are Mayank's Python skills?",
                "tool": "search_profile",
                "arguments": {
                    "query": "Python"
                }
            },

            {
                "question": "What does Mayank know about FastAPI?",
                "tool": "search_profile",
                "arguments": {
                    "query": "FastAPI"
                }
            }
        ]

        # ====================================================
        # EXECUTE QUESTIONS
        # ====================================================

        for index, item in enumerate(
            questions,
            start=1
        ):

            question = item["question"]
            tool = item["tool"]
            arguments = item["arguments"]

            print()
            print()
            print("#" * 80)
            print(f"QUESTION {index}")
            print("#" * 80)

            print()
            print("USER:")
            print(question)

            print()
            print("MCP TOOL:")
            print(tool)

            print()
            print("ARGUMENTS:")
            print(
                json.dumps(
                    arguments,
                    indent=2,
                    ensure_ascii=False
                )
            )

            result = await call_tool(
                client,
                tool,
                arguments
            )

            print()
            print("MCP RESPONSE:")

            try:

                print(
                    json.dumps(
                        result,
                        indent=2,
                        ensure_ascii=False,
                        default=str
                    )
                )

            except Exception:

                print(result)

        # ====================================================
        # RESOURCE TEST
        # ====================================================

        print()
        print()
        print("#" * 80)
        print("RESOURCE TESTS")
        print("#" * 80)

        # ----------------------------------------------------
        # PROFILE
        # ----------------------------------------------------

        try:

            result = await client.read_resource(
                "portfolio://profile"
            )

            print_result(
                "PROFILE RESOURCE",
                result
            )

        except Exception as exc:

            print_result(
                "PROFILE RESOURCE ERROR",
                {
                    "error": str(exc)
                }
            )

        # ----------------------------------------------------
        # SKILLS
        # ----------------------------------------------------

        try:

            result = await client.read_resource(
                "portfolio://skills"
            )

            print_result(
                "SKILLS RESOURCE",
                result
            )

        except Exception as exc:

            print_result(
                "SKILLS RESOURCE ERROR",
                {
                    "error": str(exc)
                }
            )

        # ----------------------------------------------------
        # PROJECTS
        # ----------------------------------------------------

        try:

            result = await client.read_resource(
                "portfolio://projects"
            )

            print_result(
                "PROJECTS RESOURCE",
                result
            )

        except Exception as exc:

            print_result(
                "PROJECTS RESOURCE ERROR",
                {
                    "error": str(exc)
                }
            )

        # ----------------------------------------------------
        # EXPERIENCE
        # ----------------------------------------------------

        try:

            result = await client.read_resource(
                "portfolio://experience"
            )

            print_result(
                "EXPERIENCE RESOURCE",
                result
            )

        except Exception as exc:

            print_result(
                "EXPERIENCE RESOURCE ERROR",
                {
                    "error": str(exc)
                }
            )

        # ====================================================
        # COMPLETE
        # ====================================================

        print()
        print()
        print("=" * 80)
        print("✓ MCP SERVER TEST COMPLETED")
        print("=" * 80)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":

    asyncio.run(main())