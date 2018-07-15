from shutil import move, copyfile
import os
import binascii
import json

# Def path file report
URL_PATH_INPUT_FILE_REPORT = "C:\\Users\\NGUYENXUANBANG\\Desktop"
# List folder name find report file
URL_PATH_FOLDER_NAME = ["1" , "2"]
URL_PATH_OUTPUT_FILE_REPORT = "C:\\Users\\NGUYENXUANBANG\\Desktop\\report.txt"
NAME_FOLDER_REPORT = "reports"
FILE_NAME_REPORT = "report.json"

# Def method check if folder exit
def check_Folder_Is_Exit(path_file):
    try:
        return os.path.exists(path_file)
    except Exception as e:
        print("ERROR " + str(e))

# Def function read file report using URL
# path_file: path file
def find_And_Read_File_Report(path_file):
    data_resilt_api_stats = []
    try:
        if URL_PATH_FOLDER_NAME and len(URL_PATH_FOLDER_NAME) > 0:
            for name_folder in URL_PATH_FOLDER_NAME:
                for root, directories, filenames in os.walk(path_file + "\\" + name_folder + "\\" + NAME_FOLDER_REPORT):
                    for filename in filenames:
                        if filename == FILE_NAME_REPORT:
                            file_Link_Report = os.path.join(root, filename)
                            # Get file data report in file report json
                            report_file_data = read_File_Report(file_Link_Report)
                            # Get behavior and apistats
                            if report_file_data and len(report_file_data) > 0 and report_file_data['behavior']['apistats'] and len(report_file_data['behavior']['apistats']) > 0:
                                report_file_behavior = report_file_data['behavior']['apistats']
                                for behavior in report_file_behavior:
                                    for data_json in report_file_behavior[behavior]:
                                        data_resilt_api_stats.append(data_json + " : " + str(report_file_behavior[behavior][data_json]))
                                write_File_Report(URL_PATH_OUTPUT_FILE_REPORT, data_resilt_api_stats)
        else:
            print("ERROR NOT FOUND")                
    except Exception as e:
        print("ERROR " + str(e))

# Read file report using path file
# Return Data in JSON file
def read_File_Report(path_file):
    try:
        with open(path_file, "r") as report_file:
            return json.load(report_file)
    except Exception as e:
        print("ERROR " + str(e))

# Method write data to file
def write_File_Report(path_file, data):
    try:
        if data and len(data) > 0:
            with open(path_file, 'a', encoding="utf-8") as the_file:
                for data_dis in data:
                    the_file.write(data_dis + "\n")
    except Exception as e:
        print("ERROR " + str(e))

# Main run report file
def main_run():
    flat_Is_Exit_Folder = check_Folder_Is_Exit(URL_PATH_INPUT_FILE_REPORT)
    if flat_Is_Exit_Folder and flat_Is_Exit_Folder == True:
        find_And_Read_File_Report(URL_PATH_INPUT_FILE_REPORT)

main_run()