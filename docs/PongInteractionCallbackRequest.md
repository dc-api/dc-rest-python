# PongInteractionCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 

## Example

```python
from dc_rest.models.pong_interaction_callback_request import PongInteractionCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PongInteractionCallbackRequest from a JSON string
pong_interaction_callback_request_instance = PongInteractionCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(PongInteractionCallbackRequest.to_json())

# convert the object into a dict
pong_interaction_callback_request_dict = pong_interaction_callback_request_instance.to_dict()
# create an instance of PongInteractionCallbackRequest from a dict
pong_interaction_callback_request_from_dict = PongInteractionCallbackRequest.from_dict(pong_interaction_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


