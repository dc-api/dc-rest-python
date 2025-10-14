# LabelComponentForModalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | [optional] 
**label** | **str** |  | 
**description** | **str** |  | [optional] 
**component** | [**LabelComponentForModalRequestComponent**](LabelComponentForModalRequestComponent.md) |  | 

## Example

```python
from dc_rest.models.label_component_for_modal_request import LabelComponentForModalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LabelComponentForModalRequest from a JSON string
label_component_for_modal_request_instance = LabelComponentForModalRequest.from_json(json)
# print the JSON string representation of the object
print(LabelComponentForModalRequest.to_json())

# convert the object into a dict
label_component_for_modal_request_dict = label_component_for_modal_request_instance.to_dict()
# create an instance of LabelComponentForModalRequest from a dict
label_component_for_modal_request_from_dict = LabelComponentForModalRequest.from_dict(label_component_for_modal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


