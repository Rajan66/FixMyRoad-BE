import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from ward.models import Ward
from _user.models import User, UserProfile

fake = Faker()


class Command(BaseCommand):
    help = "Seed 32 wards with users and UserProfiles, plus 10 extra random users"

    WARDS = [
        "Balkhu",
        "Chhetrapati",
        "Gongabu",
        "Lainchaur",
        "Thamel",
        "Kuleshwor",
        "Teku",
        "Bagbazar",
        "Gaushala",
        "Maitighar",
        "Maharajgunj",
        "Kalimati",
        "Sinamangal",
        "Kalanki",
        "Swayambhu",
        "Balaju",
        "Koteshwor",
        "Bhadrakali",
        "Chabahil",
        "Thapathali",
        "Kirtipur Road",
        "Maitidevi",
        "Jorpati",
        "Chhauni",
        "Teku West",
        "Gongabu East",
        "Balkumari",
        "Samakhusi",
        "Indrachowk",
        "Banasthali",
        "Budhanilkantha",
        "Kapan",
    ]

    DEFAULT_PASSWORD = "admin@123"  # Default password for all users

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("⚠️ Clearing existing wards, users, and profiles...")

        for ward in Ward.objects.all():
            user = ward.user
            ward.delete()
            if user:
                if hasattr(user, "profile"):
                    user.profile.delete()
                user.delete()

        for user in User.objects.filter(role="user"):
            if hasattr(user, "profile"):
                user.profile.delete()
            user.delete()

        self.stdout.write("🗑️ Cleared existing data.")

        wards_list = []
        created_wards = 0

        # Create 32 wards with users and profiles
        for idx, ward_name in enumerate(self.WARDS, start=1):
            user_email = f"ward{idx}@kathmandu.com"
            user = User.objects.create_user(
                email=user_email,
                password=self.DEFAULT_PASSWORD,
                role="user",
                is_active=True,
            )

            # Create the ward
            ward_obj = Ward.objects.create(
                name=ward_name,
                ward_number=str(idx),
                user=user,
                address=f"{ward_name}, Kathmandu",
                phone=None,
            )
            wards_list.append(ward_obj)

            UserProfile.objects.create(
                user=user,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                address=fake.address(),
                ward=None,
            )

            created_wards += 1
            self.stdout.write(
                f"✅ Created Ward {ward_name} with user {
                    user_email} and profile"
            )

        # Create 10 extra random users and profiles
        extra_user_count = 10
        for i in range(1, extra_user_count + 1):
            user_email = f"user{i}@kathmandu.com"
            user = User.objects.create_user(
                email=user_email,
                password=self.DEFAULT_PASSWORD,
                role="user",
                is_active=True,
            )

            # Assign random ward
            random_ward = random.choice(wards_list) if wards_list else None
            UserProfile.objects.create(
                user=user,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                address=fake.address(),
                ward=random_ward,
            )

            self.stdout.write(f"✅ Created extra user {
                              user_email} with profile")

        self.stdout.write(
            self.style.SUCCESS(
                f"🎉 Successfully created "
                + f"{created_wards} wards with users and profiles "
                f"and {extra_user_count} extra users with profiles."
            )
        )
