import csv
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    """Separate a list of SportClubs into their own sports

    For example, given the list
    [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA"), SportClub("LA", "Angels", "MLB")],
    return the iterable [[SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA")],
    [SportClub("LA", "Angels", "MLB")]]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    # TODO: Complete the function
    all_bysports = []
    all_sports = []
    for i in all_clubs:
        i_sport = i.getSport()
        if i_sport not in all_sports:
            all_sports.append(i_sport)
            all_bysports.append([i])
        else:
            idx_sport = all_sports.index(i_sport)
            all_bysports[idx_sport].append(i)
    return all_bysports


def sortSport(sport: List[SportClub]) -> List[SportClub]:
    """Sort a list of SportClubs by the inverse of their count and their name

    For example, given the list
    [SportClub("Houston", "Rockets", "NBA", 80), SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list
    [SportClub("LA", "Lakers", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130), SportClub("Houston", "Rockets", "NBA", 80)]

    Args:
        sport: A list of SportClubs that only contain clubs playing the same sport

    Returns:
        A sorted list of the SportClubs  
    """
    # TODO: Complete the function
    # hint: check documentation for sorting lists 
    # ( https://docs.python.org/3/library/functions.html#sorted , https://docs.python.org/3/howto/sorting.html#sortinghowto )
    sorted_sport = sorted(sport, key=lambda club: (-club.getCount(), club.getName()))
    return sorted_sport


def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked" for the top 3 teams in each sport.

    Args:
        sorted_sports: an Iterable of different sports, each already sorted correctly
    """
    # TODO: Complete the function
    with open("survey_database.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["City", "Team Name", "Sport", "Number of Times Picked"])
        for sport_clubs in sorted_sports:
            for club in sport_clubs[:3]:  
                writer.writerow([club.getCity(), club.getName(), club.getSport(), club.getCount()])

