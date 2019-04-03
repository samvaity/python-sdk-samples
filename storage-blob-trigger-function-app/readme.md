# BlobTrigger - Python

This sample demonstrates a simple use case of processing data on Blobs that are uplaoded to a specific container(configurable) using Python.

## How it works

For a `BlobTrigger` to work, you provide a path which dictates where the blobs are located inside your container, and can also help restrict the types of blobs you wish to return. For instance, you can set the path to `samples/{name}.png` to restrict the trigger to only the samples path and only blobs with ".png" at the end of their name. Every time a blob is created/added on the storage this function is triggered and performs operations on the blob(resize, append, download etc).
