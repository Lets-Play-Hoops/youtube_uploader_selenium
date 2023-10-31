from .Constant import *


def get_metadata(video_name: str, date_str: str):
    if "highlight" in video_name.lower():
        video_name = video_name.lower().replace("highlight", "highlights")
        playlist = "Let's Play Hoops Basketball Game Highlights"
    else:
        playlist = "Let's Play Hoops Basketball Game Recording"
    name_without_extention = video_name.split(".")[0].capitalize()

    print("name_without_extention", name_without_extention)
    return {
        Constant.VIDEO_TITLE: f"{name_without_extention} - {date_str}",
        Constant.VIDEO_DESCRIPTION: "Join our weekly open run at www.letsplayhoops.com",
        Constant.VIDEO_TAGS: [
            "basketball",
            "new york",
            "brooklyn",
            "crownheights",
            "letsplayhoops",
            "Let's Play Hoops",
        ],
        Constant.VIDEO_PLAYLIST: playlist,
    }
