# Api to colorize black and white images!
### Poetry package manager is being used for dependency management.
## Data Sources and Collection for training.
The famous COCO dataset is being used to train the model.
How to download the dataset?
 1. After cloning the repository, create a new directory called *dataset* inside it.
 2. Then, download and unzip the annotations file while inside the dataset directory from [2017 Train/Val annotations [241MB]](http://images.cocodataset.org/annotations/annotations_trainval2017.zip), you can use *wget* for it.
 3. For this api, only the *person* category is being used for training, you can first filter the annotations for the category using `python filter_coco_annotations.py --input_json dataset/annotations/instances_train2017.json --output_json training_version_one.json --categories person`
 4. The next step is to download the images into your local filesystem using `python download_coco_data.py --input_json dataset/annotations/training_version_one.json --output_location dataset/version_one`
 5. Eventually, if you want to add more categories to the training dataset, this 2 step process makes it easy to version your dataset.
