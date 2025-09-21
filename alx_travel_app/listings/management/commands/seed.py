from decimal import Decimal
from django.core.management.base import BaseCommand
from django.db import transaction

from listings.models import Listing


SAMPLE_LISTINGS = [
    {
        "title": "Cozy Studio in Downtown",
        "description": "A compact, comfortable studio within walking distance of restaurants and transit.",
        "price_per_night": Decimal("45.00"),
        "location": "Downtown"
    },
    {
        "title": "Spacious 2BR Apartment with Balcony",
        "description": "Bright 2 bedroom apartment, full kitchen, balcony with city views.",
        "price_per_night": Decimal("120.00"),
        "location": "City Center"
    },
    {
        "title": "Seaside Cottage",
        "description": "Charming cottage by the sea — perfect for weekend getaways.",
        "price_per_night": Decimal("150.00"),
        "location": "Seaside"
    },
    {
        "title": "Mountain Cabin Retreat",
        "description": "Peaceful cabin surrounded by hiking trails and nature.",
        "price_per_night": Decimal("95.50"),
        "location": "Highlands"
    },
    {
        "title": "Modern Loft Near Tech Hub",
        "description": "Stylish loft with fast wifi and workspace — ideal for remote work.",
        "price_per_night": Decimal("200.00"),
        "location": "Tech District"
    },
]
class Command(BaseCommand):
    help = "Seed the database with sample listings data."
    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all existing listings before seeding.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        clear = options.get("clear", False)
        if clear:
            total_before = Listing.objects.count()
            self.stdout.write(f"Deleting {total_before} existing listing(s)...")
            Listing.objects.all().delete()
        created_count = 0
        for data in SAMPLE_LISTINGS:
            listing, created = Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "price_per_night": data["price_per_night"],
                    "location": data["location"],
                },
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {listing.title}"))

        self.stdout.write(self.style.SUCCESS(f"Seeding complete. {created_count} new listing(s) created."))
