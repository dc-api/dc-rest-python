# StringSelectOptionForRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**value** | **str** |  | 
**description** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**emoji** | [**ComponentEmojiForRequest**](ComponentEmojiForRequest.md) |  | [optional] 

## Example

```python
from dc_rest.models.string_select_option_for_request import StringSelectOptionForRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StringSelectOptionForRequest from a JSON string
string_select_option_for_request_instance = StringSelectOptionForRequest.from_json(json)
# print the JSON string representation of the object
print(StringSelectOptionForRequest.to_json())

# convert the object into a dict
string_select_option_for_request_dict = string_select_option_for_request_instance.to_dict()
# create an instance of StringSelectOptionForRequest from a dict
string_select_option_for_request_from_dict = StringSelectOptionForRequest.from_dict(string_select_option_for_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


