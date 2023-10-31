import argparse
from youtube_uploader_selenium import YouTubeUploader
from typing import Optional
from media_finder import get_media_list


def main(
    video_name: str,
    video_path: str,
    date_str: str,
    thumbnail_path: Optional[str] = None,
    profile_path: Optional[str] = None,
):
    uploader = YouTubeUploader(
        video_name, video_path, date_str, thumbnail_path, profile_path
    )
    was_video_uploaded, video_id = uploader.upload()
    assert was_video_uploaded


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--thumbnail",
        help="Path to the thumbnail image",
    )
    parser.add_argument("--profile", help="Path to the firefox profile")
    args = parser.parse_args()

    date_str = "October 14, 2023"
    for video_name, video_path in get_media_list("H:\\Downloads\\10.14"):
        main(
            video_name,
            video_path,
            date_str,
            args.thumbnail,
            profile_path=args.profile,
        )
