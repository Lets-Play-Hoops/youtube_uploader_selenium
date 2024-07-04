import argparse
from youtube_uploader_selenium import YouTubeUploader
from typing import Optional
from media_finder import get_media_list


def main(
    folder_path: str,
    date_str: str,
    thumbnail_path: Optional[str] = None,
    profile_path: Optional[str] = None,
):
    succeed = []
    failed = []
    uploader = YouTubeUploader(thumbnail_path, profile_path)
    for video_name, video_path in get_media_list(folder_path):
        was_video_uploaded, video_id = uploader.upload(video_name, video_path, date_str)
        if was_video_uploaded:
            succeed.append((video_name, video_id))
        else:
            failed.append(video_name)

    print(f"finished all uploads. succeed vidoes: {succeed}, failed videos: {failed}.")
    uploader.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--thumbnail",
        help="Path to the thumbnail image",
    )
    parser.add_argument("--profile", help="Path to the firefox profile")
    args = parser.parse_args()

    date_str = "June 23, 2024"
    folder_path = "H:\\Downloads\\6.23"
    main(
        folder_path,
        date_str,
        args.thumbnail,
        profile_path=args.profile,
    )
