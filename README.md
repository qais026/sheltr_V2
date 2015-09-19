# sheltr_V2

Fork https://github.com/qais026/sheltr_V2

```
git clone git@github.com:YOUR_REPO/sheltr_V2.git
cd sheltr_V2/
virtualenv venv
source venv/bin/activate
python --version # if not python 3, do the next two steps
virtualenv -p python3 venv
python --version # should be python 3 now
pip install -r requirements.txt
python manage.py migrate
python manage.py utils_populate_db_excel
python manage.py createsuperuser
python manage.py runserver
```
```
Visit http://0.0.0.0:8000/
and
http://0.0.0.0:8000/admin
```

### Links
- [https://github.com/qais026/sheltr_V2](https://github.com/qais026/sheltr_V2)
- [https://docs.google.com/document/d/1yjp6I4U1kw8kaToGsFWFTUgfS3LAVs1fNXWytT8O-Io/edit](https://docs.google.com/document/d/1yjp6I4U1kw8kaToGsFWFTUgfS3LAVs1fNXWytT8O-Io
)
- [http://adminsheltr.pythonanywhere.com/](http://adminsheltr.pythonanywhere.com/)

