curl -X POST \
    'http://127.0.0.1:8000/api/v1/gatekeeper/token/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'X-CSRFTOKEN: KtOuYZu2fgs2k8IH5h4kiZi4zHcO8UUPSVyd1OYFWVOGNhFbesTWkcrleXnNT39o' \
    -d '{"email": "l3vi3211@gmail.com", "password": "admin"}' | tee >(jq -r '.access' | xsel --clipboard --input)
