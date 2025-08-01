class ReportChoices:
    STATUS_CHOICES = [
        ("open", "Open"),
        ("in progress", "In Progress"),
        ("resolved", "Resolved"),
    ]

    SEVERITY_CHOICES = [
        ("low", "low"),
        ("medium", "medium"),
        ("high", "High"),
    ]

    FLAG_CHOICES = [
        ("valid", "Valid"),
        ("needs_review", "Needs Review"),
        ("invalid", "Invalid"),
    ]
