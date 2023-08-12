##  Oura Extract, Transform, and Dashboard

### Description
This project provides a framework for utilizing the [Oura Ring V2 API](https://cloud.ouraring.com/v2/docs) to extract 
personal Oura ring data of interest (`oura_API_extrac.py`), transform the data to create charts (`oura_transform.py`), 
and load the charts into a [streamlit](https://docs.streamlit.io/) dashboard (`oura_dashboard.py`). The dashboard  is 
utilized to create PDFs for printing out and bringing to doctor appointments (`oura_example_report.pdf`).

My previous iteration of this [project](https://github.com/MattyMyers22/Oura_Ring_R_md_PDF) relied on downloading CSVs 
of data from [Oura](https://cloud.ouraring.com/user/sign-in?next=%2F) and utilizing R for data manipulation, 
visualization, and loading the charts into an R Markdown file.

### Dependencies
Modules required for this project can be found in the `requirements.txt` file. It is also required that you have an API 
key registered through Oura. The API key would be concatenated on the end of 'Bearer ' and inserted where `oura_api_key`
is found in `oura_API_extract.py`. Within the file `oura_API_extract.py`, the API key is set up to pull from a 
`config.py` file that is ignored for security reasons.

Once the API key is properly set up, the dashboard can be viewed by running `streamlit run oura_dashboard.py` in the 
terminal from the root directory.

Note: Streamlit is better for creating webapp dashboards than PDF reports. You can either print to PDF utilizing the 
menu on the streamlit dashboard or the functionality of the browser opened. Either method as well as different 
orientations of the PDF (landscape/portrait) may have different results. Sometimes the dashboard may show up as blank. 
This project provided me with an opportunity to play around with streamlit and test its capabilities.