import requests
import time
import pytest

from utilities import xml_utils
from utilities import string_utils
from utilities import wait_and_check_utils


# Fixtures are not used as only one test case is created. In case of many test cases, fixtures can be implemented
# This is an end to end test case for testing the data flow from qts_watch_folder to media manager content api
# This test interacts with custom utilities created in /APIautomation/utilities path
# This test interacts with dummy qts_watch_folder located at /APIautomation/qts_watch_folder
@pytest.mark.e2e
@pytest.mark.smoke
def test_01_e2e_new_file_to_media_manager():

    # Creates a variable for Media Manager content API
    mm_content_api_url = "http://mm/entities/program/"

    # Creates a unique program name using the customized utility 'string_utils'
    program_name = "program_" + string_utils.unique_string()

    # Creates XML file with the unique file and program name content, puts it to dummy qts_watch_folder inside project
    xml_obj = xml_utils.CreateProgramXml(program_name)
    # Notes the time to use in upcoming timeout condition(xml deletion timeout)
    file_creation_time = xml_obj.is_xml_created()

    # Checks if the XML file is consumed for the timeout period of 60 seconds. It used custom wait and check utility
    xml_consumption_status = wait_and_check_utils.wait_check_xml_deletion(file_creation_time, program_name)

    # If the xml is deleted, notes the time to use in upcoming timeout condition(wfe process completion timeout)
    assert xml_consumption_status == True
    deletion_time = time.time()

    # Gets the WFE Process API in 10s intervals till timeout of 180. It uses a custom utility
    process_completion_status = wait_and_check_utils.wait_check_wfe_process_completion(deletion_time, program_name)

    # Checks Media Manager Content API for the newly added program, if the WFE Process is completed for it
    if process_completion_status:
        mm_response = requests.get(mm_content_api_url + program_name)
        assert mm_response.status_code == 200
