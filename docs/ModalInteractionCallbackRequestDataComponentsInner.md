# ModalInteractionCallbackRequestDataComponentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | [optional] 
**components** | [**List[TextInputComponentForModalRequest]**](TextInputComponentForModalRequest.md) |  | 
**label** | **str** |  | 
**description** | **str** |  | [optional] 
**component** | [**LabelComponentForModalRequestComponent**](LabelComponentForModalRequestComponent.md) |  | 
**content** | **str** |  | 

## Example

```python
from dc_rest.models.modal_interaction_callback_request_data_components_inner import ModalInteractionCallbackRequestDataComponentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModalInteractionCallbackRequestDataComponentsInner from a JSON string
modal_interaction_callback_request_data_components_inner_instance = ModalInteractionCallbackRequestDataComponentsInner.from_json(json)
# print the JSON string representation of the object
print(ModalInteractionCallbackRequestDataComponentsInner.to_json())

# convert the object into a dict
modal_interaction_callback_request_data_components_inner_dict = modal_interaction_callback_request_data_components_inner_instance.to_dict()
# create an instance of ModalInteractionCallbackRequestDataComponentsInner from a dict
modal_interaction_callback_request_data_components_inner_from_dict = ModalInteractionCallbackRequestDataComponentsInner.from_dict(modal_interaction_callback_request_data_components_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


