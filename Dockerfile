# Use an official Python runtime as a parent image
FROM python:3.10

# Install Git
RUN apt-get update && apt-get install -y git




# Set the working directory in the container
WORKDIR /root/CI-CD-TEST

# Copy the project files into the container
COPY . /root/CI-CD-TEST


## Copy the automation scripts into the container
COPY automation/ /root/automation/
#
## Copy chromedriver to the desired location in the container
COPY chromedriver /usr/bin/chromedriver
COPY chromedriver /usr/local/bin/chromedriver

# Make chromedriver executable (if needed)
RUN chmod +x /usr/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver
RUN chmod +x ./automation/restart-ci

RUN chmod +x /root/automation/restart-ci

# Define environment variable
ENV PATH="/usr/bin/chromedriver:${PATH}"
RUN python3 -m venv venv
# Run the restart-ci script when the container launches

#CMD ["/bin/bash", "-c", "apt-get update && apt-get upgrade -y && /root/automation/restart-ci && tail -f /dev/null"]
CMD ["bash", "-c", "apt-get update && apt-get upgrade -y && while true; do kill -9 $(ps -ef | grep defunct | awk '{print $2}'); sleep 3; done & /root/automation/restart-ci && tail -f /dev/null"]


