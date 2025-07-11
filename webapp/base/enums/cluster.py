class ClusterStatus:
    STATUS_CHOICES = [
        ("new", "New"),
        ("in progress", "In Progress"),
        ("partially_resolved", "Partially Resolved"),
        ("resolved", "Resolved"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("critical", "Critical"),
    ]

    FLAG_CHOICES = [
        ("valid", "Valid"),
        ("needs_review", "Needs Review"),
        ("suspicious", "Suspicious"),
        ("invalid", "Invalid"),
    ]
