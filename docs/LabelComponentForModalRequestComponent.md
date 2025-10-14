# LabelComponentForModalRequestComponent


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
**default_values** | [**List[UserSelectDefaultValue]**](UserSelectDefaultValue.md) |  | [optional] 
**channel_types** | **List[int]** |  | [optional] 
**options** | [**List[StringSelectOptionForRequest]**](StringSelectOptionForRequest.md) |  | 
**style** | **int** |  | 
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.label_component_for_modal_request_component import LabelComponentForModalRequestComponent

# TODO update the JSON string below
json = "{}"
# create an instance of LabelComponentForModalRequestComponent from a JSON string
label_component_for_modal_request_component_instance = LabelComponentForModalRequestComponent.from_json(json)
# print the JSON string representation of the object
print(LabelComponentForModalRequestComponent.to_json())

# convert the object into a dict
label_component_for_modal_request_component_dict = label_component_for_modal_request_component_instance.to_dict()
# create an instance of LabelComponentForModalRequestComponent from a dict
label_component_for_modal_request_component_from_dict = LabelComponentForModalRequestComponent.from_dict(label_component_for_modal_request_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


