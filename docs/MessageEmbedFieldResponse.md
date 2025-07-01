# MessageEmbedFieldResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**inline** | **bool** |  | 

## Example

```python
from dc_rest.models.message_embed_field_response import MessageEmbedFieldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageEmbedFieldResponse from a JSON string
message_embed_field_response_instance = MessageEmbedFieldResponse.from_json(json)
# print the JSON string representation of the object
print(MessageEmbedFieldResponse.to_json())

# convert the object into a dict
message_embed_field_response_dict = message_embed_field_response_instance.to_dict()
# create an instance of MessageEmbedFieldResponse from a dict
message_embed_field_response_from_dict = MessageEmbedFieldResponse.from_dict(message_embed_field_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


