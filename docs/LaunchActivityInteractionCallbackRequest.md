# LaunchActivityInteractionCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 

## Example

```python
from dc_rest.models.launch_activity_interaction_callback_request import LaunchActivityInteractionCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LaunchActivityInteractionCallbackRequest from a JSON string
launch_activity_interaction_callback_request_instance = LaunchActivityInteractionCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(LaunchActivityInteractionCallbackRequest.to_json())

# convert the object into a dict
launch_activity_interaction_callback_request_dict = launch_activity_interaction_callback_request_instance.to_dict()
# create an instance of LaunchActivityInteractionCallbackRequest from a dict
launch_activity_interaction_callback_request_from_dict = LaunchActivityInteractionCallbackRequest.from_dict(launch_activity_interaction_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


