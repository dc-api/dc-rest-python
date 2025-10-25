# MentionableSelectComponentForModalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | [optional] 
**custom_id** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**default_values** | [**List[MentionableSelectComponentForMessageRequestDefaultValuesInner]**](MentionableSelectComponentForMessageRequestDefaultValuesInner.md) |  | [optional] 

## Example

```python
from dc_rest.models.mentionable_select_component_for_modal_request import MentionableSelectComponentForModalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MentionableSelectComponentForModalRequest from a JSON string
mentionable_select_component_for_modal_request_instance = MentionableSelectComponentForModalRequest.from_json(json)
# print the JSON string representation of the object
print(MentionableSelectComponentForModalRequest.to_json())

# convert the object into a dict
mentionable_select_component_for_modal_request_dict = mentionable_select_component_for_modal_request_instance.to_dict()
# create an instance of MentionableSelectComponentForModalRequest from a dict
mentionable_select_component_for_modal_request_from_dict = MentionableSelectComponentForModalRequest.from_dict(mentionable_select_component_for_modal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


