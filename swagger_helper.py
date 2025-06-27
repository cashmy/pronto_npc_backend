import argparse
import os
import subprocess
import sys


def generate_schema(project_root):
    """
    Generates the drf-spectacular schema.yml file.

    Args:
        project_root (str): The absolute path to the Django project's root directory.
    """
    print("\n--- Starting Schema Generation ---")
    print(f"Working directory: {project_root}")

    # Construct the command to run manage.py spectacular
    # sys.executable ensures that the Python interpreter currently running this script
    # (which should be your activated virtual environment's Python) is used.
    schema_command = [
        sys.executable,  # e.g., 'python.exe' or 'python3' from your activated venv
        os.path.join(project_root, "manage.py"),  # Path to manage.py
        "spectacular",
        "--color",
        "--file",
        "schema.yml",
    ]

    try:
        # Execute the command.
        # cwd: Sets the current working directory for the command.
        # check=True: Raises a CalledProcessError if the command returns a non-zero exit code.
        # capture_output=True: Captures stdout and stderr.
        # text=True: Decodes stdout/stderr as text (universal_newlines=True also works).
        result = subprocess.run(
            schema_command, cwd=project_root, check=True, capture_output=True, text=True
        )

        print("\nSchema generation output (stdout):")
        print(result.stdout)
        if result.stderr:
            # drf-spectacular often prints warnings/errors to stderr even on success
            print("\nSchema generation errors/warnings (stderr):")
            print(result.stderr)

        print("\nSchema.yml generated successfully!")

    except subprocess.CalledProcessError as e:
        print(f"\nError generating schema.yml: Command exited with code {e.returncode}")
        print("Command:", " ".join(e.cmd))
        print("Stdout:", e.stdout)
        print("Stderr:", e.stderr)
        sys.exit(1)  # Exit script with an error code
    except FileNotFoundError:
        print("\nError: 'manage.py' or 'python' command not found.")
        print(
            "Please ensure you are in the Django project root and your virtual environment is activated."
        )
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred during schema generation: {e}")
        sys.exit(1)


def launch_docker(project_root):
    """
    Launches the Swagger UI Docker container, mounting the generated schema.yml.

    Args:
        project_root (str): The absolute path to the Django project's root directory.
    """
    print("\n--- Starting Swagger UI Docker Container ---")

    # Get the absolute path to schema.yml on the host machine.
    # Docker volume mounts (`-v`) often prefer forward slashes even on Windows,
    # so we replace os.sep (which is '\' on Windows) with '/'.
    schema_path_on_host = os.path.join(project_root, "schema.yml")
    docker_volume_path = schema_path_on_host.replace(os.sep, "/")

    # Check if schema.yml exists before attempting to mount it
    if not os.path.exists(schema_path_on_host):
        print(f"Error: schema.yml not found at '{schema_path_on_host}'.")
        print(
            "Please generate the schema first (e.g., using --generate-schema or --all option)."
        )
        sys.exit(1)

    # Construct the Docker command
    docker_command = [
        "docker",
        "run",
        "--rm",  # Add --rm to automatically remove the container when it exits/stops
        "-p",
        "8080:8080",  # Maps host port 8080 to container port 8080
        "-e",
        "SWAGGER_JSON=/schema.yml",  # Tells Swagger UI where to find the schema inside the container
        "-v",
        f"{docker_volume_path}:/schema.yml",  # Mounts host schema.yml to container /schema.yml
        "swaggerapi/swagger-ui",
    ]

    print(f"Executing Docker command: {' '.join(docker_command)}")
    print("Swagger UI will be accessible at http://localhost:8080")
    print("Press Ctrl+C in this terminal to stop the Docker container.")

    try:
        # Use check=False because 'docker run' will typically exit with a non-zero code
        # when stopped manually via Ctrl+C, which is expected behavior for interactive containers.
        # We don't capture output because we want Docker's logs to stream directly to the console.
        subprocess.run(docker_command, cwd=project_root, check=False)
        print("\nSwagger UI Docker container stopped.")
    except FileNotFoundError:
        print("\nError: 'docker' command not found.")
        print(
            "Please ensure Docker Desktop is installed and running, and 'docker' is in your system's PATH."
        )
        sys.exit(1)
    except KeyboardInterrupt:
        # Catch KeyboardInterrupt specifically for graceful shutdown
        print("\nCtrl+C detected. Stopping Swagger UI Docker container...")
        # Optional: You could add a 'docker stop' command here if '--rm' wasn't sufficient
        # However, for simple 'docker run' commands, Ctrl+C usually signals the container to stop.
        # We'll rely on '--rm' to clean it up automatically.
        sys.exit(0)  # Exit cleanly
    except Exception as e:
        print(f"\nAn unexpected error occurred while launching Docker: {e}")
        sys.exit(1)


def main():
    """
    Main function to parse arguments and run the selected commands.
    """
    parser = argparse.ArgumentParser(
        description="Automate drf-spectacular schema generation and Swagger UI Docker launch.",
        formatter_class=argparse.RawTextHelpFormatter,  # Keeps help formatting for multi-line descriptions
    )

    # Create a mutually exclusive group for the primary actions
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-g",
        "--generate-schema",
        action="store_true",
        help="Only generate the schema.yml file using drf-spectacular.\n"
        "The command executed is: 'py manage.py spectacular --color --file schema.yml'",
    )
    group.add_argument(
        "-l",
        "--launch-docker",
        action="store_true",
        help="Only launch the Swagger UI Docker container. This assumes 'schema.yml' already exists.\n"
        "The command executed is: 'docker run -p 8080:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/schema.yml:/schema.yml swaggerapi/swagger-ui'",
    )
    group.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Generate schema.yml first, then launch the Swagger UI Docker container.",
    )

    args = parser.parse_args()

    # Determine the project's root directory.
    # This assumes the script is run from the root of your Django project
    # (where manage.py is located).
    project_root = os.getcwd()

    # --- Execute actions based on arguments ---
    if args.generate_schema:
        generate_schema(project_root)
    elif args.launch_docker:
        launch_docker(project_root)
    elif args.all:
        generate_schema(project_root)
        launch_docker(project_root)
    else:
        # If no arguments are provided, print help message and exit
        print("No action specified. Please use -g, -l, or -a.")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    # Wrap the main function call in a try-except to catch top-level KeyboardInterrupt
    # that might not be caught deeper in the subprocess calls
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by user (Ctrl+C). Exiting.")
        sys.exit(0)
