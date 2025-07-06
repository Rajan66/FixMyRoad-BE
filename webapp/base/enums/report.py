class ReportChoices:
    STATUS_CHOICES = [
        ("open", "Open"),
        ("approved", "Approved"),
        ("spam", "Spam"),
        ("resolved", "Resolved"),
    ]

    PRIORITY_CHOICES = [
        ("low", "low"),
        ("medium", "medium"),
        ("high", "High"),
    ]
