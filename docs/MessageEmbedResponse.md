# MessageEmbedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**color** | **int** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**fields** | [**List[MessageEmbedFieldResponse]**](MessageEmbedFieldResponse.md) |  | [optional] 
**author** | [**MessageEmbedAuthorResponse**](MessageEmbedAuthorResponse.md) |  | [optional] 
**provider** | [**MessageEmbedProviderResponse**](MessageEmbedProviderResponse.md) |  | [optional] 
**image** | [**MessageEmbedImageResponse**](MessageEmbedImageResponse.md) |  | [optional] 
**thumbnail** | [**MessageEmbedImageResponse**](MessageEmbedImageResponse.md) |  | [optional] 
**video** | [**MessageEmbedVideoResponse**](MessageEmbedVideoResponse.md) |  | [optional] 
**footer** | [**MessageEmbedFooterResponse**](MessageEmbedFooterResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.message_embed_response import MessageEmbedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageEmbedResponse from a JSON string
message_embed_response_instance = MessageEmbedResponse.from_json(json)
# print the JSON string representation of the object
print(MessageEmbedResponse.to_json())

# convert the object into a dict
message_embed_response_dict = message_embed_response_instance.to_dict()
# create an instance of MessageEmbedResponse from a dict
message_embed_response_from_dict = MessageEmbedResponse.from_dict(message_embed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


