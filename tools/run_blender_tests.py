import sys
import subprocess
import os
from pathlib import Path

def run_blender_tests(blender_path="blender"):
    """
    Spustí pytest uvnitř Blenderu v headless módu.
    """
    project_root = Path(__file__).parent.parent
    tests_path = project_root / "tests" / "blender"
    addon_path = project_root / "addon"

    # Příkaz pro spuštění Blenderu s python skriptem
    # --background: Headless mód
    # --python-expr: Spustí pytest přímo uvnitř Blenderu
    
    cmd = [
        blender_path,
        "--background",
        "--python-expr",
        f"import pytest; import sys; sys.path.append(r'{addon_path}'); sys.exit(pytest.main([r'{tests_path}']))"
    ]

    print(f"Running Blender tests: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    return result.returncode

if __name__ == "__main__":
    # Uživatel může specifikovat cestu k Blenderu přes enviroment proměnnou BLENDER_PATH
    blender_executable = os.environ.get("BLENDER_PATH", "blender")
    exit_code = run_blender_tests(blender_executable)
    sys.exit(exit_code)
