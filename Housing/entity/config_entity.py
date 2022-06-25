from collections import namedtuple
DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url","tgz_download_dir","ingested_train_dir","ingested_test_dir"])