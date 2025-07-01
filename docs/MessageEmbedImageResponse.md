# MessageEmbedImageResponse


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
from dc_rest.models.message_embed_image_response import MessageEmbedImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageEmbedImageResponse from a JSON string
message_embed_image_response_instance = MessageEmbedImageResponse.from_json(json)
# print the JSON string representation of the object
print(MessageEmbedImageResponse.to_json())

# convert the object into a dict
message_embed_image_response_dict = message_embed_image_response_instance.to_dict()
# create an instance of MessageEmbedImageResponse from a dict
message_embed_image_response_from_dict = MessageEmbedImageResponse.from_dict(message_embed_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


