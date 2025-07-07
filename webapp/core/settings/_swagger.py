class SwaggerSettings:
    SWAGGER_SETTINGS = {
        "SECURITY_DEFINITIONS": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": 'Enter the token with the `Bearer` prefix, e.g. "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."',
            }
        },
        "SECURITY_REQUIREMENTS": [{"Bearer": []}],
        "AUTO_SCHEMA_CLASS": "drf_yasg.inspectors.SwaggerAutoSchema",
    }
