***This package is intended to help developers quickly build scalable and customisable front end user interfaces for machine learning models. You can start using this package by following these 5 easy steps:***


 <br/>
 <br/>

***Step 1: Install and Setup***

  1.1. Open up a new working directory and create a virtual environment by running this command `python -m venv env` on the comand prompt.
  <br/>
  
  1.2. Run `env\Scripts\activate` to activate the virtual environment.
  <br/>
  
  1.3. Install the Django machine learning user interface package by running `pip install django-machine-learning-user-interface`.
  <br/>
  
  1.4. Run `cd \env\Lib\site-packages\src` to find the package files.
  <br/>
  
  1.5. Open up the files on a code editor e.g. VsCode.
  <br/>
  
  1.6. Intall project requirments by running `pip install -r requirements.txt` on the comand prompt.
  <br/>
  <br/>
  
  
 
***Step 2: Secrete Key***

  2.1. Genrate a secrete key. You can use get one here: https://djecrety.ir/.
  <br/>
  
  2.2. Create a .env file in src and store you secrte key inside.
  <br/>
  
  2.3. Make sure to label it `SECRET_KEY`.
  <br/>
  <br/>
  


***Step 3: Inputs***

  3.1. Navigate to `src\input`.
  <br/>
  
  3.2. Inside the input file create a folder and call it **model** then copy your pickle model file (e.g 'titanic.pkl') into this folder.
  <br/>
  
  3.3. In the **forms.py** file populate the class **IndexForm** as specified in the code comments.
  <br/>
  
  3.4. In the **params.py** file specify the name of the target variable (e.g. 'Passenger Status') and the name of the model (e.g 'titanic.pkl').
  <br/>
  <br/>
 
***Step 4: Views***

  4.1. Navigate to `src\interface\views.py`.
  <br/>
  
  4.2. Add the cleaned form data as specified (line 21).
  <br/>
   
  4.3. List the x variables as specified (line 30).
  <br/>
  
  4.4. If your model is a classification model, edit line 41 as specified.
  <br/>
  <br/>
  
  
***Step 5: Generate the UserInterface***

  5.1. On the comand prompt run `python manage.py runserver`.
  <br/>
  
  5.2. Go to local host on your browser(http://127.0.0.1:8000/) and you should see your application and be able to interact with your application.
  <br/>
  
  
  
