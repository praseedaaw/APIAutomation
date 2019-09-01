from yattag import Doc
import os
import time


class CreateProgramXml:
    # The utility clacc
    def __init__(self, program_name):
        self.program_name = program_name

    # Method to create an XML with program content in dummy 'qts_watch_folder'
    def is_xml_created(self):

        # Checks current directory
        project_root = os.getcwd()
        qtc_path = project_root + '/qts_watch_folder/'

        # Navigates to new directory 'qts_watch_folder'
        os.chdir(qtc_path)

        # Creates XML file with unique name and unique content to 'qts_watch_folder'
        f = open(str(self.program_name) + ".xml", "x")
        doc, tag, text = Doc().tagtext()
        with tag('program'):
            with tag('name'):
                text(str(self.program_name))
        f.write(doc.getvalue())

        # Notes the time
        file_creation_time = time.time()

        # Navigates back to project root directory
        os.chdir(project_root)

        # Returns the time noted
        return file_creation_time
