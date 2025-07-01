# EmojiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**roles** | **List[str]** |  | 
**require_colons** | **bool** |  | 
**managed** | **bool** |  | 
**animated** | **bool** |  | 
**available** | **bool** |  | 

## Example

```python
from dc_rest.models.emoji_response import EmojiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmojiResponse from a JSON string
emoji_response_instance = EmojiResponse.from_json(json)
# print the JSON string representation of the object
print(EmojiResponse.to_json())

# convert the object into a dict
emoji_response_dict = emoji_response_instance.to_dict()
# create an instance of EmojiResponse from a dict
emoji_response_from_dict = EmojiResponse.from_dict(emoji_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


