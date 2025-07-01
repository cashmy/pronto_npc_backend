import argparse
import os
import shutil
import subprocess
import sys
import time


# --- ANSI Color Codes for Terminal Output ---
class Colors:
    """A simple class for adding color to terminal output."""

    SUCCESS = "\033[92m"  # Green
    WARNING = "\033[93m"  # Yellow
    ERROR = "\033[91m"  # Red
    INFO = "\033[94m"  # Blue
    ENDC = "\033[0m"  # End Color


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


def robust_rmtree(path_to_remove: str) -> None:
    """A more robust version of shutil.rmtree that retries on errors."""
    for attempt in range(3):
        try:
            shutil.rmtree(path_to_remove)
            return
        except OSError as e:
            if attempt < 2:
                print(
                    f"{Colors.WARNING}--- Error removing directory {path_to_remove}: {e}. "
                    f"Retrying in 1 second...{Colors.ENDC}"
                )
                time.sleep(1)
            else:
                print(
                    f"{Colors.ERROR}*** Error removing directory {path_to_remove} "
                    f"after multiple retries: {e}{Colors.ENDC}"
                )
                sys.exit(1)


def clean_docs() -> None:
    """Removes the Sphinx build directory if it exists."""
    if os.path.exists(BUILD_DIR):
        print(f"{Colors.INFO}--- Cleaning build directory: {BUILD_DIR}{Colors.ENDC}")
        robust_rmtree(BUILD_DIR)
        print(f"{Colors.SUCCESS}+++ Clean complete.{Colors.ENDC}")
    else:
        print(
            f"{Colors.WARNING}--- Build directory not found. Nothing to clean.{Colors.ENDC}"
        )


def build_docs() -> None:
    """Runs the sphinx-build command to generate HTML documentation."""
    print(f"{Colors.INFO}--- Building Sphinx documentation...{Colors.ENDC}")
    command = [sys.executable, "-m", "sphinx", "-b", "html", SOURCE_DIR, BUILD_DIR]
    result = subprocess.run(command, capture_output=True, text=True, check=False)

    if result.returncode != 0:
        print(f"{Colors.ERROR}*** Sphinx build failed. See errors below:{Colors.ENDC}")
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)
    else:
        print(f"{Colors.SUCCESS}+++ Sphinx build successful.{Colors.ENDC}")
        # Print warnings from the build process, which go to stderr
        if result.stderr:
            print(f"\n{Colors.WARNING}--- Sphinx Build Warnings ---{Colors.ENDC}")
            print(result.stderr.strip())
            print(f"{Colors.WARNING}---------------------------{Colors.ENDC}")


def copy_docs_to_static() -> None:
    """Copies the built Sphinx documentation to the Django static directory."""
    if not os.path.exists(SPHINX_BUILD_HTML_DIR):
        print(
            f"{Colors.WARNING}*** Sphinx build output not found at "
            f"{SPHINX_BUILD_HTML_DIR}. Skipping copy.{Colors.ENDC}"
        )
        return

    print(
        f"{Colors.INFO}--- Copying Sphinx docs from {SPHINX_BUILD_HTML_DIR} to "
        f"{DOCS_DEST_DIR} ---{Colors.ENDC}"
    )

    # Remove existing destination to ensure a clean copy
    if os.path.exists(DOCS_DEST_DIR):
        print(f"--- Removing existing directory: {DOCS_DEST_DIR}")
        robust_rmtree(DOCS_DEST_DIR)

    try:
        shutil.copytree(SPHINX_BUILD_HTML_DIR, DOCS_DEST_DIR)
        print(
            f"{Colors.SUCCESS}+++ Sphinx documentation copied successfully.{Colors.ENDC}"
        )
    except OSError as e:
        print(f"{Colors.ERROR}*** Error copying documentation: {e}{Colors.ENDC}")
        sys.exit(1)


def run_collectstatic() -> None:
    """Runs the Django collectstatic command."""
    print(f"{Colors.INFO}--- Running Django's collectstatic command...{Colors.ENDC}")
    command = [sys.executable, MANAGE_PY, "collectstatic", "--noinput"]
    result = subprocess.run(command, capture_output=True, text=True, check=False)

    if result.returncode != 0:
        print(f"{Colors.ERROR}*** collectstatic failed. See errors below:{Colors.ENDC}")
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)
    else:
        print(f"{Colors.SUCCESS}+++ collectstatic successful.{Colors.ENDC}")


def serve_docs(port: int = 8008) -> None:
    """Serves the built Sphinx documentation on a local web server."""
    if not os.path.exists(SPHINX_BUILD_HTML_DIR):
        print(
            f"{Colors.ERROR}*** Build directory not found at {SPHINX_BUILD_HTML_DIR}. "
            f"Please build the docs first with '-b'.{Colors.ENDC}"
        )
        sys.exit(1)

    os.chdir(SPHINX_BUILD_HTML_DIR)
    try:
        # Use the http.server module available in Python 3
        import http.server
        import socketserver

        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(
                f"{Colors.SUCCESS}--- Serving documentation at http://localhost:{port}/"
                f"{Colors.ENDC}"
            )
            print(f"{Colors.INFO}--- Press Ctrl+C to stop the server.{Colors.ENDC}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{Colors.INFO}--- Server stopped.{Colors.ENDC}")
        sys.exit(0)


def main() -> None:
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
            "  python automate_doc.py --serve # Build and serve docs locally\n"
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
    action_group.add_argument(
        "--serve",
        action="store_true",
        help="Build and serve the documentation on a local web server "
        "(implies --all and ignores --skip-collectstatic).",
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
    is_action_specified = args.clean or args.build or args.all or args.serve
    if not is_action_specified:
        args.all = True

    # --- Execute actions ---
    if args.clean or args.all or args.serve:
        clean_docs()

    if args.build or args.all or args.serve:
        build_docs()
        copy_docs_to_static()
        # 'serve' is for local preview, so we don't run collectstatic
        if args.collectstatic and not args.serve:
            run_collectstatic()

    if args.serve:
        serve_docs()


if __name__ == "__main__":
    main()
