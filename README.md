# API Automation

# Tech Stack
- Python 3.7.3 (https://wsvincent.com/install-python3-mac/)
- pip package manager
- Commandline tool for allure report(brew install allure)
- All other libraries needed are added in /APIautomation/requirements.txt
    To install the libraries
    1) Open 'Terminal'
    2) Navigate to project root directory i.e. APIautomation
    3) run the command 'pip install -r requirements.txt' 

## How to set environment for running tests
- python 3 virtual environment(venv) needs to be set up(https://www.ianmaddaus.com/post/manage-multiple-versions-python-mac/)

## Existing Features:
- pytest features are:
    Organize and run test per directory (test discovery)
    Run tests by name matching(test file name and method should start with the word 'test')
    Run tests by mark (smoke, integration, db)
    Create your own fixtures(preconditions) and distribute them.
- Requests library is useful to connect to and interact with APIs
- json and and jsonpath libraries are useful to deal JSON files 
- yattag helps to create XML files

## More possible features
- Batch file to delete xml files in qts_watch_folder
- Integration with Jenkins
- Use other powerful libraries of pytest

### Assumptions
- As qts_watch_folder is not accessible, a dummy file to represent qts_watch_folder is created under project root, i.e. /APIautomation/qts_watch_folder
    - At the present, it is just a folder and no stub is created to delete files in it. But it is possible.
    - Test is created with an assumption that, XML files in qts_watch_folder will be consumed and deleted 

## Run tests
- Navigate to project root path in terminal
- run commands: 
    # Run and generate allure json report
    pytest --alluredir <path to reports folder>
    # for detailed console
    "pytest -v"
    # for simple console
    "pytest"
 # More ways to run
- Refer: http://doc.pytest.org/en/latest/usage.html

## Reports
- allure-pytest JSON (reports will be generated in /APIautomation/reports()
- allure generate -c <path to reports folder> (reports will be converted to HTML file i.e. index.html and saved in directory 'allure-report'. Open in any browser)