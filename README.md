    Zaro - Django course selling platform (scaffold)


    Requirements:
  - Python 3.9+
  - pip install django razorpay

Quick start:
  1. cd zaro_project
  2. python -m venv .venv
  3. source .venv/bin/activate  (Windows: .venv\Scripts\activate)
  4. pip install django razorpay
  5. export RAZORPAY_KEY_ID='your_key'
     export RAZORPAY_KEY_SECRET='your_secret'
     export DJARO_SECRET_KEY='change-me'
  6. python manage.py migrate
  7. python manage.py createsuperuser
  8. python manage.py runserver

Notes:
 - Razorpay integration requires valid keys and internet access.
 - This scaffold provides core models, templates, and checkout flow.
 - Add media files, course content, and refine templates for production.
