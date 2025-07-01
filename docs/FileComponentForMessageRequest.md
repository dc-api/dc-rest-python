# FileComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**spoiler** | **bool** |  | [optional] 
**file** | [**UnfurledMediaRequestWithAttachmentReferenceRequired**](UnfurledMediaRequestWithAttachmentReferenceRequired.md) |  | 

## Example

```python
from dc_rest.models.file_component_for_message_request import FileComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileComponentForMessageRequest from a JSON string
file_component_for_message_request_instance = FileComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(FileComponentForMessageRequest.to_json())

# convert the object into a dict
file_component_for_message_request_dict = file_component_for_message_request_instance.to_dict()
# create an instance of FileComponentForMessageRequest from a dict
file_component_for_message_request_from_dict = FileComponentForMessageRequest.from_dict(file_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


