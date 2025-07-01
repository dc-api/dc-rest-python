# AttachmentResponse


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
from dc_rest.models.attachment_response import AttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentResponse from a JSON string
attachment_response_instance = AttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(AttachmentResponse.to_json())

# convert the object into a dict
attachment_response_dict = attachment_response_instance.to_dict()
# create an instance of AttachmentResponse from a dict
attachment_response_from_dict = AttachmentResponse.from_dict(attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


