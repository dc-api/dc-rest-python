# ComponentEmojiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**animated** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.component_emoji_response import ComponentEmojiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentEmojiResponse from a JSON string
component_emoji_response_instance = ComponentEmojiResponse.from_json(json)
# print the JSON string representation of the object
print(ComponentEmojiResponse.to_json())

# convert the object into a dict
component_emoji_response_dict = component_emoji_response_instance.to_dict()
# create an instance of ComponentEmojiResponse from a dict
component_emoji_response_from_dict = ComponentEmojiResponse.from_dict(component_emoji_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


