import sys
from io import StringIO
from typing import Any, Dict


def run_python_code(code: str) -> Dict[str, Any]:
    stdout_capture = StringIO()
    stderr_capture = StringIO()

    old_stdout = sys.stdout
    old_stderr = sys.stderr

    sys.stdout = stdout_capture
    sys.stderr = stderr_capture

    result = {
        "status": "success",
        "output": None,
        "stdout": None,
        "stderr": None,
        "error": None,
    }

    try:
        local_vars = {}
        exec(code, {"__builtins__": __builtins__}, local_vars)

        result["output"] = local_vars.get("result", None)
        result["stdout"] = stdout_capture.getvalue()
        result["stderr"] = stderr_capture.getvalue()

    except Exception as e:
        result["status"] = "error"
        result["error"] = f"{type(e).__name__}: {str(e)}"
        result["stderr"] = stderr_capture.getvalue()

    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

    return result
