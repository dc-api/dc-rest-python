# StringSelectOptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**value** | **str** |  | 
**description** | **str** |  | [optional] 
**emoji** | [**ComponentEmojiResponse**](ComponentEmojiResponse.md) |  | [optional] 
**default** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.string_select_option_response import StringSelectOptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StringSelectOptionResponse from a JSON string
string_select_option_response_instance = StringSelectOptionResponse.from_json(json)
# print the JSON string representation of the object
print(StringSelectOptionResponse.to_json())

# convert the object into a dict
string_select_option_response_dict = string_select_option_response_instance.to_dict()
# create an instance of StringSelectOptionResponse from a dict
string_select_option_response_from_dict = StringSelectOptionResponse.from_dict(string_select_option_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


