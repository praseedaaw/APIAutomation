import time
import os
import requests
import json
import jsonpath


def wait_check_xml_deletion(start_time, program_name):

    # This utility method assumes that 'APIautomation/qts_watch_folder' is the real qts_watch_folder
    # The method gets XML creation time and the new program name to parameters
    # Defines the timeout period as 60 of XML file consumption process
    max_limit = 60  # Seconds.
    deletion_status = False
    project_root = os.getcwd()

    # Checks if time elapsed after xml creation is less than timeout period
    while time.time() - start_time < max_limit:

        # Checks if the xml file is deleted from dummy qts_watch_folder
        if not os.path.exists(project_root + '/qts_watch_folder/' + str(program_name) + ".xml"):
            deletion_status = True
            break

        # Waits 10 seconds and repeats while loop
        time.sleep(10)

    # Returns True when the file is deleted
    return deletion_status


def wait_check_wfe_process_completion(start_time, program_name):
    # This method checks WFE Process status in regular intervals till timeout period of 180 seconds from XML deletion
    # Gets XML deletion time and program name to its parameters

    # Defines API url and initializes other variables
    wfe_api_base_url = "http://wfe/processes"
    time_out = 180  # Seconds.
    process_completed = False

    # Checks if time elapsed after xml deletion is less than timeout period
    while time.time() - start_time < time_out:

        # Gets all processes in WFE.
        wfe_responses = requests.get(wfe_api_base_url)
        wfe_json_response = json.loads(wfe_responses.text)

        # Fetches the length of processes JSON array
        json_length = len(wfe_json_response)

        # Finds the new program object and checks its process status
        for i in range(0, json_length + 1):
            if jsonpath.jsonpath(wfe_json_response[i].program_id) == program_name:
                if jsonpath.jsonpath(wfe_json_response[i].status) == "completed":
                    process_completed = True
            break

        # Waits for 10s if the process is not completed. Repeats fetching and checking the processes again
        time.sleep(10)

    # Returns True when the process is completed for the new program
    return process_completed
