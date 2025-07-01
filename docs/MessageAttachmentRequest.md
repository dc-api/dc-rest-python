# MessageAttachmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**filename** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**duration_secs** | **float** |  | [optional] 
**waveform** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**is_remix** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.message_attachment_request import MessageAttachmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MessageAttachmentRequest from a JSON string
message_attachment_request_instance = MessageAttachmentRequest.from_json(json)
# print the JSON string representation of the object
print(MessageAttachmentRequest.to_json())

# convert the object into a dict
message_attachment_request_dict = message_attachment_request_instance.to_dict()
# create an instance of MessageAttachmentRequest from a dict
message_attachment_request_from_dict = MessageAttachmentRequest.from_dict(message_attachment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


