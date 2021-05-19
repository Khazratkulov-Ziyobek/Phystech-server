<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="#">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <a href="https://phystech-server.herokuapp.com/home">
    <h3 align="center">Student Managment Systems 1.3</h3>
  </a>
  <p align="center">
    by Khazratkulov Ziyobek
    <br />
    
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project-and-usage">About the project and usage</a>
      <ul>
        <li><a href="#description-content-of-the-code">Description content of the code</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#parsing-and-testing">Parsing and testing</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#scraping">Scraping</a></li>
        <li><a href="#testing">Testing</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About the project and usage


This project Student Managment Systems. It is just 1 version. This project is a student data registration. The project is homework Python programming practice Review_2.

Project deployed on Heroku, link <a href="https://phystech-server.herokuapp.com/home">here</a>

You should enter your information and they will appear on main page. A detailed example is shown below:\
<br>
![picture](images/Screenshot_1.png)
<br>
![picture](images/Screenshot_2.png)
<br>
![picture](images/Screenshot_3.png)
<br>
![picture](images/Screenshot_4.png)
<br>
![picture](images/Screenshot_5.png)
<br>
![picture](images/Screenshot_6.png)
<br>

### Description content of the code
* Directories:\
    <b>images</b> - the directory, where the pictures are located.\
    <b>templates</b> - the directory, where the html files are located
* Files:\
    <b>Profile, requirements.txt, runtime.txt, uwsgi.ini</b> - files, which is used for deploying on heroku.\
    <b>app.py</b> - main executable file on project\
    <b>test.py</b> - file for testing our project\
    <b>student_data.db</b> - the database on which all the data is located



### Built with
* [Bootstrap](https://getbootstrap.com) - free set of tools for creating websites and web applications.
* [Flask](https://palletsprojects.com/p/flask/) - framework for creating web applications in the Python programming language
* [Flask_SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - this is a set of SQL tools for Python
* [Unittest](https://docs.python.org/3/library/unittest.html) - testing tool in Python
* [requests](https://pypi.org/project/requests/) - this is a Python HTTP library
* [bs4](https://pypi.org/project/beautifulsoup4/) - it is a Python package for parsing HTML and XML documents


<!-- SCRAPING AND TESTING -->
## Scraping and testing

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Khazratkulov-Ziyobek/Phystech-server.git
   ```
2. Or download zip form
    ![picture](images/Screenshot4.png)
3. Install neccessary pockets:
    ```sh
    - pip install flask
    - pip install flask_sqlalchemy
    - pip install lxml
    - pip install openpyxl
    - pip install unittest
    - pip install requests
    - pip install bs4
    ```
### Scraping
Here I am scraping the table results of the current season Football Leagues from website [SkySports](https://www.skysports.com/). 
<br>
![picture](images/Screenshot_7.png)
<br>
<br>
![picture](images/Screenshot_8.png)
<br>
<br>
![picture](images/Screenshot_9.png)
<br>
<br>
![picture](images/Screenshot_10.png)
<br>
<br>
![picture](images/Screenshot_11.png)
<br>
<br>
![picture](images/Screenshot_12.png)
<br>
<br>

### Testing
```sh
For testing type "python test.py"
```
</details>



<!-- CONTACT -->
## Contact

Telegram account  - [@Khazratkulov_Z](https://web.telegram.org/#/login)

Email - [khazratkulov.zt@phystech.edu]()

Project link - https://github.com/Khazratkulov-Ziyobek/Phystech-server
</details>