## Short description

SkillCheck is a Django app designed for testing staff knowledge and creating quizzes. With SkillCheck, you can easily create and manage tests or quizzes and track your staff's or users progress. The app provides a REST interface.

SkillCheck also provides detailed statistics for completed quizzes or tests. You can view the average score, and other metrics for individual quizzes, users, categories or for your staff as a whole. This information can help you identify knowledge gaps and areas where additional training may be necessary.

## Quickstart:

- Create admin to create categories. use "python manage.py createsuperuser" command. Admin site is already configured.
- Set moderator permissions for users using admin account.
- Remember to comment project/celery.py and project/_ _ init _ _.py and switch db to sqlite to run project not in Docker. 
- Remember 'django.core.mail.backends.console.EmailBackend' is used by default. Activation link will be printed in console.
- To test endpoints use swagger like 'http://127.0.0.1:8000/swagger/'

## Terms of reference

Registration and authorization.

Testing can be carried out according to different knowledge categories.

Example.

    Programming Languages (category)

        Python Basics (specific test)
        Java Fundamentals (specific test)

    Networking (category)

        TCP/IP Fundamentals (specific test)
        Network Security Principles (specific test)



There should be 2 user modes in the system: moderator and student (employee).

#### Student (employee) actions:

* take test
* view previous test results (number of questions answered correctly, the percentage of correct answers, and the grade received)


#### Moderator actions:

* view statistics of test results in general by categories, by specific tests, by specific users
* CRUD tests, questions to tests, set right and wrong answers


## Tech stack:
Django REST framework, djoser, django_filters, Postgres, Celery, Redis.

## Testing:
Standard Django and DRF testing tools. Use "python manage.py test tests" command.