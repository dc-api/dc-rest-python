# MessageEmbedVideoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**proxy_url** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**placeholder** | **str** |  | [optional] 
**placeholder_version** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**flags** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.message_embed_video_response import MessageEmbedVideoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageEmbedVideoResponse from a JSON string
message_embed_video_response_instance = MessageEmbedVideoResponse.from_json(json)
# print the JSON string representation of the object
print(MessageEmbedVideoResponse.to_json())

# convert the object into a dict
message_embed_video_response_dict = message_embed_video_response_instance.to_dict()
# create an instance of MessageEmbedVideoResponse from a dict
message_embed_video_response_from_dict = MessageEmbedVideoResponse.from_dict(message_embed_video_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


