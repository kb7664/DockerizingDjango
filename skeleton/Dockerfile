# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Install package managers
RUN apt-get update
RUN apt-get install -y python3.7-dev, python3-apt, python3-pip, apt-utils, vim

# Install and configure mod_wsgi to run on apache2
# TODO: build an apt installer to handle this stuff
RUN apt-get install -y apache2
RUN systemctl reboot
RUN apt-get install -y mod_wsgi-httpd, mod_wsgi,
RUN service httpd restart
Run apt-get install -y apache2-dev, apache2-mpm-worker
RUN a2dismod mpm_event
RUN a2enmod mpm_worker
RUN service apache2 restart
Run apt-get install -y libapache2-mod-wsgi-py3
RUN rm -f /etc/apache2/sites-available/000-default.conf
COPY sites-available-skeleton.conf /etc/apache2/sites-available/sites-available-skeleton.conf
RUN a2ensite /etc/apache2/sites-available/sites-available-skeleton.conf

# Install Postgres
RUN apt-get install -y postgresql-11, postgresql-contrib, libpq-dev

# Install any needed packages specified in requirements.txt
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# create root directory for our project in the container
RUN mkdir /skeleton_app

# Set the working directory to /skeleton_app
WORKDIR /skeleton_app

# Copy the current directory contents into the container at /skeleton_app
COPY ./skeleton_app/

# Serve files though apache2
RUN chmod g+w /opt/repositories/skeleton
RUN chown :www-data /opt/repositories/skeleton
EXPOSE 80 3500
CMD [“apache2ctl”, “-D”, “FOREGROUND”]
