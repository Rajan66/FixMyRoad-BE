# FixMyRoad Backend

**FixMyRoad** is a platform for citizens to report damaged roads. Users can submit pothole reports, and ward representatives can validate and analyze them for faster repairs.

---

## Features

- Submit and view pothole reports with images, descriptions, and locations.  
- Ward representatives can validate reports and view clusters.  
- Public map visualization to highlight problem zones.  


## Objectives

- Enable citizens to report road issues easily.  
- Provide authorities with verified reports and analytics.  
- Encourage faster repairs and safer roads.  

---


## Setup (Backend Only)

1. Clone the repo:  
```bash
git clone https://github.com/your-username/FixMyRoad.git
cd FixMyRoad/webapp
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations and start server:
```
python manage.py migrate
python manage.py runserver
```
