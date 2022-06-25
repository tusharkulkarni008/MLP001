from collections import namedtuple
DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url","tgz_download_dir","ingested_train_dir","ingested_test_dir"])
DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])
DataTransformationConfig = namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                    "transfromed_train_dir",
                                                                    "transfromed_test_dir",
                                                                    "preprocessed_object_file_path"])