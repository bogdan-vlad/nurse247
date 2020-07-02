# from google.cloud import storage
# import tempfile


# def upload_blob(blob_name):
#     """Uploads a file to the bucket."""
#     bucket_name = "your-nurse-uploads"
#     # source_file_name = "local/path/to/file"
#     # destination_blob_name = "storage-object-name"

#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(blob_name)

#     with tempfile.NamedTemporaryFile() as temp:
#         blob.upload_from_filename(temp.name)

#     print(
#         "File {} uploaded.".format(blob)
#     )
