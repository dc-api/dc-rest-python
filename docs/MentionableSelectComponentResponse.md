# MentionableSelectComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**custom_id** | **str** |  | 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**default_values** | [**List[MentionableSelectComponentResponseDefaultValuesInner]**](MentionableSelectComponentResponseDefaultValuesInner.md) |  | [optional] 

## Example

```python
from dc_rest.models.mentionable_select_component_response import MentionableSelectComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MentionableSelectComponentResponse from a JSON string
mentionable_select_component_response_instance = MentionableSelectComponentResponse.from_json(json)
# print the JSON string representation of the object
print(MentionableSelectComponentResponse.to_json())

# convert the object into a dict
mentionable_select_component_response_dict = mentionable_select_component_response_instance.to_dict()
# create an instance of MentionableSelectComponentResponse from a dict
mentionable_select_component_response_from_dict = MentionableSelectComponentResponse.from_dict(mentionable_select_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


