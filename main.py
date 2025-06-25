import asyncio
import httpx
from fastmcp import FastMCP

mcp = FastMCP("Python Interpreter")


@mcp.tool(
    name="execute_python_code",
    description="Execute Python code with a Python interpreter given a source code string.",
)
async def execute_python_code(source_code: str) -> dict:
    """Execute Python code using the REST API interpreter.

    Args:
        source_code: The Python code to execute

    Returns:
        dict: Result containing stdout, stderr, exit_code, and files
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://localhost:50081/v1/execute",
                json={"source_code": source_code},
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            return {
                "stdout": "",
                "stderr": f"Request error: {str(e)}",
                "exit_code": 1,
                "files": {},
            }
        except httpx.HTTPStatusError as e:
            return {
                "stdout": "",
                "stderr": f"HTTP error {e.response.status_code}: {e.response.text}",
                "exit_code": 1,
                "files": {},
            }


if __name__ == "__main__":
    mcp.run()
