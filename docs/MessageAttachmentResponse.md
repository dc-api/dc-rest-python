# MessageAttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**filename** | **str** |  | 
**size** | **int** |  | 
**url** | **str** |  | 
**proxy_url** | **str** |  | 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**duration_secs** | **float** |  | [optional] 
**waveform** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**ephemeral** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**application** | [**ApplicationResponse**](ApplicationResponse.md) |  | [optional] 
**clip_created_at** | **datetime** |  | [optional] 
**clip_participants** | [**List[UserResponse]**](UserResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.message_attachment_response import MessageAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageAttachmentResponse from a JSON string
message_attachment_response_instance = MessageAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(MessageAttachmentResponse.to_json())

# convert the object into a dict
message_attachment_response_dict = message_attachment_response_instance.to_dict()
# create an instance of MessageAttachmentResponse from a dict
message_attachment_response_from_dict = MessageAttachmentResponse.from_dict(message_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


