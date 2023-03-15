# Bird-ai classification

This repo contains all the files for the hands-on session to Hands-On with Azure and AI: Activating your Azure for Students Subscription and Building AI Solutions with Azure Cognitive Services.

### To Run

- Install the requirements `pip install -r requirements.txt`
- Create an Azure Custom Vision resource
- Lauch the studio and train the model
- After trainijng, test the model and publish it
- Click on performance, then select Prediction URL
- Copy the `prediction-key` and the `endpoint` for the *Image URL* 
- Go back to the performance tab, copy the iteration number (`Iteration ID`) you want to use. e.g `Iteration 1`
- Click on Settings, and copy the `project ID`
- Open the .env file and paste `prediction-key`, `endpoint`, `Iteration ID` into these.
- Save your changes
- Open your terminal and run `python streamlit app.py`