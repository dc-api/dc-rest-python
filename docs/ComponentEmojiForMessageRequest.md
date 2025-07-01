# ComponentEmojiForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from dc_rest.models.component_emoji_for_message_request import ComponentEmojiForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentEmojiForMessageRequest from a JSON string
component_emoji_for_message_request_instance = ComponentEmojiForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(ComponentEmojiForMessageRequest.to_json())

# convert the object into a dict
component_emoji_for_message_request_dict = component_emoji_for_message_request_instance.to_dict()
# create an instance of ComponentEmojiForMessageRequest from a dict
component_emoji_for_message_request_from_dict = ComponentEmojiForMessageRequest.from_dict(component_emoji_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


