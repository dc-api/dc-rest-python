# StringSelectOptionForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**value** | **str** |  | 
**description** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**emoji** | [**ComponentEmojiForMessageRequest**](ComponentEmojiForMessageRequest.md) |  | [optional] 

## Example

```python
from dc_rest.models.string_select_option_for_message_request import StringSelectOptionForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StringSelectOptionForMessageRequest from a JSON string
string_select_option_for_message_request_instance = StringSelectOptionForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(StringSelectOptionForMessageRequest.to_json())

# convert the object into a dict
string_select_option_for_message_request_dict = string_select_option_for_message_request_instance.to_dict()
# create an instance of StringSelectOptionForMessageRequest from a dict
string_select_option_for_message_request_from_dict = StringSelectOptionForMessageRequest.from_dict(string_select_option_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


