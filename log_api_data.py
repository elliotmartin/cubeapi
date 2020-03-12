import requests
import random

LOG_FILE = "log_cubes.txt"
LOG_MAX = 100


def get_results(page_json):
    return [result for result in page_json['results']]


def write_all_pages(log_file):
    # gets the first page
    r = requests.get("http://localhost:8000/api/cubes/").json()
    while r['next']:
        for result in get_results(r):
            write_log_line(log_file, str(result))

        r = requests.get(r['next']).json()


#TODO
def parse_new_data():
    None


def write_log_line(log_file, line):
    with open(log_file, "a") as f:
        f.write(line)
        f.write("\n")


def clear_log_file(log_file):
    with open(log_file, "w+") as f:
        f.write("")


if __name__ == "__main__":
    clear_log_file(LOG_FILE)
    write_all_pages(LOG_FILE)