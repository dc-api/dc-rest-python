# ModalInteractionCallbackRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_id** | **str** |  | 
**title** | **str** |  | 
**components** | [**List[ActionRowComponentForModalRequest]**](ActionRowComponentForModalRequest.md) |  | 

## Example

```python
from dc_rest.models.modal_interaction_callback_request_data import ModalInteractionCallbackRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ModalInteractionCallbackRequestData from a JSON string
modal_interaction_callback_request_data_instance = ModalInteractionCallbackRequestData.from_json(json)
# print the JSON string representation of the object
print(ModalInteractionCallbackRequestData.to_json())

# convert the object into a dict
modal_interaction_callback_request_data_dict = modal_interaction_callback_request_data_instance.to_dict()
# create an instance of ModalInteractionCallbackRequestData from a dict
modal_interaction_callback_request_data_from_dict = ModalInteractionCallbackRequestData.from_dict(modal_interaction_callback_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


