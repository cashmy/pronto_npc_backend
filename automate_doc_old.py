import argparse
import os
import shutil
import subprocess
import sys
import time

# --- Configuration ---
# Assuming this script is in the project root directory.
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
BUILD_DIR = os.path.join(DOCS_DIR, "build")
SOURCE_DIR = os.path.join(DOCS_DIR, "source")
MANAGE_PY = os.path.join(ROOT_DIR, "manage.py")

# New config for copying docs
SPHINX_BUILD_HTML_DIR = os.path.join(BUILD_DIR, "html")
APP_STATIC_DIR = os.path.join(ROOT_DIR, "pronto_npc_backend", "static")
DOCS_DEST_DIR = os.path.join(APP_STATIC_DIR, "docs")


def robust_rmtree(path_to_remove):
    """A more robust version of shutil.rmtree that retries on errors."""
    for attempt in range(3):
        try:
            shutil.rmtree(path_to_remove)
            return
        except OSError as e:
            if attempt < 2:  # Not the last attempt
                print(
                    f"--- Error removing directory {path_to_remove}: {e}. Retrying in 1 second..."
                )
                time.sleep(1)
            else:
                print(
                    f"*** Error removing directory {path_to_remove} after multiple retries: {e}"
                )
                sys.exit(1)


def clean_docs():
    """Removes the Sphinx build directory if it exists."""
    if os.path.exists(BUILD_DIR):
        print(f"--- Cleaning build directory: {BUILD_DIR}")
        robust_rmtree(BUILD_DIR)
        print("+++ Clean complete.")
    else:
        print("--- Build directory not found. Nothing to clean.")


def build_docs():
    """Runs the sphinx-build command to generate HTML documentation."""
    print("--- Building Sphinx documentation...")
    command = [sys.executable, "-m", "sphinx", "-b", "html", SOURCE_DIR, BUILD_DIR]
    result = subprocess.run(command, capture_output=True, text=True, check=False)

    if result.returncode != 0:
        print("*** Sphinx build failed. See errors below:")
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)
    else:
        print("+++ Sphinx build successful.")
        # Print warnings from the build process, which go to stderr
        if result.stderr:
            print("\n--- Sphinx Build Warnings ---")
            print(result.stderr.strip())
            print("---------------------------")

def copy_docs_to_static():
    """Copies the built Sphinx documentation to the Django static directory."""
    if not os.path.exists(SPHINX_BUILD_HTML_DIR):
        print(
            f"*** Sphinx build output not found at {SPHINX_BUILD_HTML_DIR}. Skipping copy."
        )
        return

    print(
        f"--- Copying Sphinx docs from {SPHINX_BUILD_HTML_DIR} to {DOCS_DEST_DIR} ---"
    )

    # Remove existing destination to ensure a clean copy
    if os.path.exists(DOCS_DEST_DIR):
        print(f"Removing existing directory: {DOCS_DEST_DIR}")
        robust_rmtree(DOCS_DEST_DIR)

    try:
        shutil.copytree(SPHINX_BUILD_HTML_DIR, DOCS_DEST_DIR)
        print("+++ Sphinx documentation copied successfully.")
    except OSError as e:
        print(f"*** Error copying documentation: {e}")
        sys.exit(1)

def run_collectstatic():
    """Runs the Django collectstatic command."""
    print("--- Running Django's collectstatic command...")
    command = [sys.executable, MANAGE_PY, "collectstatic", "--noinput"]
    result = subprocess.run(command, capture_output=True, text=True, check=False)

    if result.returncode != 0:
        print("*** collectstatic failed. See errors below:")
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)
    else:
        print("+++ collectstatic successful.")


def main():
    """Parses command-line arguments and executes the requested actions."""
    parser = argparse.ArgumentParser(
        description="Automate Sphinx documentation generation and Django static file collection.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python automate_doc.py      # Clean, build, and run collectstatic (default)\n"
            "  python automate_doc.py -a   # Same as default\n"
            "  python automate_doc.py -b   # Build docs and run collectstatic\n"
            "  python automate_doc.py -b -s  # Build docs only\n"
            "  python automate_doc.py -c   # Clean the build directory only\n"
            "  python automate_doc.py -h   # Show this help message"
        ),
    )

    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument(
        "-c",
        "--clean",
        action="store_true",
        help="Only remove the existing build directory.",
    )
    action_group.add_argument(
        "-b",
        "--build",
        action="store_true",
        help="Build the Sphinx documentation. Runs 'collectstatic' by default.",
    )
    action_group.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Perform 'clean' then 'build'. This is the default action.",
    )

    parser.add_argument(
        "-s",
        "--skip-collectstatic",
        dest="collectstatic",
        action="store_false",
        help="Do not run the 'collectstatic' command after a successful build.",
    )

    args = parser.parse_args()

    # Determine default action if none is specified
    is_action_specified = args.clean or args.build or args.all
    if not is_action_specified:
        args.all = True

    # --- Execute actions ---
    if args.clean or args.all:
        clean_docs()

    if args.build or args.all:
        build_docs()
        copy_docs_to_static()
        if args.collectstatic:
            run_collectstatic()

if __name__ == "__main__":
    main()