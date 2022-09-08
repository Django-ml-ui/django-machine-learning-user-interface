
<h2>Install and Setup<h2>
Install and Setup
Open up a new working directory and create a virtual environment: py -m venv env
Activate the virtual environment: env\Scripts\activate
Intall the package: pip install django-machine-learning-user-interface
Cd to \env\Lib\site-packages\src to find the package files.
Open up code editor e.g. VsCode
Intall project requirments by running: pip install -r requirements.txt on the comand prompt.

Secrete Key
Genrate a secrete key. You can use get one here: https://djecrety.ir/. 
Create a .env file in src and store you secrte key inside. 
Make sure to label it SECRET_KEY.

Inputs
Navigate to src\input
Inside the input file create a folder called model and copy your pickle model file (e.g 'titanic.pkl') into this folder.
In the forms.py file populate the class IndexForm as specified
In the params.py file specify the name of the target variable (e.g. 'Passenger Status') and the name of the model (e.g 'titanic.pkl')


Views
Navigate to src\interface\views.py
Add the cleaned form data as specified (line 21)
List the x variables as specified (line 30)
If your model is a classification model, edit line 41 as specified.


Run 
On the comand prompt run python manage.py runserver, go to local host on your browser(http://127.0.0.1:8000/) and you should see your application and be able to interact with your application. 




