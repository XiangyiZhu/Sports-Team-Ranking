from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple


def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    # TODO: Complete the function
    content = []
    with open(file, "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            if any(not field for field in row):
                raise ValueError
            city, name, sport = row
            content.append((city, name, sport))
    return content
                

def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory,calls readFile(file) on each of
    them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the
    number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing
    the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    # TODO: Complete the function
    cwd = Path(".")
    csv_files = list(cwd.glob('*.csv'))

    bad_files = []
    good_files = []

    all_sport_clubs = []
    for file in csv_files:
        try:
            every_file = readFile(file)
            for line in every_file:
                club = SportClub(*line,1)
                if club not in all_sport_clubs:
                    all_sport_clubs.append(club)
                else:
                    idx = all_sport_clubs.index(club)
                    all_sport_clubs[idx].incrementCount()
            good_files.append(file)
        except ValueError:
            bad_files.append(file)
            continue

    with open('report.txt', 'w') as report_file:
        report_file.write(f"Number of files read: {len(good_files)}\n")
        total_lines = sum(club.getCount() for club in all_sport_clubs)
        report_file.write(f"Number of lines read: {total_lines}\n")

    with open('error_log.txt', 'w') as error_log_file:
        for bad_file in bad_files:
            error_log_file.write(f"{bad_file}\n")

    return all_sport_clubs






    


