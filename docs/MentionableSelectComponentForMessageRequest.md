# MentionableSelectComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**custom_id** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**default_values** | [**List[MentionableSelectComponentForMessageRequestDefaultValuesInner]**](MentionableSelectComponentForMessageRequestDefaultValuesInner.md) |  | [optional] 

## Example

```python
from dc_rest.models.mentionable_select_component_for_message_request import MentionableSelectComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MentionableSelectComponentForMessageRequest from a JSON string
mentionable_select_component_for_message_request_instance = MentionableSelectComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(MentionableSelectComponentForMessageRequest.to_json())

# convert the object into a dict
mentionable_select_component_for_message_request_dict = mentionable_select_component_for_message_request_instance.to_dict()
# create an instance of MentionableSelectComponentForMessageRequest from a dict
mentionable_select_component_for_message_request_from_dict = MentionableSelectComponentForMessageRequest.from_dict(mentionable_select_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


