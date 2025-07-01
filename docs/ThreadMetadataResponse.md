# ThreadMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** |  | 
**archive_timestamp** | **datetime** |  | [optional] 
**auto_archive_duration** | **int** |  | 
**locked** | **bool** |  | 
**create_timestamp** | **datetime** |  | [optional] 
**invitable** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.thread_metadata_response import ThreadMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadMetadataResponse from a JSON string
thread_metadata_response_instance = ThreadMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(ThreadMetadataResponse.to_json())

# convert the object into a dict
thread_metadata_response_dict = thread_metadata_response_instance.to_dict()
# create an instance of ThreadMetadataResponse from a dict
thread_metadata_response_from_dict = ThreadMetadataResponse.from_dict(thread_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


