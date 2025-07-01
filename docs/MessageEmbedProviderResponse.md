# MessageEmbedProviderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.message_embed_provider_response import MessageEmbedProviderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageEmbedProviderResponse from a JSON string
message_embed_provider_response_instance = MessageEmbedProviderResponse.from_json(json)
# print the JSON string representation of the object
print(MessageEmbedProviderResponse.to_json())

# convert the object into a dict
message_embed_provider_response_dict = message_embed_provider_response_instance.to_dict()
# create an instance of MessageEmbedProviderResponse from a dict
message_embed_provider_response_from_dict = MessageEmbedProviderResponse.from_dict(message_embed_provider_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


