class CorsSettings:
    ALLOWED_HOSTS = []  # Accepts all hosts in development (not safe for prod)

    CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins in development

    CORS_ALLOWED_ORIGINS = [
        # "http://localhost:3000",
    ]

    # If you want to restrict to specific domains instead:
    # CORS_ALLOW_ALL_ORIGINS = False
    # CORS_ALLOWED_ORIGINS = [
    #     "http://localhost:3000",
    #     "http://127.0.0.1:3000",
    # ]

    CORS_ALLOW_CREDENTIALS = True  # Needed if frontend sends cookies or uses sessions

    CORS_ALLOW_HEADERS = [
        "accept",
        "accept-encoding",
        "authorization",
        "content-type",
        "dnt",
        "origin",
        "user-agent",
        "x-csrftoken",
        "x-requested-with",
    ]
