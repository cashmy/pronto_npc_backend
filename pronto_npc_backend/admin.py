# pronto_npc_backend/pronto_npc_backend/admin.py (The complete file)

from django.contrib import admin
from django.urls import reverse # Only reverse is strictly needed in index method
from django.utils.html import format_html
from django.apps import apps
from django.conf import settings

# Alias the default admin.site instance for clarity
from django.contrib.admin import site as default_admin_site

class MyCustomAdminSite(admin.AdminSite):
    site_header = "Pronto NPC Backend Admin"
    site_title = "Pronto NPC Admin"
    index_title = "Welcome to Pronto NPC Backend"

    # CRITICAL: DO NOT DEFINE get_urls() HERE.
    # CRITICAL: DO NOT DEFINE app_index() HERE.
    # This class will inherit ALL the default URL patterns from admin.AdminSite.

    def index(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}

        sphinx_docs_url = '/static/docs/index.html'

        # --- SIMPLIFY THE custom_docs_link TO ONLY INCLUDE SPHINX DOCS ---
        extra_context['custom_docs_link'] = format_html(
            '<div class="admin-custom-docs-container">'
            '<h3>Project Documentation</h3>'
            '<ul>'
            '<li><a href="{}" style="font-weight: bold;">Full Sphinx Documentation</a></li>'
            '</ul>'
            '</div>',
            sphinx_docs_url,
        )
        return super().index(request, extra_context=extra_context)

# 1. Instantiate your custom admin site
custom_admin_site = MyCustomAdminSite(name='my_admin')


# 2. Automated Re-registration (This part remains the same)
print("DEBUG: Attempting to re-register models with custom_admin_site...")
registered_models_to_transfer = list(default_admin_site._registry.items())

for model, model_admin in registered_models_to_transfer:
    try:
        if model._meta.app_label in ['admin', 'auth', 'contenttypes', 'sessions', 'sites', 'staticfiles', 'admindocs']:
            print(f"DEBUG: Skipping built-in model '{model._meta.model_name}' ({model._meta.app_label}) for re-registration.")
            continue

        default_admin_site.unregister(model)
        custom_admin_site.register(model, model_admin.__class__)
        print(f"DEBUG: Re-registered model '{model._meta.model_name}' ({model._meta.app_label}) with custom_admin_site.")
    except admin.sites.AlreadyRegistered:
        print(f"WARNING: Model '{model._meta.model_name}' already registered with custom_admin_site, skipping.")
    except Exception as e:
        print(f"ERROR: Failed to re-register model '{model._meta.model_name}': {e}")
print("DEBUG: Model re-registration process completed.")