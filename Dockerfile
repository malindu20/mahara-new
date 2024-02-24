# Use the official Python image as the base image
FROM python:3.11-slim
 
# Set the working directory in the container
WORKDIR /midterm
 
# Copy the Python script into the container at /app
COPY midtermapp.py .
 
# Install Flask
RUN pip install Flask
 
# Expose port 8080 to the outside world
EXPOSE 8080
 
# Run the Python script when the container launches
CMD ["python", "midtermapp.py"]