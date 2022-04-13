from pathlib import Path

import requests  # type: ignore
from pycocotools.coco import COCO  # type: ignore


class CocoDataDownloader:
    """Downloads the specified categories version of coco data"""

    def main(self, args):
        # Open json
        self.input_json_path = Path(args.json_location)
        self.output_folder_path = Path(args.destination_images)

        # Verify input path exists
        if not self.input_json_path.exists():
            print("Input json path not found.")
            print("Quitting early.")
            quit()

        # Verify output path does not already exist
        if self.output_folder_path.exists():
            should_continue = input("Output path already exists. Overwrite? (y/n) ").lower()
            if should_continue != "y" and should_continue != "yes":
                print("Quitting early.")
                quit()

        # instantiate COCO specifying the annotations json path
        coco = COCO(self.input_json_path)
        imgIds = coco.getImgIds()
        images = coco.loadImgs(imgIds)

        # Save the images into a local folder
        for im in images:
            img_data = requests.get(im["coco_url"]).content
            with open(self.output_folder_path.joinpath(im["file_name"]), "wb") as handler:
                handler.write(img_data)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Download filtered COCO images: " "Download the images from the json file version specified"
    )

    parser.add_argument(
        "-i",
        "--input_json",
        dest="json_location",
        help="path to a json file with filtered annotations consisting of image addresses",
    )

    parser.add_argument(
        "-o",
        "--output_location",
        dest="destination_images",
        help="path to save the downloaded images",
    )

    args = parser.parse_args()

    cdd = CocoDataDownloader()
    cdd.main(args)
