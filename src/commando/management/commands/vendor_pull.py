import helpers

from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")

VENDOR_STATIC_FILES = {
    # "saas-theme.min.css": "https://github.com/codingforentrepreneurs/SaaS-Foundations/blob/main/src/staticfiles/theme/saas-theme.min.css",
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map"
}

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files")
        completed_urls = []
        
        for name, urls in VENDOR_STATIC_FILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(urls, out_path)
            if dl_success:
                completed_urls.append(urls)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {urls}")
                )

        if set(completed_urls) == set(VENDOR_STATIC_FILES.values()):
            self.stdout.write(
                self.style.SUCCESS("Successfully downloaded all vendor static files")
            )
        else:
            self.stdout.write(
                self.style.ERROR("Some files were not downloaded")
            )