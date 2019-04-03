#----------------------------------------------------------------------------------
# Microsoft Developer & Platform Evangelism
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, 
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES 
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
#----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious.  No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
#----------------------------------------------------------------------------------

import os
import config
import sys
from PIL import Image
from random_data import RandomData
from azure.storage import CloudStorageAccount
from azure.storage.blob import BlockBlobService

#
# Azure Storage Blob Sample - Demonstrate how to use the Blob Storage service. 
# Blob storage stores unstructured data such as text, binary data, documents or media files. 
# Blobs can be accessed from anywhere in the world via HTTP or HTTPS. 
#
 
# Documentation References: 
#  - What is a Storage Account - http://azure.microsoft.com/en-us/documentation/articles/storage-whatis-account/ 
#  - Getting Started with Blobs - https://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-blob-storage/
#  - Blob Service Concepts - http://msdn.microsoft.com/en-us/library/dd179376.aspx 
#  - Blob Service REST API - http://msdn.microsoft.com/en-us/library/dd135733.aspx 
#  - Blob Service Python API - http://azure.github.io/azure-storage-python/ref/azure.storage.blob.html
#  - Azure Storage: Getting Started with Azure Storage in Python - https://github.com/Azure-Samples/storage-blob-python-getting-started
#
 
class BlobBasicSamples():

    def __init__(self):
        self.random_data = RandomData()
    # Runs all samples for Azure Storage Blob service.
    # Input Arguments:
    # account - CloudStorageAccount to use for running the samples
    def run_all_samples(self, account):
        print('\n\nAzure Storage Blob sample - Starting.')
        
        try:
            # Block blob basics
            print('\n\n* Basic block blob operations *\n')
            self.basic_blockblob_operations(account)
           
        except Exception as e:
            print('Error occurred in the sample. Please make sure the account name and key are correct.', e)

        finally:
            print('\nAzure Storage Blob sample - Completed.\n')
     
        
    # Runs basic block blob samples for Azure Storage Blob service.
    # Input Arguments:
    # account - CloudStorageAccount to use for running the samples
    def basic_blockblob_operations(self, account):
        blob_name1 = "thumbnail1"
        file_to_upload = "HelloWorld.jpg"
        try:
            # Create a Block Blob Service object
            blockblob_service = account.create_block_blob_service()
            #blockblob_service = BlockBlobService(account_name=config.STORAGE_ACCOUNT_NAME, account_key=config.STORAGE_ACCOUNT_KEY)
            container_name = 'blockblobbasicscontainer' + self.random_data.get_random_name(6)
                # Create a new container
            print('1. Create a container with name - ' + container_name)
            blockblob_service.create_container(container_name)

            # Create a thumbnail
            size = 128, 128
            full_path_to_infile = os.path.join(os.path.dirname(__file__), file_to_upload)
            outfile = os.path.splitext(file_to_upload)[0] + ".thumbnail"
            if file_to_upload != outfile:
                im = Image.open(full_path_to_infile)
                rgb_im = im.convert("RGB")
                rgb_im.thumbnail(size)
                rgb_im.save(outfile, "JPEG")
            print('2. Create a thumbnail with name - ' + outfile)
        
            # Create blobs
            print('3. Create blob of thumbnail name - '+ blob_name1)
            # Get full path on drive to file_to_upload by joining the fully qualified directory name and file name on the local drive
            full_path_to_file = os.path.join(os.path.dirname(__file__), outfile)
            blockblob_service.create_blob_from_path(container_name, blob_name1, full_path_to_file)
            
            # List all the blobs in the container 
            print('3. List Blobs in Container')
            generator = blockblob_service.list_blobs(container_name)
            for blob in generator:
                print('\tBlob Name: ' + blob.name)
            
            # Download the blob
            print('4. Download the blob')
            blockblob_service.get_blob_to_path(container_name, blob_name1, os.path.join(os.path.dirname(__file__), file_to_upload + '.copy.png'))
        except:
            print('Could not complete the operation')
        finally:
            print('Thumbnail Blob uploaded to container successfully!')