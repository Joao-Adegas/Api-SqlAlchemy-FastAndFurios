Prerequisites

- Have XAMPP installed on your machine.

Steps to initialize the project

  XAMPP:
  
  - Open XAMPP.

  - Go to Apache Config and click on "Apache (httpd.conf)".

  - Change the ports 8000 to 8080 (Press Ctrl + F and search for 8000 to help you find it).

  - Start Apache and MySQL by clicking on "Start" (If MySQL starts and then stops, open Task Manager and end all mysql processes).

  - Go to MySQL Admin and import the database from the "Database" folder, using the file "carros_velozes_e_furiosos.sql".
  
  BackEnd:
  
  - Navigate to the BackEnd folder.

  - Initialize the virtual environment:
  
          python -m venv env
        ./env/Scripts/activate

  - Install the dependencies from requirements.txt:
  
        pip install -r requirements.txt

  - Start the BackEnd by running the following command in the terminal:
  
        python main.py

  FrontEnd:
  
  - Navigate to the FrontEnd folder.
  
  - Install the node_modules dependencies:
  
        npm i
  
  - Run the FrontEnd with the command:
  
        npm run dev
  
  - Open the link provided in the terminal to access the application.


