# MessageEmbedAuthorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**url** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**proxy_icon_url** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.message_embed_author_response import MessageEmbedAuthorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageEmbedAuthorResponse from a JSON string
message_embed_author_response_instance = MessageEmbedAuthorResponse.from_json(json)
# print the JSON string representation of the object
print(MessageEmbedAuthorResponse.to_json())

# convert the object into a dict
message_embed_author_response_dict = message_embed_author_response_instance.to_dict()
# create an instance of MessageEmbedAuthorResponse from a dict
message_embed_author_response_from_dict = MessageEmbedAuthorResponse.from_dict(message_embed_author_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


