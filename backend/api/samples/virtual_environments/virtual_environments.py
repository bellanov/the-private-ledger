"""Virtual Environments.

Overview of *Virtual Environments* and their usage.

Virtual environments are isolated Python environments that allow you to manage
separate sets of dependencies for different projects.
"""

import sys


def demo_venv_info() -> dict:
    """Demonstrate getting information about current Python environment."""
    venv_info = {
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}",
        "python_executable": sys.executable,
        "prefix": sys.prefix,
        "path": sys.path[:3],  # First few entries
    }
    return venv_info


def demo_check_venv_active() -> bool:
    """Check if code is running in a virtual environment."""
    # Check if 'venv' or 'virtualenv' directories exist
    return hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )


def demo_package_isolation() -> str:
    """Demonstrate concept of package isolation in virtual environments."""
    # In a virtual environment, packages are isolated
    # Each venv has its own site-packages directory
    import site

    site_packages = site.getsitepackages()

    if site_packages:
        return site_packages[0]
    else:
        return site.getusersitepackages()


def demo_venv_benefits() -> list:
    """List the benefits of virtual environments."""
    benefits = [
        "Isolate project dependencies",
        "Avoid version conflicts between projects",
        "Reproducible environments",
        "Easy cleanup (just delete the directory)",
        "Can have different Python versions",
    ]
    return benefits


def demo_pip_in_venv() -> str:
    """Demonstrate pip usage in virtual environment."""
    # In a venv, pip is isolated to that environment
    # When you do: pip install package_name
    # It installs to the venv's site-packages, not globally
    return "pip install mypackage  # installs to this venv only"


def main() -> None:
    """Demonstrate virtual environment concepts."""
    # Show Python environment info
    venv_info = demo_venv_info()
    print(f"✓ Python version: {venv_info['python_version']}")
    print(f"✓ Python executable: {venv_info['python_executable']}")

    # Check if in venv
    in_venv = demo_check_venv_active()
    print(f"✓ Running in virtual environment: {in_venv}")

    # Get package isolation info
    site_packages = demo_package_isolation()
    assert site_packages is not None
    print(f"✓ Site packages location: {site_packages}")

    # List benefits
    benefits = demo_venv_benefits()
    assert len(benefits) > 0
    print(f"✓ Virtual environment benefits identified")

    # Pip usage
    pip_cmd = demo_pip_in_venv()
    assert "pip install" in pip_cmd
    print(f"✓ Pip usage in venv understood")

    print("\nAll virtual environment concepts demonstrated successfully!")
    print("\nCommon Virtual Environment Commands:")
    print("- conda create -n venv_name python=3.x  # Create Anaconda venv")
    print("- conda activate venv_name              # Activate venv")
    print("- conda deactivate                       # Deactivate venv")
    print("- python -m venv venv_name              # Create venv with venv module")
    print("- source venv_name/bin/activate         # Activate (Linux/Mac)")
    print("- venv_name\\Scripts\\activate            # Activate (Windows)")
    print("- pip install package_name              # Install packages in venv")
    print("- pip freeze > requirements.txt         # Export dependencies")
    print("- pip install -r requirements.txt       # Install from file")


if __name__ == "__main__":
    main()
