import random
from django.core.management.base import BaseCommand
from _user.models import User
from report.models import PotholeReport
from comment.models import Comment  # adjust import path if needed


class Command(BaseCommand):
    help = "Seed pothole report comments in Nep-English style"

    def handle(self, *args, **kwargs):
        self.stdout.write("⚠️ Clearing old comments...")
        Comment.objects.all().delete()

        reports = list(PotholeReport.objects.all())
        users = list(User.objects.all())

        if not reports:
            self.stdout.write(self.style.ERROR("No pothole reports found!"))
            return

        if not users:
            self.stdout.write(self.style.ERROR("No users found!"))
            return

        # --- 20 Nep-English style comments ---
        comments_pool = [
            "Yo road ta khattam vayo yaar, gadi chalaunda pani dar lagcha 😭",
            "Municipality lai report garda ni kehi hudaina jasto cha.",
            "Hajur haru le pani report garnu na, sabai ko awaj utham!",
            "Aba ta motorbike ko suspension nai tutne bhayo 😩",
            "Yo pothole ma ta ekchoti bus jhardai gayo re!",
            "Ward ko manche haru kahile herne hola yo problem?",
            "Yo road ma pani jamcha, aba tyaha bata hidna pani garo cha.",
            "FixMyRoad app ekdam helpful cha, hope they fix it soon!",
            "Yo area ma pothole ko sankhya din din badhira cha.",
            "Yo report herera authority le action linos hai!",
            "Euta pothole banda arko pothole aai rako cha, mazza!",
            "Yo road ma ta daily accident huney bhayo.",
            "Traffic jam hune mukhya reason nai yo pothole ho.",
            "Yo report ramro cha, photo le sabai proof diyeko cha.",
            "Fix nagarda aba yo jagga ma swimming pool bancha jasto cha 😂",
            "Gadi le jump garnu parcha jasto cha yo road ma!",
            "Yo area ma repair hune bela samma aru pothole ni badhcha hola.",
            "Sabai le milera complain garnu parcha, tes pachi matra kaam hunchha.",
            "Local leader lai tag garne bela aayo aba 😤",
            "Dherai samay dekhi same problem, aba ta limit nai bhayo!",
        ]

        total_comments = 0

        # --- Assign up to 5 random comments per report ---
        for report in reports:
            comment_count = random.randint(1, 5)
            selected_comments = random.sample(comments_pool, comment_count)
            for text in selected_comments:
                user = random.choice(users)
                Comment.objects.create(
                    report=report,
                    user=user,
                    comment=text,
                )
                total_comments += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"🎉 Seeded {
                    total_comments} Nep-English comments across {len(reports)} reports!"
            )
        )
