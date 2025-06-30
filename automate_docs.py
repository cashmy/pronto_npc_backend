import os
import shutil
import subprocess
import sys

# --- Configuration ---
# Assume this script is run from the project root (where manage.py is)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Path to your Django project's main app directory (where settings.py is)
# This is PROJECT_ROOT / 'pronto_npc_backend'
DJANGO_SETTINGS_DIR = os.path.join(PROJECT_ROOT, "pronto_npc_backend")

# This is the directory that *contains* your static/ and templates/ folders.
# It should be the same as DJANGO_SETTINGS_DIR if static/ and templates/ are sibling to settings.py.
# If they are in the *first* pronto_npc_backend (where settings.py is), then this is correct.
APP_RESOURCES_ROOT = DJANGO_SETTINGS_DIR  # <--- This is the key change!

# Path to your Sphinx docs directory (where conf.py and index.rst are)
SPHINX_DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")
SPHINX_BUILD_OUTPUT_DIR = os.path.join(SPHINX_DOCS_DIR, "build", "html")

# Destination for the built Sphinx docs within your Django static files
# This now correctly targets:
# pronto_npc_backend/pronto_npc_backend/static/docs/build/html
DJANGO_STATIC_DOCS_DEST = os.path.join(
    APP_RESOURCES_ROOT, "static", "docs", "build", "html"
)

# Path for the admin template override
# Path for the admin template override
DJANGO_ADMIN_TEMPLATE_DIR = os.path.join(PROJECT_ROOT, "core", "templates", "admin")
DJANGO_ADMIN_APP_LIST_TEMPLATE = os.path.join(
    DJANGO_ADMIN_TEMPLATE_DIR, "app_list.html"
)

# Content for the app_list.html override
APP_LIST_TEMPLATE_CONTENT = """{% extends 'admin/app_list.html' %}
{% load i18n static %}

{% block content %}
    {{ block.super }} {# This renders the original content of app_list.html #}

    <div id="content-related" style="margin-top: 20px; padding: 10px; background: #e0e0e0; border-radius: 5px; margin-bottom: 20px;">
        <h3>Project Documentation</h3>
        <ul>
            <li>
                <a href="{% url 'admin:doc_view' %}" class="doc-link">Django Admin Built-in Docs</a>
            </li>
            <li>
                {# Path to your Sphinx docs relative to STATIC_URL #}
                {# Ensure your Sphinx docs are copied to your static files directory #}
                <a href="{% static 'docs/build/html/index.html' %}" class="doc-link">Full Sphinx Documentation</a>
            </li>
        </ul>
    </div>
{% endblock %}
"""

# --- Functions ---


def build_sphinx_docs():
    """Builds the Sphinx documentation."""
    print(f"--- Building Sphinx documentation in {SPHINX_DOCS_DIR} ---")
    current_dir = os.getcwd()  # Stores the current directory (project root)
    os.chdir(SPHINX_DOCS_DIR)  # <--- THIS IS THE CRUCIAL LINE! It changes to 'docs/'
    try:
        # On Windows, use 'cmd /c' to execute the batch file.
        # Ensure that make.bat exists in the SPHINX_DOCS_DIR.
        # Using shell=True for this specific case is fine,
        # but generally avoid it if user input is involved.
        # Alternatively, use ['./make.bat', 'html'] if you don't want shell=True,
        # but ensure './make.bat' is executable.
        result = subprocess.run(
            ["cmd", "/c", "make html"],
            capture_output=True,
            text=True,
            check=True,
            shell=True,
        )  # <--- MODIFIED LINE

        print(result.stdout)
        if result.stderr:
            print(f"Sphinx Build Warnings/Errors:\n{result.stderr}")
        print("Sphinx documentation built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error building Sphinx documentation:\n{e.stderr}")
        sys.exit(1)
    finally:
        os.chdir(current_dir)  # Changes back to the original directory (project root)


def copy_sphinx_docs():
    """Copies the built Sphinx documentation to the Django static directory."""
    print(
        f"--- Copying Sphinx docs from {SPHINX_BUILD_OUTPUT_DIR} to {DJANGO_STATIC_DOCS_DEST} ---"
    )

    # Remove existing destination to ensure a clean copy
    if os.path.exists(DJANGO_STATIC_DOCS_DEST):
        shutil.rmtree(DJANGO_STATIC_DOCS_DEST)
        print(f"Removed existing directory: {DJANGO_STATIC_DOCS_DEST}")

    try:
        shutil.copytree(SPHINX_BUILD_OUTPUT_DIR, DJANGO_STATIC_DOCS_DEST)
        print("Sphinx documentation copied successfully.")
    except Exception as e:
        print(f"Error copying Sphinx documentation: {e}")
        sys.exit(1)


def create_admin_template_override():
    """Creates or updates the Django admin template override for app_list.html."""
    print(
        f"--- Creating/Updating Django admin template override at {DJANGO_ADMIN_APP_LIST_TEMPLATE} ---"
    )

    # Ensure the directory exists
    os.makedirs(DJANGO_ADMIN_TEMPLATE_DIR, exist_ok=True)

    try:
        with open(DJANGO_ADMIN_APP_LIST_TEMPLATE, "w") as f:
            f.write(APP_LIST_TEMPLATE_CONTENT)
        print("Django admin `app_list.html` override created/updated successfully.")
    except Exception as e:
        print(f"Error creating/updating admin template: {e}")
        sys.exit(1)


def main():
    """Main function to automate the documentation process."""
    print("Starting documentation automation process...")

    # 1. Build Sphinx Docs
    build_sphinx_docs()

    # 2. Copy Built Docs to Django Static
    copy_sphinx_docs()

    # 3. Create Admin Template Override
    create_admin_template_override()

    print("\nDocumentation automation complete!")
    print("Remember to run `python manage.py collectstatic` in production,")
    print("and restart your Django development server if it was running.")


if __name__ == "__main__":
    main()
