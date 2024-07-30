# Task_django
[test task](https://docs.google.com/document/d/16f7axKvveGAB-R0KvTp8KtOSmnxrGZJr7_QELFvmrn8/edit#heading=h.3hhrszhva87t) for getting a job as junior python developer

Instructrions:
1. Load the project into a Python IDE like Pycharm
2. Download all dependencies that are listed in requirements.txt
3. Run project
4. Go to the registration field http://127.0.0.1:8000/admin/login/?next=/admin/
5. Choice any ready user account
   [admin - Login: admin Password: admin]
   [Manager - Login: manager1 Password: 1234567f]
   [Guard - Login: Guardian Password: 1234567f]
   [Resident - Login: Resident Password: 1234567f]
7. In 'admin' you can create user accounts with any of choosen role, create houses, entrances, appartments, assign managers and any other privilegies
8. In 'manager' you can view house, which you assigned, change entrances and add guards and any manipulations with notifications
9. In 'guard' you can view entrances, notifications
10. In 'resident' you can view appartments, notifications
11. In the “AUDIT LOG” you can get logs with any changes in the entrances and apartments and expand the data that will be logged



Extra work:
1. A unique address and unique numbering of apartments and entrances in the building are required
2. You can only select people from the relevant group
3. Added Log with using django-auditlog
4. Added Notifications placeboard
