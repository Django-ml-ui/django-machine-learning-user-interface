**This package is intended to help developers quickly build scalable and customisable front end user interfaces for machine learning models.**
<br>
<h6>Install and Setup<h6>

  <p>1. Open up a new working directory and create a virtual environment: py -m venv env<p/>
  <p>2. Activate the virtual environment: env\Scripts\activate<p/>
  <p>3. Cd to \env\Lib\site-packages\src to find the package files.<p/>
  <p>4. Open up code editor e.g. VsCode.<p/>
  <p>5. Intall project requirments by running: pip install -r requirements.txt on the comand prompt.</p>
<br>
<h6>Secrete Key<h6>
  <p>1. Genrate a secrete key. You can use get one here: https://djecrety.ir/.<p/>
  <p>2. Create a .env file in src and store you secrte key inside.<p/>
  <p>3. Make sure to label it SECRET_KEY.<p/>
<br>
<h6>Inputs<h6>
  <p>1. Navigate to src\input.<p/>
  <p>2. Inside the input file create a folder called model and copy your pickle model file (e.g 'titanic.pkl') into this folder.<p/>
  <p>3. In the forms.py file populate the class IndexForm as specified.<p/>
  <p>4. In the params.py file specify the name of the target variable (e.g. 'Passenger Status') and the name of the model (e.g 'titanic.pkl').<p/>
<br>  
<h6>Views<h6>
  <p>1. Navigate to src\interface\views.py.<p/>
  <p>2. Add the cleaned form data as specified (line 21).<p/>
  <p>3. List the x variables as specified (line 30).<p/>
  <p>4. If your model is a classification model, edit line 41 as specified.<p/>
<br>
<h6>Run<h6>
  <p>1. On the comand prompt run python manage.py runserver.<p/>
  <p>2. Go to local host on your browser(http://127.0.0.1:8000/) and you should see your application and be able to interact with your application. <p/>

  
  
  
