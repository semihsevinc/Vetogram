<h1>Vetogram</h1>

<h2> Application for Veterinary made in Django</h2>

While an account with admin permission can access all functions in the application, a user without permission cannot create, edit or delete any records. You must be logged into the application, except for the home page. If you want, you can create an account yourself.

There are models for Pet owners and patients in the application.
I used a class-based form because I thought it was simple to use on the frontend.

# Quick Start

Install using `git clone git@github.com:semihsevinc/Vetogram.git`

    python manage.py runserver

You can access to home page without `login`, but to see other pages like `Pet Owners` and `Patients`, you must be logged in.

There are accounts for admin and user here, you can create a user yourself if you want.

`Admin` Username: admin  Password: admintest
`User` Username: user Password: usertest
