---
services: storage
platforms: python
author: samvaity
---

# Azure Storage: Upload and resize with Azure Storage in Python
This sample uses a local copy of an jpg image, resizes that image to a thumbnail size of 128*128 and uploads/creates a blob it to a container(new) with the name `thumbnail1`.

## Running this sample
Use your Azure Storage account name and key. Please update the config.py file with the appropriate properties.

To run the sample using the Storage Service
1. Create a Storage Account through the Azure Portal and provide your STORAGE_ACCOUNT_NAME and STORAGE_ACCOUNT_KEY in the config.py file. See https://azure.microsoft.com/en-us/documentation/articles/storage-create-storage-account/ for more information.
2. Set breakpoints and run the project. 

## Deploy this sample 

Either fork the sample to a local folder or download the zip file from https://github.com/samvaity/python-sdk-samples

To get the source code of the SDK via git, type:
git clone https://github.com/samvaity/python-sdk-samples.git
cd .\storage-blob-resize-upload

##Minimum Requirements
Python 2.7, 3.3, or 3.4.
To install Python, please go to https://www.python.org/downloads/

## More information
  - What is a Storage Account - http://azure.microsoft.com/en-us/documentation/articles/storage-whatis-account/  
  - Getting Started with Blobs - https://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-blob-storage/
  - Blob Service Concepts - http://msdn.microsoft.com/en-us/library/dd179376.aspx 
  - Blob Service REST API - http://msdn.microsoft.com/en-us/library/dd135733.aspx 
  - Storage Emulator - http://azure.microsoft.com/en-us/documentation/articles/storage-use-emulator/