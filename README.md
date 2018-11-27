# analysishelpers_app

## Dash App for displaying EDA & Model results 
##### NOTE: This app is directly linked to the analysishelpers package. 
##### NOTE: All graphs images and pickled objects need to be moved into the /app folder in order to be rendered by the app.

First use the analysishelpers package to conduct the analysis. The package will automatically output all graphs as png's (or whatever file type you want) as well as all modeling results (pickled dictionaries). Then use stats_app.py to display the results. 

The app has muptiple tabs; 

 * Tab 1: EDA 
 * Tab 2 - n: Models 

To run the app: 

* Make sure all graph images are in the /app folder 
* Go to the terminal (or command promt) and navigate to the .../analysishelpers_app/app
* Type python3 stats_app.py
  * You'll need to copy the url in the terminal and paste into a web broswer 
