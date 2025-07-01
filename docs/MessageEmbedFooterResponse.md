# MessageEmbedFooterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**icon_url** | **str** |  | [optional] 
**proxy_icon_url** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.message_embed_footer_response import MessageEmbedFooterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageEmbedFooterResponse from a JSON string
message_embed_footer_response_instance = MessageEmbedFooterResponse.from_json(json)
# print the JSON string representation of the object
print(MessageEmbedFooterResponse.to_json())

# convert the object into a dict
message_embed_footer_response_dict = message_embed_footer_response_instance.to_dict()
# create an instance of MessageEmbedFooterResponse from a dict
message_embed_footer_response_from_dict = MessageEmbedFooterResponse.from_dict(message_embed_footer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


