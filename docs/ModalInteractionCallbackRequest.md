# ModalInteractionCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**data** | [**ModalInteractionCallbackRequestData**](ModalInteractionCallbackRequestData.md) |  | 

## Example

```python
from dc_rest.models.modal_interaction_callback_request import ModalInteractionCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModalInteractionCallbackRequest from a JSON string
modal_interaction_callback_request_instance = ModalInteractionCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(ModalInteractionCallbackRequest.to_json())

# convert the object into a dict
modal_interaction_callback_request_dict = modal_interaction_callback_request_instance.to_dict()
# create an instance of ModalInteractionCallbackRequest from a dict
modal_interaction_callback_request_from_dict = ModalInteractionCallbackRequest.from_dict(modal_interaction_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


