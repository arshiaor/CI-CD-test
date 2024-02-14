# Use an official Python runtime as a parent image
FROM python:3.10

# Install Git
RUN apt-get update && apt-get install -y git

# Set the working directory in the container
WORKDIR /root/CI-CD-TEST

# Copy the project files into the container
COPY . /root/CI-CD-TEST

# Copy the automation scripts into the container
COPY /root/automation /root/automation

# Copy chromedriver to the desired location in the container
COPY /usr/bin/chromedriver /usr/bin/chromedriver

# Make chromedriver executable (if needed)
RUN chmod +x /usr/bin/chromedriver

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV PATH="/usr/bin/chromedriver:${PATH}"

# Run the restart-ci script when the container launches
CMD ["/bin/bash", "-c", "/root/automation/restart-ci"]