# EdiPortal API 🔥


	Portal is a web application that users can create and publish and manage data.

Getting Started

	To work on the sample code, you'll need to clone project's repository to your local computer. If you haven't, do that first.

	bitbucket repo :

	git clone

	1)Create a Python virtual environment for your Django project. This virtual environment allows you to isolate this project and install any packages you need without affecting the system Python installation. At the terminal, type the following command:

		$ virtualenv -p python3.7 venv

	2)Activate the virtual environment:

		$ source venv/bin/activate

	3)Install Python dependencies for this project:

		$ pip install -r requirements.txt

	4)For Database schema:

		$ python manage.py migrate

	5)Create Super User

		$ python manage.py createsupersuer

	6)Start the Django development server:

		$ python manage.py runserver

Open http://127.0.0.1:8000/ in a web browser to view your application.


#sudo apt-get install rabbitmq-server

#systemctl enable rabbitmq-server
#systemctl start rabbitmq-server
#systemctl status rabbitmq-server
#celery -A EdiPortal worker -l info