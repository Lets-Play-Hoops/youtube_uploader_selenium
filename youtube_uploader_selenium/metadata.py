def get_metadata(video_name: str, date_str: str):
    name_without_extention = video_name.split(".")[0].capitalize()
    print("name_without_extention", name_without_extention)
    return {
        "title": f"{name_without_extention} - {date_str}",
        "description": "Join our weekly open run at www.letsplayhoops.com",
        "tags": [
            "basketball",
            "new york",
            "brooklyn",
            "crownheights",
            "letsplayhoops",
            "Let's Play Hoops",
        ],
    }
